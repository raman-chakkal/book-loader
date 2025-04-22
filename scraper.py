from googlesearch import google
import re

def generate_query(book_name, language):
    return f'"{book_name}" filetype:pdf lang:{language}'

def find_pdf_links(query, num_results=10):
    links = []
    for url in search(query, num_results=num_results):
        if re.search(r"\.pdf$", url):
            links.append(url)
    return links
