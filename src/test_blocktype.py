import unittest
from blocktype import BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(BlockType.block_to_block_type(block), BlockType.PARAGRAPH)
        block = "# This is a heading"
        self.assertEqual(BlockType.block_to_block_type(block), BlockType.HEADING)
        block = "```\nThis is a code block\n```"
        self.assertEqual(BlockType.block_to_block_type(block), BlockType.CODE)
        block = "> This is a quote"
        self.assertEqual(BlockType.block_to_block_type(block), BlockType.QUOTE)
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(BlockType.block_to_block_type(block), BlockType.UNORDERED_LIST)