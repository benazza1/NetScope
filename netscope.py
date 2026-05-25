import random
import time
import sys
import os

# colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# counters
dns_count = 0
http_count = 0
tcp_count = 0

# fake data
fake_domains = [
    "google.com",
    "cloudflare.com",
    "github.com",
    "openai.com",
    "youtube.com"
]

fake_protocols = ["DNS", "HTTP", "TCP"]

fake_ips = [
    "8.8.8.8",
    "1.1.1.1",
    "142.250.190.78",
    "172.217.16.142"
]

# banner
banner = f"""
{CYAN}
🔥 NETSCOPE PRO v1.2
Simple Network Analyzer Simulator
{RESET}
"""

def help_menu():
    print(f"""
{GREEN}Usage:{RESET}
  python3 netscope.py           Run analysis
  python3 netscope.py live      Live mode (slower output)
  python3 netscope.py DNS       Filter DNS only
  python3 netscope.py HTTP      Filter HTTP only
  python3 netscope.py TCP       Filter TCP only
  python3 netscope.py --help    Help menu
""")

# help
if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print(banner)
    help_menu()
    sys.exit()

print(banner)

# mode detection
live_mode = False
filter_proto = None

if len(sys.argv) > 1:
    arg = sys.argv[1].upper()

    if arg == "LIVE":
        live_mode = True
    else:
        filter_proto = arg

# generate fake packets
packets = []

for _ in range(10):
    src = "192.168.1.10"
    dst = random.choice(fake_ips)
    proto = random.choice(fake_protocols)
    data = random.choice(fake_domains)

    packets.append(f"{src} -> {dst} | {proto} | {data}")

# analysis
print("=" * 60)

for i, p in enumerate(packets, start=1):

    src, rest = p.split(" -> ")
    dst, proto, data = rest.split(" | ")

    if filter_proto and proto.upper() != filter_proto:
        continue

    if proto == "DNS":
        dns_count += 1
        color = CYAN
    elif proto == "HTTP":
        http_count += 1
        color = GREEN
    else:
        tcp_count += 1
        color = YELLOW

    print(f"{color}[{i}] PACKET{RESET}")
    print(f"SRC   : {src}")
    print(f"DST   : {dst}")
    print(f"PROTO : {proto}")
    print(f"DATA  : {data}")
    print("-" * 50)

    time.sleep(1 if live_mode else 0.3)

# summary
print(f"\n{CYAN}📊 SUMMARY{RESET}")
print(f"DNS  : {dns_count}")
print(f"HTTP : {http_count}")
print(f"TCP  : {tcp_count}")

print(f"\n{GREEN}✔ Analysis Complete 🚀{RESET}")
