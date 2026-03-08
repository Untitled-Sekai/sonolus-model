from pydantic import BaseModel, Field
from typing import Literal, List


class SonolusSignaturePublicKey(BaseModel):
    """Sonolus署名検証用の公開鍵（JWK形式）
    
    ECDSA-SHA256で署名されたメッセージの検証に使用される公開鍵です。
    JSON Web Key (RFC 7517) 形式で提供されます。
    """
    key_ops: List[Literal["verify"]] = Field(default=["verify"], description="キー操作：検証のみ")
    ext: bool = Field(default=True, description="鍵の外部利用可能性")
    kty: Literal["EC"] = Field(default="EC", description="鍵の種類：楕円曲線")
    x: str = Field(description="X座標（Base64URL形式）")
    y: str = Field(description="Y座標（Base64URL形式）")
    crv: Literal["P-256"] = Field(default="P-256", description="楕円曲線：P-256")
