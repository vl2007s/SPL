from spl_scoring.spl import SPL
from checks.https_check import check_https
from checks.shortner_check import check_shortener

weight = {
    "https": 10,
    "shortener": 20
}

checks = [
    ("https", check_https),
    ("shortener", check_shortener)
]

def calculate_risk(url):
    spl = SPL()
    for name, check_func in checks:
        result, reason = check_func(url)
        if result:
            spl.add(weight[name], reason)
    return spl.score, spl.reasons, spl.get_danger_level()

