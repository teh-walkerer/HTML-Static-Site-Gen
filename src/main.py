from textnode import TextNode
from textnode import TextType
from copydirectory import recursive_copy
from generatepage import generate_page

destination_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/public"
source_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/static"
template = "github.com/teh-walkerer/HTML-Static-Site-Gen/template.html"
content = "github.com/teh-walkerer/HTML-Static-Site-Gen/content/index.md"
html_file_to_generate = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/public/index.html"
def main():
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    recursive_copy(source_dir, destination_dir)
    generate_page(content, template, html_file_to_generate)

if __name__ == "__main__":
    main()