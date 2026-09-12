"""PhishLens CLI: analyze one URL and print its risk score, level and reasons.

Run from the repo root:
    python UI/cli.py "https://example.com/some-link"
"""

import sys
import os

# Allow running as `python UI/cli.py` from the repo root: make the project
# root importable so `core` resolves regardless of the current directory.
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import argparse
from core import calculate_risk


def main():
    parser = argparse.ArgumentParser(description="Calculate the risk score of a URL.")
    parser.add_argument("url", type=str, help="The URL to analyze.")
    args = parser.parse_args()

    url = args.url
    score, reasons, danger_level = calculate_risk(url)

    print(f"URL: {url}")
    print(f"Risk Score: {score}")
    print(f"Danger Level: {danger_level}")
    if reasons:
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")


if __name__ == "__main__":
    main()
