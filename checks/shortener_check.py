"""URL-shortener heuristic: a shortened link hides the real destination, which
is why shorteners are a classic phishing carrier."""

from urllib.parse import urlparse

# Well-known shortener domains. The list is deliberately exact: an unknown
# shortener is not a signal by itself.
SHORTENERS = {
    "bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd",
    "ow.ly", "buff.ly", "adf.ly", "cutt.ly", "rebrand.ly",
}


def check_shortener(url):
    """Return (True, reason) for known shortener domains, else (False, None).

    Matching is case-insensitive and tolerates a leading "www." so that
    "www.bit.ly" is caught as well."""
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    if host in SHORTENERS:
        return True, "URL shortener used"
    return False, None
