import sys

sys.path.append('..')
from sentiment import *
from bm25 import *

dic = {
    '0': 'can you fit make up brushes in the trays',
    '1': 'Can you move all the dividers?',
    '2': 'is the surface in side the smooth?',
    '3': 'How deep do the extending trays measure?',
    '4': 'Can bottles of nail polish stand upright in the top trays when the case is closed?'
}

print get_dict_sentiment(dic)

bm25 = BM25(dic, dic['0'])
print bm25.get_best()
print bm25.get_k_best(3)
