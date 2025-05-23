from blockmarkdown import markdown_to_html_node, extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown_data = markdown_file.read()
        file_content = markdown_to_html_node(markdown_data).to_html()
        file_title = extract_title(markdown_data)
    with open(template_path) as template_file:
        template_data = template_file.read()
        template_data = template_data.replace("{{ Title }}", file_title).replace('href="/', f'href="{basepath}')
        template_data = template_data.replace("{{ Content }}", file_content).replace('src="/', f'src="{basepath}')
    # Create the directory if it doesn't exist        
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the modified template to the destination file
    with open(dest_path, "w") as dest_file:
        dest_file.write(template_data)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # Crawl through every directory
    for entry in os.listdir(dir_path_content):
        # If entry is a file, call generate_pages
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        current_content_path = Path(os.path.join(dir_path_content, entry))
        original_content_path = Path(dir_path_content)    
        relative_content_path = Path(current_content_path.relative_to(original_content_path))    
        dest_content_path = Path(dest_dir_path / relative_content_path).with_suffix(".html")
        if os.path.isfile(entry_path):
            generate_page(entry_path, template_path, dest_content_path, basepath)
        else:
            os.mkdir(dest_path)
            generate_pages_recursive(current_content_path, template_path, dest_path, basepath)    