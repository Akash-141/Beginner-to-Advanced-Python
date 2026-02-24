# Day 21 Examples: pip usage in Python

# NOTE:
# These examples assume you installed 'requests' using:
# pip install requests

# ---------- Example: Using an external package ----------
import requests

response = requests.get("https://api.github.com")

print("Status code:", response.status_code)
print("Content type:", response.headers.get("content-type"))


# ---------- Example: Simple helper function ----------
def check_website(url):
    try:
        r = requests.get(url, timeout=5)
        return f"{url} is UP (status {r.status_code})"
    except requests.RequestException:
        return f"{url} is DOWN"

print(check_website("https://www.python.org"))
