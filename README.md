# 顔認識システム（リアルタイム・複数人対応）

このプロジェクトは、研究室のB4企画において「顔認証」を使う必要があり、  
その一環として開発された **Pythonベースのリアルタイム顔認証システム**です。

---

## 🎯 プロジェクトの目的

- カメラ映像から **複数人の顔をリアルタイム認識**すること
- 認識された人物に応じて「名前」または「Unknown」を表示
- 類似度（顔距離）を表示することで精度調整や可視化を行う
- 今後、出席管理やセキュリティ用途への拡張を目指す

---

## 🧠 主な特徴

- ✅ **複数人対応（1:N顔認識）**
- ✅ PCのWebカメラからのリアルタイム映像処理
- ✅ 顔を枠で囲み、名前 or Unknownを表示
- ✅ 類似度（face distance）を表示して判定根拠を明示
- ✅ 顔画像はフォルダ単位で簡単に登録可能

---

## 🚀 実行方法

```bash
# 顔のエンコード（初回のみ）
python encode_faces.py

# リアルタイム顔認識の実行
python test_multi_realtime.py
```

---

## 🗂️ ディレクトリ構成

face_recognition/  
├── 0527env                   # 仮想環境の情報  
├── face_dataset/              # 登録画像（人物名ごとにサブフォルダ）  
│   ├── taiyo/  
│   │   ├── taiyo1.jpg  
│   │   └── taiyo2.jpg  
│   └── obama/  
│       ├── obama1.jpg  
│       └── obama2.jpg  
├── test.py                   # 静止画での顔認証  
├── test_realtime.py          # webカメラを用いた顔認証（ただし、一人のみ）  
├── encode_faces.py           # 顔エンコードスクリプト（最初に実行）  
├── test_multi_realtime.py    # リアルタイム顔認識スクリプト（1:N）  
├── known_faces.pkl           # エンコード済みの顔データ（自動生成）  
├── requirements.txt          # 必要ライブラリ一覧  
└── README.md                 # このファイル  

---

## 🧪 使用ライブラリ（仮想環境：0527env）

以下のライブラリを使用しています。requirements.txt に記載済み。  

opencv-python  
face_recognition  
dlib  
numpy  
matplotlib  

- インストール方法：

```bash
pip install -r requirements.txt
```

---

## 💻 動作環境

| 項目     | 内容                       |
| ------ | ------------------------ |
| OS     | macOS (Apple Silicon 含む) |
| Python | 3.9.x など（推奨）             |
| 仮想環境名  | `0527env`                |
| 実行方式   | VS Code         |
| カメラ    | 内蔵 / 外部Webカメラ            |

