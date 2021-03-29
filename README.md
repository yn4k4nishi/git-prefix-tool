# git-prefix-tool

|emoji|prefix|ditail|
|---|---|---|
|:sparkles:       | Feature            | 新機能の実装|
|:+1:             | Update             | 機能の修正|
|:wastebasket:    | Remove             | 削除|
|:bug:            | Fix                | バグの修正|
|:recycle:        | Refactor           | リファクタリング|
|:pencil2:        | Typo               | タイプミスなどの修正|
|:sound:          | Add-logs           | ログの追加|
|:mute:           | Remove-logs        | ログの削除|
|:books:          | Document           | ドキュメントの変更|
|:art:            | Accessibility      | デザインUI/UXの変更|
|:horse:          | Improve-perfomance | パフォーマンスの改善|
|:cop:            | Improve-security   | セキュリティ関連の改善|
|:wrench:         | Tools              | ツール|
|:rotating_light: | Tests              | テスト|
|:construction:   | WIP                | Work In Progress|
|:bookmark:       | Version-tag        | バージョンタグ|
|:tada:           | First              | 初めてのコミット|


## インストール
以下が必要
- python3
- github CLI

github CLIのインストール
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
sudo apt-add-repository -u https://cli.github.com/packages
sudo apt install gh
```

githubにログインしておく
```bash
gh auth login
```

git prefix toolのインストール
```bash
wget -qO - https://raw.githubusercontent.com/yn4k4nishi/git-prefix-tool/main/install.sh | bash
```

## 使い方
bashターミナルで
```bash
git prefix-tool
```
を実行

矢印キーで移動、SPACEで選択し、Enterで次に進む 
```
Select Add Files (pless SPACE Key to check).
    [Select ALL]
  * README.md
    hoge.cpp

Pless Enter to go next
```

テンプレートから選択し、Enterで次に進む
```
Select Prefix List Below.
  Feature            : 新機能の実装
  Update             : 機能の修正
  Remove             : 削除
  Fix                : バグの修正
  Refactor           : リファクタリング
  Typo               : タイプミスなどの修正
  Add-logs           : ログの追加
  Remove-logs        : ログの削除
> Document           : ドキュメントの変更
  Accessibility      : デザインUI/UXの変更
  Improve-perfomance : フォーマンスの改善
  Improve-security   : セキュリティ関連の改善
  Tools              : ツール
  Tests              : テスト
  WIP                : Work In Progress
  Version-tag        : バージョンタグ
  First              : 初めてのコミット
```

bodyを入力し、Enterで次に進む
```
:books: Document
Write Body and Pless Enter.
  README.mdの更新
```

Pushするかを選択する.
何も入力せずにEnterを押すとPushされる
```
Do you push it ? (Y/n) : 
```