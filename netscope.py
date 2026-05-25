#!/usr/bin/env python3
import sys
import socket
import requests
import time

# =========================
# 🎨 LOGO
# =========================
BANNER = """
███╗   ██╗███████╗████████╗███████╗ ██████╗ ██████╗ ███████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██╔██╗ ██║█████╗     ██║   ███████╗██║   ██║██████╔╝█████╗  
██║╚██╗██║██╔══╝     ██║   ╚════██║██║   ██║██╔═══╝ ██╔══╝  
██║ ╚████║███████╗   ██║   ███████║╚██████╔╝██║     ███████╗
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝

        NetScope v1.0 - Real Network Recon Tool
"""

# =========================
# HELP MENU
# =========================
def help_menu():
    print("""
Usage:
  python3 netscope.py dns <domain>     Resolve DNS
  python3 netscope.py http <url>       Get HTTP headers
  python3 netscope.py scan <ip>        Port scanning
  python3 netscope.py live <domain>    Live monitoring
  python3 netscope.py --help          Help menu
""")

# =========================
# DNS
# =========================
def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[DNS] {domain} -> {ip}")
    except Exception as e:
        print(f"[ERROR DNS] {e}")

# =========================
# HTTP HEADERS
# =========================
def http_headers(url):
    try:
        r = requests.get(url)
        print("\n[HTTP HEADERS]")
        for k, v in r.headers.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"[ERROR HTTP] {e}")

# =========================
# PORT SCANNER
# =========================
def port_scan(ip):
    print(f"\n[SCAN] Scanning {ip} ...")
    ports = [21, 22, 80, 443, 3306, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()

# =========================
# LIVE MODE
# =========================
def live_mode(domain):
    print(f"\n[LIVE MODE] Monitoring {domain}...\n")
    for i in range(5):
        try:
            ip = socket.gethostbyname(domain)
            print(f"[{i+1}] {domain} -> {ip}")
        except:
            print("Error resolving domain")
        time.sleep(1)

# =========================
# MAIN
# =========================
def main():
    print(BANNER)

    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        help_menu()
        return

    cmd = sys.argv[1].lower()

    if cmd == "dns":
        dns_lookup(sys.argv[2])

    elif cmd == "http":
        http_headers(sys.argv[2])

    elif cmd == "scan":
        port_scan(sys.argv[2])

    elif cmd == "live":
        live_mode(sys.argv[2])

    else:
        print("Unknown command. Use --help")

if __name__ == "__main__":
    main()
