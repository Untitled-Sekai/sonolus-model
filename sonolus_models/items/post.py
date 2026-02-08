from pydantic import BaseModel, Field
from typing import Optional, List
from ..base import SonolusResourceLocator
from ..common import Tag
from ..items import BaseItem, PackBaseItem
from .user import UserItem

SRL = SonolusResourceLocator

class PostItem(BaseItem):
    """PostItemはポストの情報を提供"""
    version: int = 1
    authorUser: Optional[UserItem] = None
    time: int = Field(default_factory=lambda: 0)  # タイムスタンプ（デフォルト値0）
    thumbnail: Optional[SRL] = None

class PostPackItem(PackBaseItem):
    """PostPackItemはパック内のポストの情報を提供"""
    version: int = 1
    time: int
    thumbnail: Optional[SRL] = None
