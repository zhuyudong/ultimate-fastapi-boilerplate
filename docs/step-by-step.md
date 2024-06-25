## 一步步构建此项目

### Installing

production dependencies

```sh
pip install alembic asyncio asyncpg asgi-lifespan bcrypt beanie blinker boto3 botocore colorama colorlog croniter cryptography emails fastapi fastapi-cache2 fastapi-limiter fastapi-mail filterpy grpcio gunicorn httpx jsonschema locust loguru matplotlib mimesis minio msgpack mypy mypy-extensions numpy pandas passlib protobuf pydantic pydantic-settings pydash pyjwt pymysql python-decouple pyupgrade pyyaml raven redis requests rich ruff scipy sqlalchemy sqlalchemy-stubs sqlmodel stackprinter starlette structlog tenacity types-protobuf ua-parser user-agents uvicorn -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

poetry add alembic asyncio asyncpg asgi-lifespan bcrypt beanie blinker boto3 botocore colorama colorlog croniter cryptography emails fastapi fastapi-cache2 fastapi-limiter fastapi-mail filterpy grpcio gunicorn httpx jsonschema locust loguru matplotlib mimesis minio msgpack mypy mypy-extensions numpy pandas passlib protobuf pydantic pydantic-settings pydash pyjwt pymysql python-decouple pyupgrade pyyaml raven redis requests rich ruff scipy sqlalchemy sqlalchemy-stubs sqlmodel stackprinter starlette structlog tenacity types-protobuf ua-parser user-agents uvicorn
```

development dependencies

```sh
pip install add-trailing-comma autoflake black flake8 isort mypy mypy-extensions pip-upgrader pre-commit pytest pytest-asyncio pyupgrade ruff -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

poetry add add-trailing-comma autoflake black flake8 isort mypy mypy-extensions pip-upgrader pre-commit pytest pytest-asyncio pyupgrade ruff --group dev
```

写入 requirements.txt

```sh
pip freeze | grep -v 'add-trailing-comma\|autoflake\|black\|flake8\|isort\|mypy mypy-extensions\|pip-upgrader\|pre-commit\|pytest\|pytest-asyncio\|pyupgrade\|ruff' > requirements/base.txt

pip freeze | grep -E "add-trailing-comma|autoflake|black|flake8|isort|mypy|mypy-extensions|pip-upgrader|pre-commit|pytest|pytest-asyncio|pyupgrade|ruff" > requirements/dev.txt
```

### Intialize

```sh
pre-commit install
# or
pre-commit install --allow-missing-config
```