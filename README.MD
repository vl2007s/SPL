# 🛡️ PhishLens

> An intelligent link analyzer for detecting potential phishing.

[![Status](https://img.shields.io/badge/status-in%20development-orange)](#)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## About the Project

**PhishLens** helps quickly assess the safety of a URL before visiting it. The tool analyzes the link structure and identifies signs commonly found in phishing attacks: suspicious domains, character substitution, redirects, and unusual parameters.

The project is intended for developers, information security specialists, and anyone who wants to check links safely.

> ⚠️ The analysis result is a recommendation, not a guarantee of safety. Do not open suspicious links or enter confidential information on unknown websites.

## Features

- 🔎 Convenient URL checking
- 🧩 Analysis of domains, subdomains, paths, and parameters
- 🎭 Detection of suspicious characters and lookalike domains
- 🔀 Detection of potential redirects
- 📊 Clear risk-level assessment
- 💬 Clear explanations of detected indicators
- ⚡ Fast local analysis without opening the link

## How It Works

1. The user provides a URL to the analyzer.
2. The system normalizes the link and extracts its components.
3. A set of rules checks for common phishing indicators.
4. A risk assessment and list of detected factors are generated.

## Usage

No dependencies — only Python 3.8+.

```bash
git clone https://github.com/vl2007s/SPL.git
cd SPL
python UI/cli.py "http://bit.ly/abc"
```

Example output:

```text
URL: http://bit.ly/abc
Risk Score: 30
Danger Level: Low
Reasons:
- No HTTPS in link
- URL shortener used
```

Each check lives in `checks/` and is registered with a weight in `core.py` — add a new rule by writing a `check(url) -> (found, reason)` function and adding one line to `CHECKS`.

## Security Recommendations

- Do not visit a link just to check it.
- Do not send URLs containing private tokens or personal data to the analyzer.
- Always verify the domain manually, especially if the link arrived by email or messenger.
- Use HTTPS and keep the analysis rules updated.

## Roadmap

- [ ] Web interface for checking links
- [x] Command-line interface (CLI)
- [ ] Domain reputation checks through external sources
- [ ] QR code analysis
- [ ] Report export
- [ ] Test URL set for evaluating detection quality

## Contributing

Ideas and pull requests are welcome. Before submitting changes, describe the problem they solve and add tests for new analysis rules.

## License

This project is distributed under the [MIT](LICENSE) license.
