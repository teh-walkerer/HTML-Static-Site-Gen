from blockmarkdown import markdown_to_html_node, extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown_data = markdown_file.read()
        file_content = markdown_to_html_node(markdown_data).to_html()
        file_title = extract_title(markdown_data)
    with open(template_path) as template_file:
        template_data = template_file.read()
        template_data = template_data.replace("{{ Title }}", file_title)
        template_data = template_data.replace("{{ Content }}", file_content)
    # Create the directory if it doesn't exist        
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the modified template to the destination file
    with open(dest_path, "w") as dest_file:
        dest_file.write(template_data)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            with open(os.path.join(dir_path_content, entry)) as markdown_file:
                markdown_data = markdown_file.read()
                file_content = markdown_to_html_node(markdown_data).to_html()
                file_title = extract_title(markdown_data)
            with open(template_path) as template_file:
                template_data = template_file.read()
                template_data = template_data.replace("{{ Title }}", file_title)
                template_data = template_data.replace("{{ Content }}", file_content)
            current_content_path = Path(os.path.join(dir_path_content, entry))
            original_content_path = Path(dir_path_content)    
            relative_content_path = Path(current_content_path.relative_to(original_content_path))    
            dest_content_path = Path(dest_dir_path / relative_content_path).with_suffix(".html")
            dest_content_path_parent = dest_content_path.parent

            os.makedirs(dest_content_path_parent, exist_ok=True)

            with open(dest_content_path, "w") as dest_file:
                dest_file.write(template_data)
        else:
            os.mkdir(os.path.join(dest_dir_path, entry))
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))