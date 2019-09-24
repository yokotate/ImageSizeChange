# Pythonの設定
* Python3以上
* OpenCV

# 内容
* 入力されたフォルダに存在する画像のサイズを変更する。
    * 入力された値で割る
        * コマンドライン引数に１つの数値が渡された場合、その値で縦・横の値を割る
    * 入力された値に変更する
        * コマンドライン引数に２つの数値が渡された場合、その値に縦・横の値を変更する
    * 入力が無い場合には縦幅と横幅を4で割る
* 入力されたフォルダに存在する画像をグレースケールに変更する。

# ファイル構成
* ./ImageSizeChange.py
    * init
        * 初期値設定用
    * main
        * 実行部分
    * FolderForLoop
        * 指定フォルダの中をループして、取得したものをFolderCheckに投げる
    * FolderCheck
        * FolderForLoopから渡されたディレクトリがファイルかフォルダかを判定する
            * フォルダなら出力先に同じフォルダを作成する
            * ファイルならImageToGrayAndSizeChangeに投げる
    * ImageToGrayAndSizeChange
        * FolderCheckから渡されたファイルを変換する
            * サイズの変更
            * 色表現の変更（グレースケール）
            * 明度を上げる

# 実行方法
* ImageSizeChange.py **変換対象のフォルダのPATH** **変換結果の出力先** 横幅　縦幅
* ImageSizeChange.py **変換対象のフォルダのPATH** **変換結果の出力先** 割る値
* ImageSizeChange.py **変換対象のフォルダのPATH** **変換結果の出力先**

# 今後変更したい点
1. 変更サイズを変更できるようにする（対応完了）
    * 現在の割る値からXとYの値を指定できるようにする
2. 指定フォルダの中にあるフォルダの中のファイルも変換できるようにする（対応完了）
    * フォルダが存在していた場合、同様のフォルダ構成にできるとなおよし（できるかは知らない）
3. 明度の上昇割合を変更できるようにする
4. 実行時の引数の設定を読みやすいものに変更する