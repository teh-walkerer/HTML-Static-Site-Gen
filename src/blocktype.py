from enum import Enum

class BlockType(Enum):
    """Enum for block types."""
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

    def block_to_block_type(block):
        """Convert a block to a block type."""
        block = block.strip()
        lines = block.split("\n")
        if block.startswith("#"):
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                else:
                    break
            if 1 <= count <= 6 and block[count] == ' ':
                return BlockType.HEADING
        if block.startswith("```") and block.endswith("```"):
            return BlockType.CODE
        if block.startswith(">"):
            if all(line.startswith(">") for line in lines):
                return BlockType.QUOTE
        if block.startswith("- "):
            if all(line.startswith("- ") for line in lines):
                return BlockType.UNORDERED_LIST
        is_ordered = len(lines) > 0
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                is_ordered = False
                break
        if is_ordered:    
            return BlockType.ORDERED_LIST
        return BlockType.PARAGRAPH