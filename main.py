from typing import List, Tuple

sample1 = ['It', 'shows', ',', 'my', 'dear', 'Watson', ',', 'that',
           'we', 'are', 'dealing', 'with', 'an', 'exceptionally',
           'astute', 'and', 'dangerous', 'man', '.']
sample2 = [
    ('It', 'shows', ','),
 ('shows', ',', 'my'),
 (',', 'my', 'dear'),
 ...,
 ('dangerous', 'man', '.')
]

def build_n_grams(token:List[str], n:int) -> List[Tuple[str]]:
    pass

build_n_grams(sample1,3)

BOS = '<BOS>'
EOS = '<EOS>'
def build_ngrams_ctrl(tokens: List[str], n: int) -> List[Tuple[str]]:
    pass
   

build_ngrams_ctrl(sample1, n=3)
assert len (build_ngrams_ctrl(sample1, n=3)) 
from typing import Dict
def build_ngram_model(texts: List[List[str]], n: int) -> Dict[Tuple[str, ...], Dict[str, float]]:
    pass
    
build_ngram_model([sample1, sample2], n=3)

full_text = []
with open('arthur-conan-doyle.tok.train.txt', 'rt') as fin:
    for line in fin:
        full_text.append(list(line.split()))
model = build_ngram_model(full_text, n=3)
for prefix in [(BOS, BOS), (BOS, 'It'), ('It', 'was'), ('my', 'dear')]:
    print(*prefix)
    sorted_probs = sorted(model[prefix].items(), key=lambda x: -x[1])
    for k, v in sorted_probs[:5]:
        print(f'\t{k}\t{v:.4f}')
    print(f'\t[{len(sorted_probs)-5} more...]')