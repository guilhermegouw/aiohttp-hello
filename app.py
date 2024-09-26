import asyncio
import json

from aiohttp import web


async def handle_get(request):
    data = {"message": "Hello from server"}
    return web.json_response(data, status=200)


async def handle_post(request):
    data = await request.json()
    name = data.get("name")
    return web.Response(text=f"Hello {name}!")


app = web.Application()
app.router.add_get("/", handle_get)
app.router.add_post("/data", handle_post)

web.run_app(app, port=8080)
