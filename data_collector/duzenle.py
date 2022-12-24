
#TOPLANAN VERİLERİN DÜZENLENMESİ
"""
file=open ("haberler.txt","r",encoding="utf-8")
a=file.read().split('\n\n')
print(len(a))
"""
#sonu : olanlar
"""
tut=[]
file2=open('sil.txt','w',encoding='utf-8')
for i in range (1,15500):
    if a[i][-1]==':':
        tut.append(a[i])    
        file2.write(f'{a[i]}\n\n')
""" 
"""
arr=[]
for i in range (15482):
    b=a[i].split('\n')
    b.pop(0)
    arr.append(b)

date=[]
news=[]    
for i in range(15482):
    pre_date=arr[i][0][0:10]
    date.append(pre_date)
    news.append(arr[i][1])

p(date[15480]) 
p(news[15480]) 

file2=open('duzen_haberler.txt','w',encoding='utf-8')

for i in range(15482):
    file2.write(f'{date[i]}     {news[i]}\n')
"""

"""
file1=open('tarih.txt','r',encoding='utf-8')
tarihler=file1.read().split('\n')
file2=open('kapanis.txt','r',encoding='utf-8')
kapanislar=file2.read().replace('.','').replace(',','.').split('\n')
for i in range(1365):
    kapanislar[i]=float(kapanislar[i])
p(len(tarihler))
p(len(kapanislar))
artar=0
azalır=0
hata=0
file3=open('artar_azalir.txt','w',encoding='utf-8')
for i in range(1,1365):
    if kapanislar[i-1]-kapanislar[i]>0:
        file3.write(f'{tarihler[i]} artar\n')
        artar=artar+1
    elif kapanislar[i-1]-kapanislar[i]<=0:
        file3.write(f'{tarihler[i]} azalir\n')
        azalır=azalır+1
    else:
        file3.write(f'{tarihler[i]} HATAAAAAAAAAAAAAAA\n')
        hata=hata+1
print(artar,azalır,hata)
"""
"""
file=open ("haberler.txt","r",encoding="utf-8")
a=file.read().split('\n\n')
arr=[]
for i in range (15482):
    b=a[i].split('\n')
    b.pop(0)
    arr.append(b)

date=[]
news=[]    
for i in range(15482):
    pre_date=arr[i][0][0:10]
    date.append(pre_date)
    news.append(arr[i][1])
tutucu=[]
for i in range(1,15481):
    
    if date[i]==date[i-1]:
        news[i]=news[i-1]+news[i]
        tutucu.append(f'{date[i]}    {news[i]}')
    else:
        tutucu.append(f'{date[i]}   {news[i]}')


file2=open('toplama_haber.txt','w',encoding='utf-8')
for i in range(15479,0,-1):
    try:
        if i==15479:
            file2.write(f'{tutucu[i]}\n')
        if tutucu[i][0:10]!=tutucu[i+1][0:10]:
            file2.write(f'{tutucu[i]}\n')
    except:
        pass
"""
"""
file1=open('toplama_haber.txt','r',encoding='utf-8')
file2=open('artar_azalir.txt','r',encoding='utf-8')
file3=open('etiketli_haber.txt','w',encoding='utf-8')
haberler=file1.read().split('\n')
durum=file2.read().split('\n')
tut=[]
for i in range (1366):
    for j in range(1211):
        if durum[i][0:10]==haberler[j][0:10]:
            #tut.append(f'{durum[i]} {haberler[j][13:]}')
            file3.write(f'{durum[i]} {haberler[j][13:]}\n')
"""
'''
file1=open('etiketli_haber.txt','r',encoding='utf-8')
haberler=file1.read().split('\n')
"""
for i in range(1,1210):
    if haberler[i][0:10]==haberler[i-1][0:10]:
        print(haberler[i][0:10])
"""
print(len(haberler))
file3=open('etiketli_haber_yeni.txt','w',encoding='utf-8')
haberler.remove(haberler[933])
haberler.remove(haberler[934])
print(len(haberler))

for i in range(1208):
    file3.write(f'{haberler[i]}\n')
'''
"""
file1=open('etiketli_haber_yeni.txt','r',encoding='utf-8')
file2=open('data_haber.txt','w',encoding='utf-8')
file3=open('data_etiket.txt','w',encoding='utf-8')
oku=file1.read().split('\n')
print(oku[1][11:17])

for i in range(1207):
    file2.write(f'{oku[i][17:].strip()}\n')
    file3.write(f'{oku[i][11:17].strip()}\n')
"""
