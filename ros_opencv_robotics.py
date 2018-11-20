#import numpy as np
from sklearn.cluster import KMeans
import numpy as np
import cv2

#https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
#next: try to use playstatino eye (try in ubuntu) https://stackoverflow.com/questions/34288653/how-to-operate-an-ps-eye-with-opencv

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def main():
	video_capture = cv2.VideoCapture(0)
	counter = 1

	while(True):
			ret, frame = video_capture.read()  #read() returns an image from the vid stream

			img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			
			img = img_rgb.reshape((img_rgb.shape[0] * img_rgb.shape[1],3)) #represent as row*column,channel number
			clt = KMeans(n_clusters=1) #cluster number
			clt.fit(img)

			hist = find_histogram(clt)

			print("counter = " + str(counter))
			for (percent, color) in zip(hist, clt.cluster_centers_):
				r = color[0]
				g = color[1]
				b = color[2]
				
				if r>80 and r<120 and g>135 and b>90 and b<140 :   # check if green
					print("green!")
				elif r>115 and r<175 and g>125 and g<180 and b<75 :    # check if yellow
					print("yellow!")
				elif r>190 and g>75 and g<120 and b>65 and b<95 :  #check if red
					print("Red!")
				else:
					print("ignored!")

			cv2.imshow("Frame", frame)
			if cv2.waitKey(100) & 0xFF == ord('q'):
				break

	video_capture.release()
	cv2.destroyAllWindows()

main()