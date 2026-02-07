from pydantic import BaseModel
from typing import Optional, List
from ..common import Tag

class UserItem(BaseModel):
    """UserItemはユーザーの情報を提供"""
    name: str
    source: Optional[str] = None
    title: str
    handle: Optional[str] = None
    tags: List[Tag] = []