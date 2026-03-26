import click
from utils.logger import setup_logger
from modules.subdomain import enum_subdomains
from modules.headers import fetch_headers
from modules.whois import get_whois
from modules.portscan import scan_ports

log = setup_logger()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('domain')
def subs(domain):
    log.info(f"starting subdomain enum for {domain}")
    enum_subdomains(domain)

@cli.command()
@click.argument('target')
def headers(target):
    log.info("snagging headers")
    fetch_headers(target)

@cli.command()
@click.argument('domain')
def who(domain):
    log.info("pulling whois data")
    get_whois(domain)

@cli.command()
@click.argument('ip')
def scan(ip):
    log.info("scanning ports 1-1000")
    scan_ports(ip)

if __name__ == '__main__':
    cli()
