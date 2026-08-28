from spl_scoring.spl import SPL
from checks.https_check import check_https

weight = {
    "https": 10,
}

checks = [
    ("https", check_https)
]

def calculate_risk(url) 
spl = SPL()