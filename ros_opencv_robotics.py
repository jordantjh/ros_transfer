#import numpy as np
from sklearn.cluster import KMeans
import numpy as np
import cv2

#https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
#next: try to use playstatino eye (try in ubuntu) https://stackoverflow.com/questions/34288653/how-to-operate-an-ps-eye-with-opencv

video_capture = cv2.VideoCapture(0)

while(True):
		ret, frame = video_capture.read()  #read() returns an image from the vid stream

		img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		
		img = img_rgb.reshape((img_rgb.shape[0] * img_rgb.shape[1],3)) #represent as row*column,channel number
		clt = KMeans(n_clusters=3) #cluster number
		clt.fit(img)

		# for width in range(480):
		# 	for height in range(640):
		# 		print(img_rgb[width][height][0])

		#r, g, b = frame.split(img_rgb)

		cv2.imshow("Frame", frame)
		if cv2.waitKey(100) & 0xFF == ord('q'):
			break

print(clt.cluster_centers_)

video_capture.release()
cv2.destroyAllWindows()