"""HTTPS heuristic: links without TLS are easier to intercept or spoof.

This is one signal, not proof of phishing — the reason string is phrased to
reflect that for the user."""

from urllib.parse import urlparse


def check_https(url):
    """Return (True, reason) when the URL does not use https, else (False, None)."""
    parser = urlparse(url)

    if parser.scheme != "https":
        return True, "No HTTPS in link"

    return False, None
