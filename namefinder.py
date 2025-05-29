import requests
from bs4 import BeautifulSoup
import argparse

def ask_platform():
    print("\nWhere do you want to search?")
    print("1. Instagram")
    print("2. Facebook")
    print("3. Internet")
    choice = input("Enter choice (1/2/3): ")
    return choice

def search_instagram(name):
    print(f"\n[+] Searching Instagram for: {name}")
    query = name.replace(" ", "")
    url = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers).json()
        for user in res["users"][:10]:
            username = user["user"]["username"]
            fullname = user["user"]["full_name"]
            print(f"→ {username} ({fullname})")
    except Exception as e:
        print("[!] Error:", e)

def search_facebook(name):
    print(f"\n[+] Searching Facebook for: {name}")
    query = name.replace(" ", "+")
    url = f"https://www.facebook.com/public?query={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.find_all('a', href=True)
        found = set()

        for a in links:
            href = a['href']
            if "facebook.com" in href and "profile.php" in href:
                found.add(href)
            elif "facebook.com/" in href and not any(x in href for x in ['sharer', 'pages', 'groups']):
                found.add(href)

        for link in list(found)[:10]:
            print("→", link)
    except Exception as e:
        print("[!] Error:", e)

def search_internet(name):
    print(f"\n[+] Doing internet search for: {name}")
    query = name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    print(f"[Info] Open this in browser:\n{url}")

def main():
    parser = argparse.ArgumentParser(description="NameFinder - Find social handles by name")
    parser.add_argument('-n', '--name', required=True, help='Full name to search')
    args = parser.parse_args()

    name = args.name
    choice = ask_platform()

    if choice == "1":
        search_instagram(name)
    elif choice == "2":
        search_facebook(name)
    elif choice == "3":
        search_internet(name)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
