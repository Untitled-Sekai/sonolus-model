from pydantic import BaseModel
from typing import Optional
from ..ServerOption import ServerForm

class ServerLevelResultInfo(BaseModel):
    submits: Optional[ServerForm] = None