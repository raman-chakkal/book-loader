import requests
import os

def download_pdf(url, save_dir="downloads", filename="book.pdf"):
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, filename)

    response = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

    print(f"✅ Downloaded to: {file_path}")
