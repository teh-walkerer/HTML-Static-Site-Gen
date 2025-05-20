from textnode import TextNode
from textnode import TextType


def main():
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)

main()