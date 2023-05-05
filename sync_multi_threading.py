import concurrent.futures
import requests
import time

def download_url(url):
    with requests.get(url) as response:
        print(f"Downloaded {len(response.content)} bytes from {url}")

urls = [
    "https://www.python.org/",
    "https://www.google.com/",
    "https://www.github.com/",
    "https://www.stackoverflow.com/",
]

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(download_url, url) for url in urls]

concurrent.futures.wait(futures)

end_time = time.time()

print(f"Total time: {end_time - start_time}")
