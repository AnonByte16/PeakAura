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

def search_duckduckgo(site, name):
    print(f"\n[+] Searching {site} for: {name}")
    query = f'site:{site} "{name}"'
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    results = soup.find_all('a', attrs={'class': 'result__a'})
    if not results:
        print("[!] No results found.")
        return

    for r in results[:10]:
        print("→", r['href'])

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
        search_duckduckgo("instagram.com", name)
    elif choice == "2":
        search_duckduckgo("facebook.com", name)
    elif choice == "3":
        search_internet(name)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
