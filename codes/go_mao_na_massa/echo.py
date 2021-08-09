#!.venv/bin/python
from blacksheep.server import Application
from blacksheep.server.responses import json
import uvicorn


app = Application()


@app.route("/")
async def home(request):
    return json({"apple": 5, "lettuce": 7})


if __name__ == "__main__":
    uvicorn.run(
        "codes.go_mao_na_massa.echo:app",
        host="127.0.0.1",
        port=5000,
        log_level="info",
        workers=4,
    )
