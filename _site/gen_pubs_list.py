#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:29:13 2024

@author: omrile
"""

import pandas as pd


input_excel = 'pubs_list.xlsx'
output_md = '_pages/publications.md'

# Read Excel file
df = pd.read_excel(input_excel)
df = df.iloc[::-1].reset_index(drop=True)

# Open Markdown file for writing
with open(output_md, 'w', encoding='utf-8') as md_file:
    # Write header
    md_file.write('---\nlayout: archive\ntitle: "Publications"\npermalink: /publications/\nauthor_profile: true\n---\n\n')
    md_file.write(f"<p></p>\n\n")
    md_file.write("| --------------------------- | ------------ |\n")

    # Iterate through rows and write markdown
    for index, row in df.iterrows():
        image_path = f"/images/thumbnails/{row['image']}"
        authors = row['Authors']
        title = row['Title']
        journal_ref = row['Journal-Ref']
        url = row['URL']

        md_file.write(f"| ![txt]({image_path}) | {index + 1}. {authors}<br/>_{title}_<br/>[{journal_ref}]({url}) |\n")
    
    md_file.write("\n<sub>* Equal contribution</sub>")
    md_file.write("\n")

print(f"Markdown file '{output_md}' generated successfully.")
