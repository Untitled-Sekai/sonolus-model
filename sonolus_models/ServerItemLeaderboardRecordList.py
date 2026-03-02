from pydantic import BaseModel
from .ServerItemLeaderboardRecord import ServerItemLeaderboardRecord
from typing import List, Optional

class ServerItemLeaderboardRecordList(BaseModel):
    pageCount: int
    cursor: Optional[str] = None
    records: List[ServerItemLeaderboardRecord] = []