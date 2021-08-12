import re
import os

with open('base.html', encoding='utf-8') as base_content:
    base_content_str = base_content.read()
    for folder in os.listdir('pages'):
        with open(f'pages/{folder}/dicas/content.html') as content:
            content_str = content.read()
            page = open(f'pages/{folder}/index.html', 'w')
            full_content = base_content_str.replace('{{content}}', content_str)\
                .replace('{{header}}', '')
            page.write(full_content)  
            page.close()
    with open('base.html', 'r', encoding='utf-8') as base_content:
        base_content_str = base_content.read()
        with open('index_content.html', 'r') as index_content:
            index_content_str = index_content.read()
            index_str = base_content_str.replace('{{content}}', index_content_str)
            index = open('index.html', 'w')            
            index.write(index_str)
            index.close()