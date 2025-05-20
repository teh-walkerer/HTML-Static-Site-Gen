
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """A class representing an HTML node."""
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        """Convert the properties of the node to an HTML string."""
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """A class representing a leaf node in the HTML tree."""
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        """Convert the node to an HTML string."""
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """A class representing a parent node in the HTML tree."""
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        """Convert the node to an HTML string."""
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"