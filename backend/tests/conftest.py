import os

import pytest

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["ENV"] = "test"


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    from pehchana import config, db
    from pehchana.main import create_app

    config.get_settings.cache_clear()
    db.get_engine.cache_clear()
    db.get_sessionmaker.cache_clear()
    db.create_all()
    with TestClient(create_app()) as c:
        yield c
