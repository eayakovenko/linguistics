# -*- coding: UTF-8 -*-

STOPS = (',', '.', '!', '?', ':', ';',)


def natural_language_coeff(text):
    freq = {}
    words = text.split(' ')

    for word in words:
        if len(word) == 0:
            continue
        if len(word) == 1:
            if word not in STOPS:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

        if word[-1] in STOPS:
            if word[:-1] in freq:
                freq[word[:-1]] += 1
            else:
                freq[word[:-1]] = 1
        elif word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    fr = sorted(freq.items(), key=lambda(k,v): v, reverse=True)
    summ = 0
    count = fr[0][1]
    for i in range(1, len(fr)):
        summ += abs(float(fr[0][1]) / (i + 1) - fr[i][1])
        count += fr[i][1]

    return 100 - (summ / count) * 100
