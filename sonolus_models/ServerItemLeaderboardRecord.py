from pydantic import BaseModel
from typing import Optional
from .items import UserItem

class ServerItemLeaderboardRecord(BaseModel):
    name: str
    rank: str
    player: str
    playerUser: Optional[UserItem]
    value: str