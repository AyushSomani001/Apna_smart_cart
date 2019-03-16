import ast
import firebase_admin

from firebase_admin import credentials, firestore


# f = open('gy.txt', 'r').read()
# x = ast.literal_eval(f)
# inv_x = {v: k for k, v in x.items()}
list_items = ['box', 'blue_bottle', 'notebook', 'can', 'red_bottle', 'box_cap']
price_dict = {'box':10, 'blue_bottle':15, 'notebook':20, 'can':25, 'red_bottle':30, 'box_cap':35}
dics_dict = {'box':10, 'blue_bottle':10, 'notebook':5, 'can':10, 'red_bottle':15, 'box_cap':20}

class Manage():
    def __init__(self, x, y, z):
        self.cred = credentials.Certificate('.//login-2-7789b-firebase-adminsdk-sbe0v-da279e5330.json')
        default_app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        # self.object_doc_dict = inv_x
        # self.doc_object_dict = x
        self.list_items = x
        self.price_dict = y
        self.dics_dict = z



    def retrieve(self):
        self.li = []
        for key in self.list_items:
            
            #print(key)
                #val = 
            doc_ref = self.db.collection(u'cart_items').document(key)
            doc = doc_ref.get()

            self.li.append(doc.to_dict())
            
            # except:
            #     pass
        return self.li
        

    def update(self, object, direction):
        self.cart_dict = self.retrieve()
        doc_ = object
        if direction == 0:
            for field in self.li:
                if field is not None:
                    if object == field['name'] :
                        
                        doc_ref = self.db.collection(u'cart_items').document(doc_)
                        doc_ref.set({
                            u'name':field['name'],
                            u'qty':field['qty'] + 1,
                            u'price':field['price'],
                            u'discount':field['discount'],
                            })
                        return

            doc_ref = self.db.collection(u'cart_items').document(doc_)
            doc_ref.set({
                u'name':doc_,
                u'qty':1,
                u'price':self.price_dict[doc_],
                u'discount':self.dics_dict[doc_]
                })

        if direction == 1:
            for field in self.li:
                if field is not None:
                    if object == field['name'] :
                        
                        doc_ref = self.db.collection(u'cart_items').document(doc_)
                        doc_ref.set({
                            u'name':field['name'],
                            u'qty':field['qty'] - 1,
                            u'price':field['price'],
                            u'discount':field['discount'],
                            })
                        return
        



        # doc_ref = db.collection(u'sampledata').document(u'inspiration')
        # doc_ref.set({
	       #  u'quote':"Hi all",
	       #  u'author':"Me"
	       #  })


# try:
#     doc = doc_ref.get()
#     print(u'document data :  {}'.format(doc.to_dict()))
# except:
#     print("datatabase retrieval failed")

#k = Manage(list_items, price_dict, dics_dict)
#print(k.retrieve())
#k.update('box', 1)
# k.update('blue_bottle')
# k.update('red_bottle')
# k.update('box_cap')
# k.update('can')
# k.update('notebook')