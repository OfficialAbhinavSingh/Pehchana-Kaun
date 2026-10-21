"""Shared FastAPI dependencies."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from pehchana.db import get_session

SessionDep = Annotated[Session, Depends(get_session)]
