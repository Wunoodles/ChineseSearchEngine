##Chinese Sentence System

[中文字詞推薦](https://chinesesentencesystem.herokuapp.com/show)

##Initial
```
pip install -r requirements.txt
```
##Dataset

[SB0C4.txt](https://drive.google.com/open?id=0B_vjF2RvQ2EDeUh1NzJvT3F6Unc)
[datasorce](https://www.dropbox.com/sh/ukkyguhe19rtpac/AAALuSQKAC8IVhxDYfPhUZOYa?dl=0)

##Start
```
python api.py
```

##詞性分類
```
● 副詞 -> D
       -> DE(的)
● 動詞 -> V
       -> V_2(有)
● 名詞 -> N
       -> Nh(代名詞)
       -> Nf(量詞，包含Neqb、Neqa、Neu、Neu)
● 形容詞 -> A       
● 介系詞 -> P
● 連接詞 -> C
● 感嘆詞 -> I

```

##建立 Heroku 環境檔案
```
pip freeze > requirements.txt
echo web: python app.py > Procfile
```
