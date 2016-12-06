#!/usr/bin/python3

import asyncio
import aiohttp

async def ping(url):
    resp = await aiohttp.request('GET', url)
    print(url, resp.status)
    resp.close()

urls = [
    "https://httpbin.org/delay/2",
    "https://nuveo.com.br",
    "https://google.com",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/201",
]

loop = asyncio.get_event_loop()
todo = [ping(url) for url in urls]
wait_coro = asyncio.wait(todo)
res, _ = loop.run_until_complete(wait_coro)
loop.close()
