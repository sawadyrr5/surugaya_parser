# surugaya_parser
suruga-ya.jpから条件指定で販売一覧・詳細と買取一覧・詳細のデータを取得します

インポート

```
from requests import session
from pprint import pprint
from surugaya_parser import Search, SearchDetail, KaitoriSearch, KaitoriSearchDetail

s = session()
```

販売一覧を取得

```
# 販売一覧
pg = Search(s, '11', '艦隊これくしょん かげぬい')
pprint(pg.items)
```

販売一覧の取得結果

```
[Item(title='<<艦隊これくしょん>> かげぬい総集編 2 / たまごやき', code='ZHORE218115', category='男性向一般同人誌', brand='たまごやき', release_date='2019/08/09', price=None, price_normal=None, price_teika='920'),
 Item(title='<<艦隊これくしょん>> かげぬい 総集編 / たまごやき', code='ZHORE150594', category='男性向一般同人誌,値下げ', brand='たまごやき', release_date='2016/08/13', price=None, price_normal='590', price_teika='500'),
 Item(title='<<艦隊これくしょん>> KAGENUI(かげぬい) 1 / Oeuf', code='ZHORE176261', category='男性向一般同人誌', brand='Oeuf', release_date='2017/04/30', price=None, price_normal='2100', price_teika='1700')]
```

販売詳細の取得

```
# 販売詳細
pgd = SearchDetail(s, 'ZHORE150594')
pprint(pgd.item)
```

販売詳細の取得結果

```
ItemDetail(title='<<艦隊これくしょん>> かげぬい 総集編 / たまごやき', code='ZHORE150594', category='男性向一般同人誌', release_date='2016/08/13', price_teika='-', brand='たまごやき', model_number='-', picture='星野蒼一朗')
```


買取一覧を取得

```
# 買取一覧
kpg = KaitoriSearch(s, '11', '艦隊これくしょん かげぬい')
pprint(kpg.items)
```

買取一覧の取得結果

```
[KaitoriItem(title='<<艦隊これくしょん>> カゲヌイ オルタナティブ / ぷかぷか亭', code='ZHORE224002', category='男性向一般同人誌', price='700'),
 KaitoriItem(title='<<艦隊これくしょん>> かげぬい総集編 2 / たまごやき', code='ZHORE218115', category='男性向一般同人誌', price='300'),
 KaitoriItem(title='<<艦隊これくしょん>> かげぬい 総集編 / たまごやき', code='ZHORE150594', category='男性向一般同人誌', price='150'),
 KaitoriItem(title='<<艦隊これくしょん>> KAGENUI(かげぬい) 1 / Oeuf', code='ZHORE176261', category='男性向一般同人誌', price='700'),
 KaitoriItem(title='<<艦隊これくしょん>> かげぬい ごった煮 / さぼてにずむ', code='ZHORE171033', category='男性向一般同人誌', price='150'),
 KaitoriItem(title='<<艦隊これくしょん>> かげぬいはいつだって命懸け', code='ZHORE126270', category='男性向一般同人誌', price='100')]
```

買取詳細の取得

```
# 買取詳細
kpgd = KaitoriSearchDetail(s, 'ZHORE150594')
pprint(kpgd.item)
```

買取詳細の取得結果

```
KaitoriItemDetail(title='<<艦隊これくしょん>> かげぬい 総集編 / たまごやき', jan='-', code='ZHORE150594', catogory='男性向一般同人誌', release_date='2016/08/13', price='150', list_price='-', brand='たまごやき', model_number='-', picture='星野蒼一朗', explanation='68p/総集編/C90発行')
```







