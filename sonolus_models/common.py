from pydantic import BaseModel, Field
from typing import Optional, Union, TypeVar, Generic, Annotated, Literal
from .text import SonolusText
from .icon import SonolusIcon

Text = Union[SonolusText, str]
Icon = Union[SonolusIcon, str]


class Tag(BaseModel):
    """タグ情報を提供
    type Tag = {
        title?: Text | (string & {})
        icon?: Icon | (string & {})
    }
    """
    title: Optional[Text] = None
    icon: Optional[Icon] = None


class Sil(BaseModel):
    """Sonolus Item Locator
    type Sil = { address: string, name: string }
    """
    address: str
    name: str


# AutoExit型
AutoExit = Literal['off', 'pass', 'fullCombo', 'allPerfect']


class GameplayResult(BaseModel):
    """ゲームプレイ結果
    type GameplayResult = {
        grade: 'allPerfect' | 'fullCombo' | 'pass' | 'fail'
        arcadeScore: number
        accuracyScore: number
        combo: number
        perfect: number
        great: number
        good: number
        miss: number
        totalCount: number
    }
    """
    grade: Literal['allPerfect', 'fullCombo', 'pass', 'fail']
    arcadeScore: float
    accuracyScore: float
    combo: int
    perfect: int
    great: int
    good: int
    miss: int
    totalCount: int

T = TypeVar('T')

class UseItemDefault(BaseModel):
    """デフォルトアイテムを使用"""
    useDefault: bool = True

class UseItemCustom(BaseModel, Generic[T]):
    """カスタムアイテムを使用"""
    useDefault: bool = False
    item: T

def UseItem(item_type: T) -> Union[UseItemDefault, UseItemCustom[T]]:
    """UseItem型のファクトリー関数"""
    return Union[UseItemDefault, UseItemCustom[item_type]]
