from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    """Enum for text types."""
    NORMAL = "text"
    BOLD = "bold"
    ITALIC= "italic"
    CODE= "code"
    LINK = "link"
    IMAGE = "image"
    

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
        )
            
    def __repr__(self):
        return f"TextNode({str(self.text)}, {self.text_type.value}, {str(self.url)})"

def text_node_to_html_node(text_node):
    """Convert a TextNode to an HTMLNode."""
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Unknown text type: {text_node.text_type}")
        
