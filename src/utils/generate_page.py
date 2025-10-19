import os
from utils.markdown_to_html_node import markdown_to_html_node
from utils.extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    with open(os.path.join(".", from_path), "r") as markdown_file:
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        markdown = markdown_file.read()
        with open(os.path.join(".", template_path), "r") as template_file:
            template = template_file.read()
            content_html = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            with_title = template.replace("{{ Title }}", title)
            with_content = with_title.replace("{{ Content }}", content_html)
            fixed_links = with_content.replace('href="/', f'href="{basepath}')
            fixed_src = fixed_links.replace('src="/', f'src="{basepath}')
            directory = os.path.dirname(dest_path)
            os.makedirs(directory, exist_ok=True)
            with open(os.path.join(".", dest_path), "x") as dest_file:
                dest_file.write(fixed_src)
