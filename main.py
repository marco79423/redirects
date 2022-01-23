import pathlib
from urllib.parse import urlparse

import fastapi
import uvicorn
from fastapi.responses import RedirectResponse
from omegaconf import OmegaConf

CONFIG_PATH = pathlib.Path('./conf.d/redirects.yml')

app = fastapi.FastAPI()
config = OmegaConf.load(CONFIG_PATH)

for redirect_config in config:
    o = urlparse(redirect_config.source)

    @app.get(o.path)
    async def redirect():
        return RedirectResponse(redirect_config.target)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
