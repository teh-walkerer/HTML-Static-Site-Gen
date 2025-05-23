from textnode import TextNode
from textnode import TextType
from copydirectory import recursive_copy
from generatepage import generate_pages_recursive

destination_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/public"
source_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/static"
template = "template.html"
content = "content/"
html_file_to_generate = "public/"
def main():
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    recursive_copy(source_dir, destination_dir)
    generate_pages_recursive(content, template, html_file_to_generate)

if __name__ == "__main__":
    main()