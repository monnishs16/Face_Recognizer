import cv2
import numpy as np
from PIL import Image
import os
import pickle
face_classifier=cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
recognizer= cv2.face.LBPHFaceRecognizer_create()

ap=os.path.abspath('__name__')
dn=os.path.dirname(ap)
il=os.path.join(dn,'images')

c_id=0
label_ids={}
x_train=[]
y_labels=[]

for root,dirs,files in os.walk(il):
    for i in files:
        if i.endswith('jpeg') or i.endswith('jpg') or i.endswith('png'):
            path=os.path.join(root,i)
            label=os.path.basename(root)
            if not label in label_ids:
                label_ids[label]=c_id
                c_id+=1
            _id=label_ids[label]
            pimg=Image.open(path).convert("L")
            fimg=pimg.resize((550,550))
            iarr = np.array(fimg,'uint8')
            faces = face_classifier.detectMultiScale(iarr, 1.5, 5)
            for x,y,w,h in faces:
                roi= iarr[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(_id)
with open('labels.pickle','wb') as f:
    pickle.dump(label_ids,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save('trainner.yml')