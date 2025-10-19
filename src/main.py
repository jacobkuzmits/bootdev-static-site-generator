import os
import shutil
from utils.generate_page import generate_page
from utils.generate_pages_recursive import generate_pages_recursive


def copy_static_to_public():
    # delete public/
    if os.path.exists("public"):
        shutil.rmtree("public")
        print("Deleted public/")

    # create public/
    os.mkdir("public")

    # copy static/ into public/
    copy_directory("static", "public")

    # generate all pages from markdown
    generate_pages_recursive("content", "template.html", "public")


def copy_directory(src, target):
    src_path = os.path.abspath(os.path.join(".", src))
    target_path = os.path.abspath(os.path.join(".", target))
    src_contents = os.listdir(src_path)
    for item in src_contents:
        item_path = os.path.join(src_path, item)
        is_dir = os.path.isdir(item_path)
        if not is_dir:
            target_file_path = os.path.join(target_path, item)
            shutil.copy(item_path, target_file_path)
            print(f"copied {item_path} to {target_file_path}")
        else:
            target_dir_path = os.path.join(target_path, item)
            os.mkdir(target_dir_path)
            print(f"created directory {target_dir_path}")
            copy_directory(item_path, target_dir_path)


def main():
    copy_static_to_public()


if __name__ == "__main__":
    main()
