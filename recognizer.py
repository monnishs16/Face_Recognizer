def recognizer():
	import cv2
	import pickle
	global names
	import trainer
	i=0

	face_classifier=cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt2.xml')
	recognizer= cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainner.yml')
	org_id={}

	with open('labels.pickle', 'rb') as f:
		org_id = pickle.load(f)
		invert_id = {v: k for k, v in org_id.items()}
	cap=cv2.VideoCapture(0)

	while cap.isOpened():
		ret,img=cap.read()
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces=face_classifier.detectMultiScale(gray,1.5,5)
		for (x,y,w,h) in faces:
			roi_gray=gray[y:y+h,x:x+w]
			_id,conf=recognizer.predict(roi_gray)

			cv2.rectangle(img,(x,y),(x+w,y+h),(180,100,20),1)
			if conf>=50:
				if not invert_id[_id] in names.keys():
					names[invert_id[_id]]=1
				else:
					names[invert_id[_id]] += 1
					cv2.putText(img,invert_id[_id],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

		cv2.putText(img,'PRESS q TO STOP SCAN', (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

		cv2.imshow('video', img)

		if i==0:
			i+=1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
names={}



