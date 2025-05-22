import unittest
from blockmarkdown import markdown_to_blocks, markdown_to_html_node, extract_title




class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_h1(self):
            md = """
    # My Awesome Title

    Some content here.
    """
            self.assertEqual(extract_title(md), "My Awesome Title")

    def test_extract_title_h1_with_leading_spaces(self):
            md = """
       #    Another Title

    Paragraph.
    """
            self.assertEqual(extract_title(md), "Another Title")

    def test_extract_title_h1_not_first_line(self):
            md = """
    Some intro text.

    # The Real Title

    More text.
    """
            self.assertEqual(extract_title(md), "The Real Title")

    def test_extract_title_no_h1_raises(self):
            md = """
    ## Not a main title

    Some content.
    """
            with self.assertRaises(Exception) as context:
                extract_title(md)
            self.assertIn("No header found", str(context.exception))

    def test_extract_title_h1_with_markdown_inline(self):
            md = """
    # Title with **bold** and _italic_

    Body.
    """
            self.assertEqual(extract_title(md), "Title with **bold** and _italic_")

if __name__ == "__main__":
    unittest.main()