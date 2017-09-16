# enermemo - Python製メモスクリプト

[![Twitter](https://imgur.com/Ibo0Twr.png)](https://twitter.com/miyagaw61)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

![top](https://i.imgur.com/7QFAylu.png)

# install

```
pip install "git+https://github.com/miyagaw61/enermemo.git#egg=enermemo" --find-links="git+https://github.com/miyagaw61/enert.git#egg=enert-0.0.1"
```

# Usage

* conf_file作成
```
vim my.conf
```

* \[タグ\]:\[項目名\]:\[初期値\]
```
a:RAX:0x0000
b:RBX:0x0000
c:RCX:0x0000
```

* 実行
```
python /SOMEWHERE/enermemo.py my.conf
```

* 移動
```
jとkで上下に。
タグを入力することでそのタグの項目へ移動します。
複数のタグが存在する場合は、ループします。
```

* 更新
```
ENTERキーを押すことで値を更新することができます。
```

* 項目追加
```
+キーを押すことで項目を追加することができます。
```
![Add](https://i.imgur.com/f39g3nW.png)

* スナップショット作成
```
Ctrl+sを押すことでスナップショットを作成することができます。
次回、コマンドライン引数にスナップショットを与えて実行すれば、続きからできます。
```
![Imgur](https://i.imgur.com/CEz5kyw.png)
