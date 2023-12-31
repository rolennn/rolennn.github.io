# manage_post.py
# helper script to create a directory with a notebook (create_post)
# or edit a current notebook (edit_post) for the blog.

# [1/1/2023] i am opening vscode to edit the notebook instead of 
# jupyter-lab because: (1) i don't want to open another kernel 
# just to edit a notebook; and (2) i don't think it's possible to 
# edit notebooks in the terminal. unless i can think of another way
# to allow editing, this can suffice.

import os
import datetime as dt
import nbformat as nbf

current_dir = os.getcwd().split("\\")
blog_dir = current_dir[:7]                          # until .../projects/blog
current_time = str(dt.date.today())
template = f"""---
title: ""
date: "{current_time}"
categories: []
format: 
  html:
    code-fold: true
    toc: true
jupyter: python3
---"""
placeholder = "This is a post."


def edit_post():
    try:
        # assuming that we are currently at blog_dir (from main)
        os.system("code .")
        print("[+] vscode open for edits")
    except: 
        print("[!] something very bad: code")

def create_post(folder_name):
    # create and jump to a new directory (<blog_name>/posts/<folder_name>)
    folder_subdir = ["rolennn.github.io", "posts", folder_name]
    os.mkdir("\\".join(folder_subdir))
    os.chdir("\\".join(blog_dir + folder_subdir))

    # create an populate a new notebook with the template
    nb = nbf.v4.new_notebook()
    nb["cells"] = [nbf.v4.new_raw_cell(template), nbf.v4.new_markdown_cell(placeholder)]
    nbf.write(nb, "index.ipynb")

    print("[+] folder created")
    os.chdir("\\".join(blog_dir))
    edit_post()


if __name__ == "__main__":
    # move to the main blog directory
    os.chdir("\\".join(blog_dir))
    
    task = input("[1]edit [2]create ? ")
    if (task in ['1', '']):
        edit_post()
    elif (task == '2'):
        name = input("folder-name ? ")
        create_post(name)
    else:
        print("[!] stupid")
