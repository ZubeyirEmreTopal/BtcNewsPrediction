import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading
import time
from convert_vect import Binary

class Firebase:
    def __init__(self,model,collection) :
        self.model=model
        self.collection=collection
        self.callback_done = threading.Event()
        cred= credentials.Certificate("firebase_sdk.json")
        firebase_admin.initialize_app(cred)
        self.db=firestore.client()
        doc_ref_emp= self.db.collection('BTCHABER')
        docs_emp=doc_ref_emp.stream()
        self.deger=len(list(docs_emp))
        self.bn=Binary()
        self.deger_dict={}

    def on_snapshot(self,doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            self.deger_dict[doc.id]="empt"
        self.callback_done.set()

    def connect(self):
        doc_ref = self.db.collection(self.collection)
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)
        while True:
            time.sleep(3)
            print(self.deger)
            if  self.deger<len(self.deger_dict.keys()):
                doc_ref_emp= self.db.collection(self.collection).where("durum","==","empty")
                docs=doc_ref_emp.stream()
                for doc in docs:
                    self.deger=self.deger+1
                    metin=doc.to_dict()["haber"]
                    kelime_vek=self.bn.kok_temizlik(metin)
                    predict=self.model.predict([kelime_vek])
                    if predict[0]==0:
                        predict="azalir"
                    else: 
                        predict="artar"
                    doc_wr= self.db.collection(self.collection).document(doc.id)
                    doc_wr.set({
                    "durum":f"{str(predict)}",
                    "haber":f"{metin}"
                })