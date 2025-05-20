import unittest

from textnode import TextNode, TextType
from splitnodes import (split_nodes_delimiter, extract_markdown_images, 
                        extract_markdown_links, split_nodes_images, split_nodes_links, text_to_textnodes)

class TestSplitNodes(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )
    
    def test_delim_bold_double(self):
        node = TextNode("This is **text** with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )
    
    def test_delim_bold_multiword(self):
        node = TextNode("This is text with a **bolded word**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded word", TextType.BOLD),
            ],
            new_nodes,
        )
    

    def test_delim_italic(self):
        node = TextNode("This is text with a *italicized* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_italic_double(self):
        node = TextNode("This is *text* with a *italicized* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.ITALIC),
                TextNode(" with a ", TextType.NORMAL),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )
    
    def test_delim_italic_multiword(self):
        node = TextNode("This is text with a *italicized word*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("italicized word", TextType.ITALIC),
            ],
            new_nodes,
        )
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_no_alt_text(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_no_url(self):
        matches = extract_markdown_images(
            "This is text with an ![image]()"
        )
        self.assertListEqual([("image", "")], matches)
    
    def test_extract_markdown_images_no_alt_text_no_url(self):
        matches = extract_markdown_images(
            "This is text with an ![]()"
        )
        self.assertListEqual([("", "")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links_no_text(self):
        matches = extract_markdown_links(
            "This is a text with a [](https://i.imgur.com/zjjcJKZ.png)"     
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links_no_url(self):
        matches = extract_markdown_links(
            "This is a text with a [link]()"
        )
        self.assertListEqual([("link", "")], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_no_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    
    def test_split_images_no_url(self):
        node = TextNode(
            "This is text with an ![image]()",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, ""),
            ],
            new_nodes,
        )
    
    def test_split_images_no_alt_text(self):
        node = TextNode(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [link](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_no_text(self):
        node = TextNode(
            "This is text with a [](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    
    def test_split_links_no_url(self):
        node = TextNode(
            "This is text with a [link]()",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, ""),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        text = "This is a text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("This is a text node", TextType.NORMAL)],
            nodes,
        )

    def text_text_to_textnodes_bold(self):
        text = "This is a **bold** text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_italic(self):
        text = "This is a *italic* text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_code(self):
        text = "This is a `code` text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_link(self):
        text = "This is a [link](https://i.imgur.com/zjjcJKZ.png) text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_image(self):
        text = "This is a ![image](https://i.imgur.com/zjjcJKZ.png) text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    def test_text_to_textnodes_multiple(self):
        text = "This is a **bold** *italic* `code` [link](https://i.imgur.com/zjjcJKZ.png) ![image](https://i.imgur.com/zjjcJKZ.png) text node"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text node", TextType.NORMAL),
            ],
            nodes,
        )
    
    