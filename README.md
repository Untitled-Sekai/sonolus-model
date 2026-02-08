# Sonolus-Models

Pythonで実装されたSonolusサーバーのPydanticモデルライブラリ。
sonolus-core (TypeScript)の型定義から移行された完全な型安全性を提供します。

## インストール

```bash
pip install sonolus-models
```

## 主な機能

### 完全な型定義
- **共通型**: `Tag`, `Srl`, `Sil`, `AutoExit`, `GameplayResult`
- **アイテム型**: `LevelItem`, `SkinItem`, `BackgroundItem`, `EffectItem`, `ParticleItem`, `EngineItem`, `PostItem`, `PlaylistItem`, `ReplayItem`, `RoomItem`, `UserItem`
- **サーバー型**: `ServerInfo`, `ServerInfoButton` (3種類のUnion型)
- **オプション型**: 9種類の`ServerOption` (text, textArea, slider, toggle, select, multi, serverItem, serverItems, collectionItem, file)

### TypeScript互換
sonolus-core (TypeScript) の型定義から移行されているため、TypeScriptとの完全な互換性があります。

### Pydantic v2対応
最新のPydantic v2を使用した高速なバリデーション。

## ライセンス

MIT