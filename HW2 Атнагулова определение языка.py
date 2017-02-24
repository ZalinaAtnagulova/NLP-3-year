import random
import codecs
import collections
import sys
from itertools import islice, tee


def arrs(value):
    arr = []
    f = open(value, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    text = text.split('\n')
    for a in text:
        a = a.split(';')
        arr.append(a[1])
    return(arr)

def tokenize(text):
    return text.split(' ')

def make_ngrams(text):
    N = 3
    ngrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(text, N))))
    ngrams = [''.join(x) for x in ngrams]
    return ngrams

def specify_lang(file,arr_freq,arr_gram):
    methods = ['arr_freq', 'arr_gram']
    f = open(file, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    method = random.choice(methods)
    dic_freq = {}
    dic_gr = {}
    if method == 'arr_freq':
        print('Frequent words method')
        for word in tokenize(text.replace('\n', '').lower()):
            for l_name in arr_freq:
                if word in arr_freq[l_name]:
                    if l_name in dic_freq:
                        dic_freq[l_name] += 1
                    else:
                        dic_freq[l_name] = 1
        print(dic_freq)
    if method == 'arr_gram':
        print('N-gram method')
        for ngram in make_ngrams(text.replace('\n', '').lower()):
            for l_name in arr_gram:
                if ngram in arr_gram[l_name]:
                    if l_name in dic_gr:
                        dic_gr[l_name] += 1
                    else:
                        dic_gr[l_name] = 1
        print(dic_gr)
    
arr_freq = {}
arr_gram = {}
KK_freq_dic = arrs('KK1.txt')
arr_freq['kk'] = KK_freq_dic
UK_freq_dic = arrs('UK1.txt')
arr_freq['uk'] = UK_freq_dic
BE_freq_dic = arrs('BE1.txt')
arr_freq['be'] = BE_freq_dic
FR_freq_dic = arrs('FR1.txt')
arr_freq['fr'] = FR_freq_dic
KK_n_gram_dic = arrs('KK2.txt')
arr_gram['kk'] = KK_n_gram_dic
UK_n_gram_dic = arrs('UK2.txt')
arr_gram['uk'] = UK_n_gram_dic
BE_n_gram_dic = arrs('BE2.txt')
arr_gram['be'] = BE_n_gram_dic
FR_n_gram_dic = arrs('FR2.txt')
arr_gram['fr'] = FR_n_gram_dic
specify_lang('prob.txt',arr_freq,arr_gram)
