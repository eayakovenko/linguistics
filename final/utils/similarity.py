# -*- coding: UTF-8 -*-

import binascii

STOP_SYMBOLS = '.,!?:;-\n\r()'
STOP_WORDS = (
    u'это', u'как', u'так',
    u'и', u'в', u'над',
    u'к', u'до', u'не',
    u'на', u'но', u'за',
    u'то', u'с', u'ли',
    u'а', u'во', u'от',
    u'со', u'для', u'о',
    u'же', u'ну', u'вы',
    u'бы', u'что', u'кто',
    u'он', u'она'
)


def canonize(source):
    return [x for x in [y.strip(STOP_SYMBOLS) for y in source.lower().split()] if x and (x not in STOP_WORDS)]


def gen_shingle(source, shingle_len=2):
    shingle_len = shingle_len
    out = []
    if len(source) - (shingle_len - 1) < 1:
        return source
    for i in range(len(source) - (shingle_len - 1)):
        out.append(binascii.crc32(' '.join( [x for x in source[i:i + shingle_len]] ).encode('utf-8')))
    return out


def compare(source1, source2):
    same = 0
    for i in range(len(source1)):
        if source1[i] in source2:
            same = same + 1
    return same * 2 / float(len(source1) + len(source2)) * 100


def similarity_score(text1, text2):
    cmp1 = gen_shingle(canonize(text1))
    cmp2 = gen_shingle(canonize(text2))
    return compare(cmp1, cmp2)