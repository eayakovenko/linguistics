# -*- coding: UTF-8 -*-

eps = 5
ENG = {"a" : 8.167, "b" : 1.492, "c" : 2.782, "d": 4.253, "e" : 12.702, "f" : 2.228,
       "g" : 2.015, "h" : 6.094, "i" : 6.966, "j" : 0.153, "k" : 0.772, "l" : 4.025,
        "m" : 2.406, "n" : 6.749, "o" : 7.507, "p" : 1.929, "q" : 0.095, "r" : 5.987,
       "s" : 6.327, "t" : 9.056, "u" : 2.758, "v" : 0.978, "w" : 2.360, "x" : 0.150,
       "y" : 1.974, "z" : 0.074
       }
FR = {"a" : 7.636, "b" : 0.901, "c" : 3.260, "d": 3.669, "e" : 14.715, "f" : 1.066,
       "g" : 0.866, "h" : 0.737, "i" : 7.529, "j" : 0.613, "k" : 0.049, "l" : 5.456,
       "m" : 2.968, "n" : 7.095, "o" : 5.598, "p" : 2.521, "q" : 1.362, "r" : 6.693,
       "s" : 7.948, "t" : 7.244, "u" : 6.311, "v" : 1.838, "w" : 0.074, "x" : 0.427,
       "y" : 0.128, "z" : 0.326}
GR = {"a" : 6.516, "b" : 1.886, "c" : 2.732, "d": 5.076, "e" : 16.396, "f" : 1.656,
       "g" : 3.009, "h" : 4.577, "i" : 6.550, "j" : 0.268, "k" : 1.417, "l" : 3.437,
            "m" : 2.534, "n" : 9.776, "o" : 2.594, "p" : 0.670, "q" : 0.018, "r" : 7.003,
       "s" : 7.273, "t" : 6.154, "u" : 4.166, "v" : 0.846, "w" : 1.921, "x" : 0.034,
       "y" : 0.039, "z" : 1.134}

Lang = [ENG, FR, GR]


def define_language(text):
	fr = {
	    "a" : 0, "b" : 0, "c" : 0, "d": 0, "e" : 0, "f" : 0,
   		"g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0,
    	"m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0,
   		"s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
   		"y" : 0, "z" : 0
   	}

	count = 0.0
	for char in text:
		if char.lower() >= "a" and char.lower() <= "z":
			count += 1
			fr[char.lower()] += 1

	for i in xrange(ord("a"), ord("z")):
		if fr[chr(i)] != 0:
			fr[chr(i)] = fr[chr(i)] / count * 100
		rr = 0

	summ = [0, 0, 0]
	for i in range(ord("a"), ord("z")):
		for j in range(0, len(Lang)):
			rr = abs(fr[chr(i)] - Lang[j][chr(i)])
			summ[j] += rr

	min = summ[0]
	mini = 0
	for i in range(1, len(summ)):
		if summ[i] < min:
			min = summ[i]
			mini = i

	if abs(summ[0] - summ[1]) < eps and abs(summ[1] - summ[2] < eps):
		return -1
	elif mini == 0:
		return u"Английский"
	elif mini == 1:
		return u"Французский"
	elif mini == 2:
		return u"Немецкий"