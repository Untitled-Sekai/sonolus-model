from pydantic import BaseModel
from typing import Optional, List
from ..ServerOption import ServerForm

class ServerLevelResultInfo(BaseModel):
    submits: Optional[List[ServerForm]] = None