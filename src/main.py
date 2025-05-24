from copydirectory import recursive_copy
from generatepage import generate_pages_recursive
import sys

destination_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/docs"
source_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/static"
template = "template.html"
content = "content/"
html_file_to_generate = "docs/"
def main():
    user_input = sys.argv[1].strip()
    if user_input == "":
        raise Exception("basepath cannot be empty or whitespace")
    if user_input == "/":
        basepath = "/"
    else:
        basepath = user_input.rstrip("/") + "/"
    recursive_copy(source_dir, destination_dir)
    generate_pages_recursive(content, template, html_file_to_generate, basepath)

if __name__ == "__main__":
    main()