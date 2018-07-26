from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import MyForm

import csv
import numpy as np

def name_catch(form):
    name = str(form)
    name = name[87:]
    ind = name.find('"')
    name = name[:ind]
    return name

def csv_new_line(data):
    f = open('data.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow([data])
    f.close()

def form_test(request):
    if request.method == "POST":
        form = MyForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            name = name_catch(form)
            csv_new_line(name)
            return HttpResponseRedirect("/hikaku")
            pass  # ← 正しいデータを受け取った場合の処理
            # return render(request, 'form_test.html', {
            #     'form': form,
            # })
    else: # ← methodが'POST'ではない = 最初のページ表示時の処理
        form = MyForm()
        return render(request, 'form_test.html', {
            'form': form,
        })


def hikaku(request):
    name = request.GET.get('your_name')
    if request.method == "GET":
        # form = MyForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        # if form.is_valid():  # ← 受け取ったデータの正当性確認
        return HttpResponseRedirect("/form2?your_name="+name)
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        # form = MyForm()
        return render(request, 'saisyo.html', {'form': form,})


def csv_new(data):
    f = open('data.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(data)
    f.close()

def csv_serach(data):
    d = []
    re = 0
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            d.append(line)
    for i in range(len(d)):
        if d[i][0] == data:
            re = i
    return re

def csv_serach_add(name,num):
    d = []
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == name:
                line.append(num)
                d.append(line)
            else:
                d.append(line)
    with open('data.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(d)

def lengthdata(name):
    d = []
    with open('data.csv', 'r') as f:
        read = csv.reader(f)
        for line in read:
            if line[0] == name:
                d.append(line)
    try:
        if len(d[0]) > 40:
            return False
        else:
            return True
    except IndexError:
        return True

def lengthdata_num(name):
    d = []
    with open('data.csv', 'r') as f:
        read = csv.reader(f)
        for line in read:
            if line[0] == name:
                d.append(line)
    return (len(d[0]))

def checke_num(txt):
    txt = str(txt)
    ind = txt.find('choice')
    name = txt[ind+11:ind+12]
    return name

from .forms import HelloForm
import random
#checked
def detail(request):
    n = random.randrange(1,6,1)
    im = random.randrange(660)
    name = request.GET.get('your_name')
    if n > 2:
        image = 'static/test_data/'+str(n)+'/'+"{0:03d}".format(im)+'.png'
    else:
        image = 'static/test_data/'+str(n)+'/'+str(im)+'.png'
    if n == 1:
        n = 'a'
    if n == 2:
        n = 'b'
    if n == 3:
        n = 'c'
    if n == 4:
        n = 'd'
    if n == 5:
        n = 'e'
    if n == 6:
        n = 'f'
    num = 0
    num = csv_serach(name)
    endor = lengthdata(name)

    if endor:
        if request.method == "POST":
            form = HelloForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
            if form.is_valid():  # ← 受け取ったデータの正当性確認
                pass  # ← 正しいデータを受け取った場合の処理
                data = request.POST
                csv_serach_add(name, checke_num(data))
                csv_serach_add(name, n)
                nume = ((lengthdata_num(name)-1)/2)-0.5
                nume = int(nume)
                return render(request, 'form_test2.html', {
                    'image': image,
                    'nume': nume,
                    'form': form,
                })
        else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
            form = HelloForm()
            if num == 0:
                csv_new([name, n])
            else:
                csv_serach_add(name, n)
            nume = 0
            return render(request, 'form_test2.html', {
                'image': image,
                'nume': nume,
                'form': form,
            })
    else:
        return HttpResponseRedirect("/kekka?your_name="+name)


def kekka_csv(name):
    d = []
    ans = 0
    wakaran = 0
    text = ""
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == name:
                d.append(line)
    try:
        d = d[0]
        for i in range(1,len(d)-1,2):
            if d[i] == d[i+1]:
                text = text + d[i]+'-'+d[i+1]+' 正解\n'
                ans += 1
            elif d[i+1] == 'f':
                wakaran += 1
            else:
                text = text + d[i]+'-'+d[i+1]+' 不正解\n'
    except IndexError:
        for i in range(1, len(d)-1, 2):
            if d[i] == d[i+1]:
                text = text + d[i]+'-'+d[i+1]+' 正解\n'
                ans += 1
            elif d[i+1] == 'f':
                wakaran += 1
            else:
                text = text + d[i]+'-'+d[i+1]+' 不正解\n'
    return text, ans, wakaran


def minnnakekka_csv():
    d = []
    ans = 0
    ansritu = 0
    wakaran = 0
    text = ""
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            d.append(line)
    for e in range(len(d)):
        ans = 0
        for i in range(1, len(d[e])-1, 2):
            if d[e][i] == d[e][i+1]:
                ans += 1
            elif d[e][i+1] == 'f':
                wakaran += 1
        if wakaran == 20:
            ansritu = ansritu + (ans/(20-19)*100)
        else:
            ansritu = ansritu + (ans/(20-wakaran)*100)
    ansritu = ansritu / len(d)
    return ansritu

def kekka(request):
    name = request.GET.get('your_name')
    re,ans,wakaran = kekka_csv(name)
    if wakaran == 20:
        seirouritu = ans/(20-19)*100
    else:
        seirouritu = ans/(20-wakaran)*100
    ansritu = minnnakekka_csv()
    return render(request, 'form_kekka.html', {'kekka': re, 'ans': ans, 'seirouritu': seirouritu, 'ansritu': ansritu})

