from textnode import *
import re
import os 
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path_static = os.path.join(base_dir, "static")
dir_path_public = os.path.join(base_dir, "public")
dir_path_content = os.path.join(base_dir, "content")
template_path = os.path.join(base_dir, "template.html")



def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()

def extract_markdown_images(text):  
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
