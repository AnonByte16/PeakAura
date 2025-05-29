import argparse
import requests
import json
import time
import os

def banner():
    os.system("clear")
    print(r"""
██████╗ ███████╗ █████╗ ██╗  ██╗ █████╗ ██╗   ██╗██████╗  █████╗ ██████╗  █████╗ 
██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║  ██║█████╗  ███████║███████║███████║██║   ██║██████╔╝███████║██████╔╝███████║
██║  ██║██╔══╝  ██╔══██║██╔══██║██╔══██║██║   ██║██╔═══╝ ██╔══██║██╔═══╝ ██╔══██║
██████╔╝███████╗██║  ██║██║  ██║██║  ██║╚██████╔╝██║     ██║  ██║██║     ██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝

                🔎 PeakAura - OSINT Username & Info Scanner
                        Coded by YOU | Termux Ready
""")

def check_username(username):
    with open('platforms.json', 'r') as f:
        platforms = json.load(f)

    print(f"\n🔍 Searching for username: {username}\n")
    for site in platforms:
        url = site['url'].replace("{username}", username)
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"[✔] {site['name']}: Found → {url}")
            elif r.status_code == 404:
                print(f"[✘] {site['name']}: Not found")
            else:
                print(f"[?] {site['name']}: Status {r.status_code}")
        except requests.RequestException:
            print(f"[!] {site['name']}: Error connecting")

def check_email(email):
    print(f"\n🔍 Searching email: {email}")
    print("[ℹ] For full results, use APIs like hunter.io or emailrep.io")
    time.sleep(1)
    print(f"[✔] Simulated scan complete: No public data found for {email}")

def check_phone(phone):
    print(f"\n🔍 Searching phone: {phone}")
    print("[ℹ] For deep lookup, use APIs like NumVerify or Truecaller")
    time.sleep(1)
    print(f"[✘] Simulated check: No public record for {phone}")

def main():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Scan username across platforms")
    parser.add_argument("-e", "--email", help="Scan for email breach info")
    parser.add_argument("-p", "--phone", help="Scan public info for phone")
    args = parser.parse_args()

    if args.username:
        check_username(args.username)
    if args.email:
        check_email(args.email)
    if args.phone:
        check_phone(args.phone)

    if not any([args.username, args.email, args.phone]):
        parser.print_help()

if __name__ == "__main__":
    main()
