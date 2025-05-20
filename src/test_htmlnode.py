import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", {"class": "contained"})
        self.assertNotEqual(repr(node), "HTMLNode(div, This is a div, None, {'class': 'contained'})")
    def test_repr_with_children(self):
        node = HTMLNode("h1", "This is a heading", {"class": "heading"}, [HTMLNode("p", "This is a paragraph")])
        self.assertNotEqual(repr(node), "HTMLNode(h1, This is a heading, None, {'class': 'heading'}, [HTMLNode(p, This is a paragraph, None, None)])")
    def test_repr_with_no_children(self):
        node = HTMLNode("h1", "This is a heading", {"class": "heading"})
        self.assertNotEqual(repr(node), "HTMLNode(h1, This is a heading, None, {'class': 'heading'})")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src": "image.png"})
        self.assertEqual(node.to_html(), '<img src="image.png"></img>')
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click here</a>')
    
    def test_leaf_to_html_without_props(self):
        node = LeafNode("a", "Click here")
        self.assertEqual(node.to_html(), "<a>Click here</a>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_no_tag_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_no_props(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_empty_props(self):
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_no_tag(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )
    def test_to_html_with_no_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {})
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_none_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_parent_child(self):
        child_node = ParentNode("span", [LeafNode("b", "grandchild")])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
  
    def test_to_html_with_parent_child_and_props(self):
        child_node = ParentNode("span", [LeafNode("b", "grandchild")], {"class": "child"})
        parent_node = ParentNode("div", [child_node], {"class": "parent"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="parent"><span class="child"><b>grandchild</b></span></div>',
        )
    
    def test_to_html_with_parent_node_and_none_tag(self):
        child_node = ParentNode("span", [LeafNode(None, "grandchild")])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>grandchild</span></div>",
        )
    
    def test_to_html_with_parent_node_and_none_tag_and_none_value(self):
        child_node = ParentNode(None, [LeafNode(None, None)])
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_parent_node_and_none_tag_and_none_value_and_none_props(self):
        child_node = ParentNode(None, [LeafNode(None, None)], None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_parent_node_with_empty_childen_list(self):
        child_node = ParentNode("b", [])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><b></b></div>")
