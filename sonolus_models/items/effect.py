from pydantic import BaseModel
from typing import Optional, List
from ..base import SonolusResourceLocator
from ..common import Tag
from ..items import BaseItem, PackBaseItem
from ..items import LocalationText
from .user import UserItem

SRL = SonolusResourceLocator

class EffectItem(BaseItem):
    """EffectItemはエフェクトの情報を提供"""
    version: int = 5
    subtitle: str
    authorUser: Optional[UserItem] = None
    thumbnail: SRL
    data: SRL
    audio: SRL

class EffectPackItem(PackBaseItem):
    """EffectPackItemはパック内のエフェクトの情報を提供"""
    version: int = 5
    subtitle: LocalationText
    thumbnail: SRL
    data: SRL
    audio: SRL