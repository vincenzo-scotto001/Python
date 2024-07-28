"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

"""


import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}
        self.alphabet = string.ascii_letters + string.digits

    def shorten(self, url):
        # Check if the URL has already been shortened
        if url in self.url_to_short:
            return self.url_to_short[url]

        # Generate a new short URL
        while True:
            short = ''.join(random.choice(self.alphabet) for _ in range(6))
            if short not in self.short_to_url:
                self.url_to_short[url] = short
                self.short_to_url[short] = url
                return short

    def restore(self, short):
        # Return the original URL if it exists, otherwise return None
        return self.short_to_url.get(short)

# Example usage
shortener = URLShortener()

# Shorten a URL
original_url = "https://www.example.com/very/long/url/path"
shortened = shortener.shorten(original_url)
print(f"Shortened URL: {shortened}")

# Restore the URL
restored_url = shortener.restore(shortened)
print(f"Restored URL: {restored_url}")

# Try to restore a non-existent short URL
non_existent = shortener.restore("abcdef")
print(f"Non-existent URL: {non_existent}")

# Shorten the same URL again
shortened_again = shortener.shorten(original_url)
print(f"Shortened again: {shortened_again}")