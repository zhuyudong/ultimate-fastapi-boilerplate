# import sys
from pathlib import Path

# from sqlalchemy.orm import Session
# from rich.traceback import install
# HACK: This is a hack to allow the import of the src module, which is: <dir>/ultimate-fastapi-boilerplate/src
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from fastapi import APIRouter, Depends, Request, Response  # noqa: E402,F401
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates  # noqa: E402

from src.app.api.v1.api import api_router  # noqa: E402
from src.app.core.config import settings  # noqa: E402
from src.app.core.logging_config import log_config  # noqa: E402
from src.app.main_app import app  # noqa: E402

# from src.app.api import deps


# install(show_locals=False)
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

root_router = APIRouter()


# @root_router.get("/", status_code=200, summary="Root")
# def root(
#     request: Request,
#     response: Response,
#     # db: Session = Depends(deps.get_postgres),
# ) -> dict:
#     """
#     Root GET
#     """
#     # recipes = services.recipe.get_multi(db=db, limit=10)
#     # return TEMPLATES.TemplateResponse(
#     #     "index.html",
#     #     {"request": request, "recipes": recipes},
#     # )
#     return {"message": "Hello World"}


@root_router.get("/")
async def home():
    return RedirectResponse(url=f"{settings.API_VERSION}/redoc")


@root_router.get("/list-endpoints")
def list_endpoints(request: Request):
    endpoints = [{"name": route.name, "path": route.path} for route in app.routes]
    return endpoints


app.include_router(root_router, tags=["Root"])
app.include_router(api_router, prefix=settings.API_VERSION)

if __name__ == "__main__":
    """Use this for debugging purposes only"""
    import uvicorn

    # Development Mode
    # FIXME: /home/qj00304/anaconda3/envs/src-backend-cloud/lib/python3.11/site-packages/fastapi/openapi/utils.py:207: UserWarning: Duplicate Operation ID root__get for function root at /home/qj00304/Code/pegasus/src_backend_cloud/src/app/main.py
    uvicorn.run(
        "src.app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_config=log_config,
    )
    # Production Mode
    # uvicorn.run(app, host=settings.HOST, port=settings.PORT)
