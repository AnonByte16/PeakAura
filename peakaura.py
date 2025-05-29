import requests
import json
import argparse

def load_platforms(file='platforms.json'):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading platforms.json: {e}")
        return {}

def check_username(username, platforms):
    print(f"\n[+] Searching username '{username}' on platforms:")
    for platform in platforms:
        url = platforms[platform].replace("{username}", username)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[FOUND] {platform}: {url}")
            else:
                print(f"[NOT FOUND] {platform}")
        except Exception as e:
            print(f"[ERROR] {platform}: {e}")

def check_email(email):
    print(f"\n[+] Checking breaches for email: {email}")
    # Placeholder for real API integration
    print("[Info] Email lookup feature coming soon.")

def check_phone(phone):
    print(f"\n[+] Checking phone number: {phone}")
    # Placeholder for real API integration
    print("[Info] Phone lookup feature coming soon.")

def main():
    parser = argparse.ArgumentParser(description="PeakAura - Simple OSINT tool")
    parser.add_argument('-u', '--username', help='Username to search on platforms')
    parser.add_argument('-e', '--email', help='Email to check breaches')
    parser.add_argument('-p', '--phone', help='Phone number to lookup')

    args = parser.parse_args()

    platforms = load_platforms()

    if args.username:
        check_username(args.username, platforms)

    if args.email:
        check_email(args.email)

    if args.phone:
        check_phone(args.phone)

    if not any([args.username, args.email, args.phone]):
        parser.print_help()

if __name__ == "__main__":
    main()
