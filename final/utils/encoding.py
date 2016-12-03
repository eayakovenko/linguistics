# -*- coding: UTF-8 -*-

# forming dictionary code
def form_dict():
    dictionary = {}
    for i in range(0, 127):
        dictionary[i] = chr(i)
    return dictionary


# coding words to letters
def encode_val(word):
    list_code = []
    lent = len(word)
   
    d = form_dict()
   
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code


# comparing two dicts
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
 
    return dic  
 
# finish full encode  
def full_encode(value, key):
    dic = comparator(value, key)
 
    lis = []
    d = form_dict()
 
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis
   
# DECODER
 
# decode to numeric values
def full_decode(value, key):
 
    dic = comparator(value, key)
    d = form_dict()
    lis = []
    for v in dic:
        go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
        lis.append(go)
    return lis
   
 
def decode_val(list_in):
    list_code = []
    lent = len(list_in)
 
    d = form_dict()
   
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
                list_code.append(d[value])
    return list_code


def encode_text(text, key):
    key_encoded = encode_val(key)
    value_encoded = encode_val(text)
    shifre = full_encode(value_encoded, key_encoded)
    return ''.join(decode_val(shifre))


def decode_text(text, key):
    key_encoded = encode_val(key)
    text = list(text)
    decoded = full_decode(encode_val(text), key_encoded)
    return ''.join(decode_val(decoded))
