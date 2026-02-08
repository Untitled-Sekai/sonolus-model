from pydantic import BaseModel
from typing import Optional, List, Union, Any, TypeVar, Generic, Literal
from ..base import SonolusResourceLocator
from ..common import Tag
from ..items import BaseItem, PackBaseItem, LocalationText
from ..items.engine import EngineItem
from .user import UserItem
from ..items.skin import SkinItem
from ..items.background import BackgroundItem
from ..items.effect import EffectItem
from ..items.particle import ParticleItem

SRL = SonolusResourceLocator

T = TypeVar('T')


class UseItemDefault(BaseModel):
    """デフォルトアイテムを使用"""
    useDefault: Literal[True]


class UseItemCustom(BaseModel, Generic[T]):
    """カスタムアイテムを使用"""
    useDefault: Literal[False]
    item: T

class LevelItem(BaseItem):
    """LevelItemはレベルの情報を提供"""
    version: int = 1
    rating: float
    artists: str
    engine: EngineItem
    authorUser: Optional[UserItem] = None
    useSkin: Union[UseItemDefault, UseItemCustom[SkinItem]]
    useBackground: Union[UseItemDefault, UseItemCustom[BackgroundItem]]
    useEffect: Union[UseItemDefault, UseItemCustom[EffectItem]]
    useParticle: Union[UseItemDefault, UseItemCustom[ParticleItem]]
    cover: SRL
    bgm: SRL
    preview: Optional[SRL] = None
    data: SRL

class LevelPackItem(PackBaseItem):
    """LevelPackItemはパック内のレベルの情報を提供"""
    version: int = 1
    rating: float
    artists: LocalationText
    engine: str  # engine name
    useSkin: Union[UseItemDefault, UseItemCustom[SkinItem]]
    useBackground: Union[UseItemDefault, UseItemCustom[BackgroundItem]]
    useEffect: Union[UseItemDefault, UseItemCustom[EffectItem]]
    useParticle: Union[UseItemDefault, UseItemCustom[ParticleItem]]
    cover: SRL
    bgm: SRL
    preview: Optional[SRL] = None
    data: SRL
