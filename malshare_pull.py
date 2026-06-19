import requests

api_key = "YOUR_API_KEY"

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

def download_sample(sha1):
    print("[+] Downloading:", sha1)

    r = requests.post(
        "https://malshare.com/pull.php",
        data={"api_key": api_key, "hash": sha1},
        proxies=proxies
    )

    with open(sha1, "wb") as f:
        f.write(r.content)

def grab_hashes():
    r = requests.get(
        "https://malshare.com/daily/malshare.current.sha1.txt",
        proxies=proxies
    )

    return [h.strip() for h in r.text.splitlines() if h.strip()]

def main():
    hashes = grab_hashes()

    for h in hashes:
        download_sample(h)

if __name__ == "__main__":
    main()
