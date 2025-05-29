import requests

platforms = {
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
}

def check_username(username):
    print(f"\nChecking username: {username}\n")
    for name, url in platforms.items():
        full_url = url.format(username)
        try:
            res = requests.get(full_url)
            if res.status_code == 200:
                print(f"[+] Found on {name}: {full_url}")
            else:
                print(f"[-] Not on {name}")
        except:
            print(f"[!] Error checking {name}")

if __name__ == "__main__":
    name = input("Enter name: ").strip().replace(" ", "").lower()
    # Optionally generate variations here
    check_username(name)
