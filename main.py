from link_shortener import LinkShortener

def main():
    """
    Main function to shorten URLs and display the shortened IDs.
    """
    urls = [
        "https://walla.co.il",
        "https://nana.co.il"
    ]

    for url in urls:
        try:
            shortened_url = LinkShortener.shorten(url)
            print("Shortened URL:", shortened_url)
        except Exception as e:
            print("Error occurred:", e)

if __name__ == "__main__":
    main()
