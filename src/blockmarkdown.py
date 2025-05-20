from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from blocktype import BlockType
from splitnodes import text_to_textnodes
import re

def markdown_to_blocks(markdown):
    """
    Convert a markdown string to a list of blocks.
    """
    # Split the markdown into blocks
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            # If the block is empty, skip it
            continue
        # If the block is not empty, add it to the list of blocks
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def text_to_children(text):
    """Convert a string with inline markdown to a list of HTMLNode objects"""
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def paragraph_to_html_node(block):
    """
    Convert a paragraph string to an HTML node.
    """
    # Replace newlines with spaces and normalize whitespace
    block = re.sub(r'\s+', ' ', block.replace("\n", " ")).strip()
    
    # Create paragraph node
    paragraph_node = ParentNode("p", [])
    # Process inline markdown
    paragraph_node.children = text_to_children(block)
    return paragraph_node

def heading_to_html_node(block):
    """
    Convert a heading string to an HTML node.
    """
    # Get the level of the heading
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    
    level = max(1, min(6, level))
    content = block[level:].strip()
    heading_node = ParentNode(f"h{level}", [])         
    heading_node.children = text_to_children(content)
    return heading_node

def code_block_to_html_node(block):
    """
    Convert a code block to HTML node without parsing markdown inside
    """
    
    lines = block.strip().split('\n')
    
    # Skip the first line (contains ```)
    # And also skip the last line if it contains ```
    content_lines = []
    for i in range(1, len(lines)):
        if i == len(lines) - 1 and "```" in lines[i]:
            continue
        # Remove the leading whitespace/indentation
        content_lines.append(lines[i].strip())
    
    # Join the content lines, preserving newlines and add an extra newline at the end
    content = '\n'.join(content_lines) + '\n'
    
    # Create a LeafNode for the code content
    code_node = LeafNode("code", content)
    
    # Wrap in pre ParentNode
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def quote_to_html_node(block):
    """
    Convert a quote string to an HTML node.
    """
    lines = block.split("\n")
    cleaned_lines = [line[1:].strip() for line in lines if line.startswith(">")]
    content = "\n".join(cleaned_lines).strip()
    # Create blockquote node
    blockquote_node = ParentNode("blockquote", [])
    blockquote_node.children = text_to_children(content)
    return blockquote_node
    
def unordered_list_to_html_node(block):
    """
    Convert an unordered list string to an HTML node.
    """
    lines = block.split("\n")
    items = [line[2:].strip() for line in lines if line.startswith("- ")]
    # Create unordered list node
    ul_node = ParentNode("ul", [])
    for item in items:
        li_node = ParentNode("li", [])
        li_node.children = text_to_children(item)
        ul_node.children.append(li_node)
    return ul_node


        
    # Update ordered_list_to_html_node to handle any number at the start

def ordered_list_to_html_node(block):
        """
        Convert an ordered list string to an HTML node.
        """        
        lines = block.split("\n")
        items = []
        for line in lines:
            match = re.match(r"^\s*\d+\.\s+(.*)", line)
            if match:
                items.append(match.group(1).strip())
        # Create ordered list node
        ol_node = ParentNode("ol", [])
        for item in items:
            li_node = ParentNode("li", [])
            li_node.children = text_to_children(item)
            ol_node.children.append(li_node)
        return ol_node    

def markdown_to_html_node(markdown):
    """
    Convert a markdown string to an HTML node.
    """
    parent_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if not block.strip():
            continue
        block_type = BlockType.block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block_node = paragraph_to_html_node(block)
        elif block_type == BlockType.HEADING:
            block_node = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            block_node = code_block_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            block_node = quote_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            block_node = ordered_list_to_html_node(block)
        else:
            block_node = paragraph_to_html_node(block)
        
        parent_node.children.append(block_node)
    return parent_node

  