"""
RUN THIS WITH:
  PYTHONPATH=. python -m src
  PYTHONPATH=. MONGODB_HOST=localhost MONGODB_PORT=27017 python -m src
"""

import asyncio  # noqa: F401
import os  # noqa: F401
import sys
from pathlib import Path

SRC_PATH = f"{Path(__file__).resolve().parent.parent}/src"
sys.path.append(SRC_PATH)


import uvicorn  # noqa: E402

from src.app.common.console import console  # noqa: F401, E402
from src.app.core.config import settings  # noqa: E402
from src.app.core.logging_config import log_config  # noqa: E402


def run_dev_server() -> None:
    uvicorn.run(
        "src.app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        use_colors=True,
        log_level="info",
        # log_config=os.path.join(SRC_PATH, "app/core/logging_config.yaml"),
        log_config=log_config,
        reload_dirs=[SRC_PATH],
    )


# https://www.uvicorn.org/#running-programmatically
async def run_dev_server_async() -> None:
    config = uvicorn.Config(
        app="src.app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        use_colors=True,
        reload=settings.DEBUG,
        reload_dirs=[SRC_PATH],
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    """Use this for debugging purposes only"""
    run_dev_server()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_dev_server_async())
# # loop.run_forever()
