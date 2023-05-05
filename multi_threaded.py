The code I provided in the previous example is using multi-threaded synchronous programming 
with the `concurrent.futures` module. 
Here's an example of how to convert that code into multi-threaded asynchronous programming using `asyncio` module in Python:

```
import asyncio
import aiohttp
import time

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.read()
        print(f"Downloaded {len(content)} bytes from {url}")

async def main():
    urls = [
        "https://www.python.org/",
        "https://www.google.com/",
        "https://www.github.com/",
        "https://www.stackoverflow.com/",
    ]

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(download_url(session, url)))
        await asyncio.gather(*tasks)

    end_time = time.time()

    print(f"Total time: {end_time - start_time}")

asyncio.run(main())
```

In this example, we define an `async` function `download_url` that downloads the content of a given URL using the `aiohttp` library. 
We then define an `async` function `main` that creates a list of URLs to download and 
uses the `async with` statement to create an `aiohttp.ClientSession` object, which manages the HTTP connections.

We then create a list of `asyncio.Task` objects by calling `asyncio.ensure_future` for each URL and add them to a list of tasks. 
We then call `asyncio.gather` to execute all the tasks concurrently and wait for them to complete.

Finally, we calculate and print the total time taken to download the URLs. 
The `asyncio.run` function is used to run the `main` function, which executes the coroutine and runs the event loop.
