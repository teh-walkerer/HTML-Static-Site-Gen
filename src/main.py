from copydirectory import recursive_copy
from generatepage import generate_pages_recursive
import sys

destination_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/docs"
source_dir = "/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/static"
template = "template.html"
content = "content/"
html_file_to_generate = "docs/"
def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    recursive_copy(source_dir, destination_dir)
    generate_pages_recursive(content, template, html_file_to_generate, basepath)

if __name__ == "__main__":
    main()