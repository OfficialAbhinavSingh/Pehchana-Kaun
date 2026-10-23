"""Shared FastAPI dependencies."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from pehchana.arms import Arm, load_arms
from pehchana.config import Settings, arm_env, get_settings
from pehchana.db import get_session

SessionDep = Annotated[Session, Depends(get_session)]
SettingsDep = Annotated[Settings, Depends(get_settings)]


def get_arms(settings: SettingsDep) -> list[Arm]:
    return load_arms(settings.arms_file, arm_env())


ArmsDep = Annotated[list[Arm], Depends(get_arms)]
