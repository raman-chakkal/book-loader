from google_scraper import generate_query, find_pdf_links
from downloader import download_pdf

def main():
    print("📚 Free Book PDF Finder (Google Search Method)")
    book = input("Enter the book name: ")
    lang = input("Enter the language code (e.g., en, fr): ")

    query = generate_query(book, lang)
    print(f"\n🔍 Searching for: {query}\n")

    links = find_pdf_links(query)
    if not links:
        print("❌ No PDF links found.")
        return

    for idx, link in enumerate(links):
        print(f"{idx + 1}. {link}")

    choice = int(input("Pick a file to download (1-N): ")) - 1
    selected_link = links[choice]
    filename = input("Enter a filename (e.g., mybook.pdf): ")

    download_pdf(selected_link, filename=filename)

if __name__ == "__main__":
    main()
