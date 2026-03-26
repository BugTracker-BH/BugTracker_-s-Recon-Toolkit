[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Python Recon Toolkit

A powerful, modular reconnaissance command-line interface designed to quickly evaluate targets and enumerate attack surfaces. This toolkit leverages precise terminal outputs to perform deep scans on remote architectures.

## Features
- **Subdomain Enumeration**: Brute-force over 100+ standard subdomains to discover hidden infrastructure components.
- **Header Analysis**: Interrogate server headers and instantly flag missing strict security implementations (HSTS, CSP, etc.).
- **Whois Lookups**: Query raw data from internet registries to map domains back to their administrative blocks.
- **Port Scanning**: Identify listening tcp sockets across the host boundary and guess their underlying services.
- **Rich Terminal Output**: Renders data across beautifully responsive tables and panels.

## Requirements
```txt
requests
dnspython
colorama
click
rich
```

## Installation
```bash
git clone https://github.com/your-username/recon-toolkit.git
cd recon-toolkit
pip install -r requirements.txt
```

## Usage

### Subdomain Enumeration
```bash
python main.py subs google.com
```

### Security Header Analysis
```bash
python main.py headers https://github.com
```

### WHOIS Deep Query
```bash
python main.py who example.com
```

### Active Port Scanning
```bash
python main.py scan 192.168.1.1
```