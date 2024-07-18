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

def building_n_gram(token:List[str], n:int) -> List[Tuple[str]]:
    pass

building_n_gram(sample1,3)