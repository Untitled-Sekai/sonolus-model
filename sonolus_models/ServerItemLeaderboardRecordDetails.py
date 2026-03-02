from pydantic import BaseModel
from .items import ReplayItem
from typing import List

class ServerItemLeaderboardRecordDetails(BaseModel):
    replays: List[ReplayItem] = []