from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split a list of TextNodes into two lists based on a delimiter."""
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != text_type.NORMAL:
            # If the node is not of the specified text type, add it to the new nodes
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Delimiter splits the text into an even number of sections.")
        # If the node is of the specified text type, split it at the delimiter
        for i in range(len(sections)):
            if sections[i] == "":
                # If the section is empty, skip it
                continue
            if i % 2 == 0:
                # If the index is even, add the section to the new nodes
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                # If the index is odd, add the section to the new nodes
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    
    return new_nodes

def extract_markdown_images(text):
    """Extract images from a markdown text."""
    markdown_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return markdown_images

def extract_markdown_links(text):
    """Extract links from a markdown text."""
    markdown_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return markdown_links

def split_nodes_images(old_nodes):
    """Split a list of TextNodes into two lists based on images."""
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            # If the node is not of the specified text type, add it to the new nodes
            new_nodes.append(node)
            continue
        # If the node is of the specified text type, split it at the images
        index = 0
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            # If there are no images, add the node to the new nodes
            new_nodes.append(node)
            continue
        for match in matches:
            # If there are images, split the node at the images
            image_text, image_url = match
            full_md = f"![{image_text}]({image_url})"
            # Find the index of the image in the node text
            start = node.text.find(full_md, index)
            if start == -1:
                # If the image is not found, raise an error
                raise ValueError(f"Image {full_md} not found in node text.")
            end = start + len(full_md)
            # Create a new TextNode for the image
            image_node = TextNode(image_text, TextType.IMAGE, image_url)
            if node.text[index:start] != "":
                # If there is text before the image, create a new TextNode for it
                text_node = TextNode(node.text[index:start], TextType.NORMAL)
                new_nodes.append(text_node)
            # Add the image node to the new nodes
            new_nodes.append(image_node)
            index = end
        if index < len(node.text):
            # If there is text after the last image, create a new TextNode for it
            text_node = TextNode(node.text[index:], TextType.NORMAL)
            new_nodes.append(text_node)
    
    return new_nodes

def split_nodes_links(old_nodes):
    
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            # If the node is not of the specified text type, add it to the new nodes
            new_nodes.append(node)
            continue
        # If the node is of the specified text type, split it at the links
        index = 0
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            # If there are no links, add the node to the new nodes
            new_nodes.append(node)
            continue
        for match in matches:
            # If there are links, split the node at the links
            link_text, link_url = match
            full_md = f"[{link_text}]({link_url})"
            # Find the index of the link in the node text
            start = node.text.find(full_md, index)
            if start == -1:
                # If the link is not found, raise an error
                raise ValueError(f"Link {full_md} not found in node text.")
            end = start + len(full_md)
            # Create a new TextNode for the link
            link_node = TextNode(link_text, TextType.LINK, link_url)
            if node.text[index:start] != "":
                # If there is text before the link, create a new TextNode for it
                text_node = TextNode(node.text[index:start], TextType.NORMAL)
                new_nodes.append(text_node)
            # Add the link node to the new nodes
            new_nodes.append(link_node)
            index = end
        if index < len(node.text):
            # If there is text after the last link, create a new TextNode for it
            text_node = TextNode(node.text[index:], TextType.NORMAL)
            new_nodes.append(text_node)
    
    return new_nodes

def text_to_textnodes(text):
    """Convert a text to a list of TextNodes."""
    # Start with the input text as a single TextNode
    nodes = [TextNode(text, TextType.NORMAL)]
    for delimiter, text_type in [
        ("**", TextType.BOLD),
        ("*", TextType.ITALIC),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    
    # Split the nodes at the images
    nodes = split_nodes_images(nodes)
    
    # Split the nodes at the links
    nodes = split_nodes_links(nodes)
    
    return nodes