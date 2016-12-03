#-*- coding: UTF-8 -*-

from django.shortcuts import render
from .utils.language import define_language
from .utils.similarity import similarity_score
from .utils.natural import natural_language_coeff
from .utils.encoding import encode_text, decode_text


def index(request):
    return render(request, 'index.html')


def language(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        text = file.read()
        filename = file.name
        file.close()
        try:
            lang = define_language(text)
        except Exception as err:
            return render(request, 'language.html', {'error': err})
        return render(request, 'language.html', {'filename': filename, 'language': lang})

    return render(request, 'language.html')


def similarity(request):
    if request.method == 'POST':
        if 'file1' not in request.FILES or 'file2' not in request.FILES:
            print 'fail'
            return render(request, 'similarity.html', {'error': u'Необходимо загрузить два файла!'})
        file1, file2 = request.FILES['file1'], request.FILES['file2']
        text1 = file1.read()
        filename1 = file1.name
        file1.close()
        text2 = file2.read()
        filename2 = file2.name
        file2.close()

        try:
            similarity = round(similarity_score(text1, text2), 2)
        except Exception as err:
            return render(request, 'similarity.html', {'error': err})

        return render(request, 'similarity.html', {'filename1': filename1, 'filename2': filename2, 'score': similarity})
    return render(request, 'similarity.html')


def encoding(request):
    if request.method == 'POST':
        if 'key' in request.POST and 'text' in request.POST:
            try:
                text = request.POST['text']
                key = request.POST['key']
                encoded_text = encode_text(text=text, key=key)
                encoded_text = encoded_text.encode('string-escape')
            except Exception as err:
                return render(request, 'encoding.html', {'error': err})
            return render(request, 'encoding.html', {'encoding_text': request.POST['text'],
                                                     'encoded_text': encoded_text,
                                                     'key': key})
    return render(request, 'encoding.html')


def decoding(request):
    if request.method == 'POST':
        if 'key' in request.POST and 'text' in request.POST:
            try:
                text = request.POST['text'].decode('string-escape')
                key = request.POST['key']

                decoded_text = decode_text(text=text, key=key)
                decoded_text = decoded_text.encode('string-escape')
            except Exception as err:
                return render(request, 'encoding.html', {'error': err})
            return render(request, 'encoding.html', {'decoding_text': request.POST['text'],
                                                     'decoded_text': decoded_text,
                                                     'key': key})
    return render(request, 'encoding.html')


def natural(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        text = file.read()
        filename = file.name
        file.close()
        try:
            score = round(natural_language_coeff(text), 2)
        except Exception as err:
            return render(request, 'natural.html', {'error': err})

        return render(request, 'natural.html', {'filename': filename, 'score': score})

    return render(request, 'natural.html')


def report(request):
    return render(request, 'report.html')


def test_report(request):
    return render(request, 'test_report.html')
