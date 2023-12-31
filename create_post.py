# create_post.py
# helper script to create a directory with a notebook for the blog

import os
import datetime as dt
import nbformat as nbf

current_dir = os.getcwd()
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

name = input("folder-name? ")

# move to the posts folder, then create and enter the new folder
os.chdir(os.path.join(current_dir, "posts"))
os.mkdir(name)
os.chdir(name)

# create an populate a new notebook with the template
nb = nbf.v4.new_notebook()
nb["cells"] = [nbf.v4.new_raw_cell(template), nbf.v4.new_markdown_cell(placeholder)]
nbf.write(nb, "index.ipynb")

print("[+] done")
