from requests import session
from pprint import pprint
from surugaya_parser import Search, SearchDetail, KaitoriSearch, KaitoriSearchDetail

s = session()

# 販売一覧
pg = Search(s, '11', '艦隊これくしょん かげぬい')
pprint(pg.items)

# 販売詳細
pgd = SearchDetail(s, 'ZHORE150594')
pprint(pgd.item)

# 買取一覧
kpg = KaitoriSearch(s, '11', '艦隊これくしょん かげぬい')
pprint(kpg.items)

# 買取詳細
kpgd = KaitoriSearchDetail(s, 'ZHORE150594')
pprint(kpgd.item)
