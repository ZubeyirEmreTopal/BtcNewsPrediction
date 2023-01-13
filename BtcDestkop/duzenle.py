
import string
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import List
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM, java
import jpype
from nltk.stem.porter import PorterStemmer


class Binary:
    def __init__(self):
        ZEMBEREK_PATH = 'zemberek-full_old.jar'
        startJVM(getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))
        TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
        self.morphology = TurkishMorphology.createWithDefaults()
        nltk.download('stopwords')
        nltk.download('punkt')

    
    def kelime_temizlik(self,metin):
        yeniMetin=''
        for i in metin:
            if i not in string.punctuation:
                yeniMetin += i
        yorum=yeniMetin
        yorum=yorum.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
        yorum=yorum.lower()
        yorum=yorum.split()
        ps=PorterStemmer()
        yorum=[ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words('turkish'))]
        yorum= ' '.join(yorum)
        token = word_tokenize(yorum)
        return token

    def kok_temizlik(self,metin):
        token=self.kelime_temizlik(metin)
        lemma_word_top=''
        for i in range(len(token)):
            lemma_word = str(self.morphology.analyzeAndDisambiguate(str(token[i])).bestAnalysis()[0].getLemmas()[0])
            lemma_word_top=f'{lemma_word_top} {lemma_word}'
        file = open("ozel_kelimeler.txt","r",encoding="utf-8")
        kelimeler=file.read().split("\n")
        binary=[]
        for i in range(len(kelimeler)):
            #if metin.count(kelimeler[i])>1:
            #    print(kelimeler[i])
            binary.append(metin.count(kelimeler[i]))
        return binary



