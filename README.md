<div align="center">
  <h1>BugTracker_'s Python Recon Toolkit </h1>
  <p>A fast, modular reconnaissance CLI to quickly map out external attack surfaces.</p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
</div>

---

## Overview
This **Python Recon Toolkit** is a lightweight, zero-bloat command-line interface designed to rapidly evaluate targets during initial reconnaissance phases. Built on an entirely modular architecture, it leverages raw sockets, custom DNS resolvers, and rich terminal formatting to execute deep infrastructure scans without explicitly relying on heavy, bloated internet frameworks.

## Features
* **Subdomain Enumeration** ([subs](cci:1://file:///c:/Users/Kinan/Downloads/ReconToolkit/main.py:13:0-17:27)): Brute-forces 100+ standard subdomains using robust, fallback Cloudflare/Google DNS resolvers to bypass local network configuration drops.
* **Header Analysis** ([headers](cci:1://file:///c:/Users/Kinan/Downloads/ReconToolkit/main.py:19:0-23:25)): Interrogates server HTTP responses and actively flags any missing modern security implementations (HSTS, CSP, X-Frame-Options, etc.).
* **Whois Lookups** ([who](cci:1://file:///c:/Users/Kinan/Downloads/ReconToolkit/main.py:25:0-29:21)): Queries raw TCP socket registries directly (bypassing heavy `pip` modules) to map domain administrative blocks.
* **Active Port Scanning** ([scan](cci:1://file:///c:/Users/Kinan/Downloads/ReconToolkit/main.py:31:0-35:18)): Aggressively scans open host boundaries to identify listening TCP sockets and heuristically predicts underlying application services (HTTP, HTTPS, SSH, MySQL, etc.).

## Requirements
This toolkit uses modern Python formatting via the `rich` library to structure clean, aesthetic terminal outputs.

```txt
click==8.1.7
colorama==0.4.6
dnspython==2.6.1
requests==2.31.0
rich==13.7.1
