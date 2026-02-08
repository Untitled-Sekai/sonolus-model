from pydantic import BaseModel
from typing import Optional, List, Any
from ..base import SonolusResourceLocator
from ..common import Tag
from ..items import BaseItem, PackBaseItem, LocalationText
from .level import LevelItem
from .user import UserItem

SRL = SonolusResourceLocator

class PlaylistItem(BaseItem):
    """PlaylistItemはプレイリストの情報を提供"""
    version: int = 1
    subtitle: str
    authorUser: Optional[UserItem] = None
    levels: List[LevelItem] = []
    thumbnail: Optional[SRL] = None

class PlaylistPackItem(PackBaseItem):
    """PlaylistPackItemはパック内のプレイリストの情報を提供"""
    version: int = 1
    subtitle: LocalationText
    levels: List[str] = []  # level names
    thumbnail: Optional[SRL] = None
