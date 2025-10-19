import os
from utils.generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_path = os.path.abspath(os.path.join(".", dir_path_content))
    dest_path = os.path.abspath(os.path.join(".", dest_dir_path))
    template_abs_path = os.path.abspath(template_path)
    contents = os.listdir(content_path)
    for item in contents:
        item_path = os.path.join(content_path, item)
        is_dir = os.path.isdir(item_path)
        if not is_dir:
            target_file_path = os.path.join(dest_path, item)
            print(f"generating {target_file_path} from {item_path}")
            generate_page(
                item_path,
                template_abs_path,
                target_file_path.replace(".md", ".html"),
                basepath,
            )
        else:
            target_dir_path = os.path.join(dest_path, item)
            os.mkdir(target_dir_path)
            print(f"created directory {target_dir_path}")
            generate_pages_recursive(
                item_path, template_abs_path, target_dir_path, basepath
            )
