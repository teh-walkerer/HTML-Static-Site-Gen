from blockmarkdown import markdown_to_html_node, extract_title
import os

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