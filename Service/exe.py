from firebase_connect import Firebase
import joblib
model=joblib.load("104_model_63.pkl")
fr=Firebase(model,"BTCHABER")
fr.connect()