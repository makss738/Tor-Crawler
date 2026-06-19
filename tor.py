import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

print("[+] Testing Tor IP...")

print(
    requests.get("http://icanhazip.com", proxies=proxies).text.strip()
)
