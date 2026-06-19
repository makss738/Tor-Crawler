import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

url = input("Enter URL (normal ou onion): ").strip()

try:
    r = requests.get(url, proxies=proxies, timeout=30)
    print("\n[+] STATUS:", r.status_code)
    print("\n[+] CONTENT PREVIEW:\n")
    print(r.text[:1000])
except Exception as e:
    print("[ERROR]", e)
