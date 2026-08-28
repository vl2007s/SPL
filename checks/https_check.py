from urllib.parse import urlparse #import python lib to work with url parsing

def check_https(url): 
    parser = urlparse(url)

    #if not https 
    if parser.scheme != "https":
        return True, "No HTTPS in link" # return status, reasons and weight
    
    return False, None