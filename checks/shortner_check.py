#shortner check 

def check_shortener(url):
    from urllib.parse import urlparse
    shorteners = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd", "ow.ly", "buff.ly", "adf.ly", "cutt.ly", "rebrand.ly"]
    parser = urlparse(url)

    if parser.netloc in shorteners:
        return True, "URL shortener used"
    return False, None