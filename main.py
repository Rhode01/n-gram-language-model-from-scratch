from typing import List, Tuple
from typing import Dict
sample_text = "Lady Frances is a lone, unwed woman denied a rich inheritance on account of her sex. She does, however, carry valuable jewels with her"
sample2 = "Watson finds out where Lady Frances went, and inquires at the Englischer Hof in Baden-Baden, Germany. She stayed there for a fortnight and met a couple described as Dr. Shlessinger, a convalescent missionary and biblical scholar from South America, and his wife."
def build_n_grams(token:List[str], n_words:int) -> List[Tuple[str]]:
    words = token.split()
    output = []
    for i in range(len(token)- n_words + 1 ):
        output.append(words[i:i + n_words])
    return output

BOS = '<BOS>'
EOS = '<EOS>'

def build_ngrams_ctrl(token:List[str], n_words: int) -> List[Tuple[str, str, str]]:
    tokens = token.split()
    tokens = [BOS, BOS] + tokens + [EOS, EOS]
    output = []
    for i in range(len(tokens) - n_words + 1):
        output.append(tuple(tokens[i:i + n_words]))
    return output

def count_ngrams(token: List[List[str]], n_words: int) -> Dict[Tuple[str, ...], Dict[str, int]]:
    output = {}
    words_in =  token.split()
    for word in words_in:
        ngrams_ctrl = build_ngrams_ctrl(word, n_words)
        for i in range(len(ngrams_ctrl) - 1):
            ngram = ngrams_ctrl[i][:-1]
            next_word = ngrams_ctrl[i+1][-1]
            if ngram not in output:
                output[ngram] = {}
            if next_word not in output[ngram]:
                output[ngram][next_word] = 0
            output[ngram][next_word] += 1
    return output
        
def build_ngram_model(texts: List[List[str]], n_words: int) -> Dict[Tuple[str, ...], Dict[str, float]]:
    ngram_counts = {}
    words_in =  texts.split()
    for word in words_in:
        ngram = ngram_counts.update(count_ngrams(word,n_words))
    ngram_model = {}
    for ngram, next_word_counts in ngram_counts.items():
        total_count = sum(next_word_counts.values())
        ngram_model[ngram] = {next_word: count / total_count for next_word, count in next_word_counts.items()}
        
    for ngram, next_word_probs in ngram_model.items():
        total_prob = sum(next_word_probs.values())
        ngram_model[ngram] = {next_word: prob / total_prob for next_word, prob in next_word_probs.items()}
    
    return ngram_model
        

print(build_ngram_model(sample_text, 3))
