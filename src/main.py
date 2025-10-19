import os
import sys
import shutil
import json
from utils.generate_page import generate_page
from utils.generate_pages_recursive import generate_pages_recursive


def copy_static_to_docs(basepath):
    # delete public/
    if os.path.exists("docs"):
        shutil.rmtree("docs")
        print("Deleted docs/")

    # create public/
    os.mkdir("docs")

    # copy static/ into public/
    copy_directory("static", "docs")

    # generate all pages from markdown
    generate_pages_recursive(
        os.path.join(".", "content"),
        os.path.join(".", "template.html"),
        os.path.join(".", "docs"),
        basepath,
    )


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


def load_config():
    config_path = os.path.join(".", "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {config_path} not found, using default values")
        return {"basepath": {"local": "/", "production": "/"}}


def main():
    config = load_config()

    # Check if environment is specified (local or production)
    if len(sys.argv) >= 2 and sys.argv[1] in ["local", "production"]:
        env = sys.argv[1]
        basepath = config["basepath"][env]
    else:
        # Default to local
        basepath = config["basepath"]["local"]

    print(f"using basepath: {basepath}")

    copy_static_to_docs(basepath)


if __name__ == "__main__":
    main()
