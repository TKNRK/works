# Mac でマウスカーソルをアニメーションGIFに変更する

TODO

- 画像を探す
- mousecape をインストールする
- gif を mousecape の使える形に加工する
- mousecape でマウスカーソルを設定する

## なんでそんなことする必要があるんですか（正論）

特に意味はない．マウスカーソルが好きなキャラだったら気分がいいから．

## マウスカーソルの画像を探す

- ググれば結構フリーのものが出てくる
- キャラクターものだったら，pixivやニコニコ静画にドット絵のgifやaniが配布されている
- 好きなGIFを見つけたら作業開始

## mousecape のダウンロード

マウスカーソルを変更するためのアプリ

- 昔のバージョンだと普通に設定できたらしいけど，現在は有料のアプリを使用することが正攻法．
- システムファイルを直接いじるアプローチもあるけれど，怖いので無理（私物のPCなら試してみてたかも）
- なので，mousecapeというフリーのアプリを使用

### mousecape

- [githubのページ](https://github.com/alexzielenski/Mousecape)
- [ダウンロードページ](https://github.com/alexzielenski/Mousecape/releases)

mousecape.zip をダウンロードして解凍

## 画像の加工

- フリーのマウスカーソルは windows 向けに配布されているものがほとんど
- ani 形式のファイルは mac では使えない！
- しょうがないので，アニメーションのコマが全て貼られているファイルをダウンロードして自力で使える形に加工する
- Python を使って作業．詳細は [image_processing]() へ

## mousecape で新しい cape を作成して適用

## 完成！

![before](img/)

![after](img/)

## 参考にしたサイト

- [https://blog.kr-kp.com/macos/howto-mouse-cursor-change-for-macosx.html](https://blog.kr-kp.com/macos/howto-mouse-cursor-change-for-macosx.html)

