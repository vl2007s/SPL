"""PhishLens core: run the registered checks against a URL and combine their
weighted findings into a single risk assessment."""

from spl_scoring.spl import SPL
from checks.https_check import check_https
from checks.shortener_check import check_shortener

# Weight of each check in the final score — tune here, nothing else changes.
WEIGHTS = {
    "https": 10,
    "shortener": 20,
}

# Registry of checks: (name, callable(url) -> (found: bool, reason: str | None))
CHECKS = [
    ("https", check_https),
    ("shortener", check_shortener),
]


def calculate_risk(url):
    """Run all checks on `url`; return (score, reasons, danger_level)."""
    spl = SPL()
    for name, check_func in CHECKS:
        found, reason = check_func(url)
        if found:
            spl.add(WEIGHTS[name], reason)
    return spl.score, spl.reasons, spl.get_danger_level()
