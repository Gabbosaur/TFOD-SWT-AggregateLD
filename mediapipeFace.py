import cv2
import mediapipe as mp
from deepface import DeepFace




mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
IMAGE_FILES = ['zeropadding.jpg']

width = 0
height = 0
padding = 50

with mp_face_detection.FaceDetection(
	model_selection=1, min_detection_confidence=0.5) as face_detection:
	for idx, file in enumerate(IMAGE_FILES):
		image = cv2.imread(file)
		print('width: ', image.shape[1])
		print('height:', image.shape[0])
		width = image.shape[1]
		height = image.shape[0]

    	# Convert the BGR image to RGB and process it with MediaPipe Face Detection.
		results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

		# Draw face detections of each face.
		if not results.detections:
			print("Nessuna faccia rilevata.")
			continue

		annotated_image = image.copy()
		for detection in results.detections:
			print("Faccia rilevata.")
			# print(detection.location_data.relative_bounding_box)
			xmin = int(detection.location_data.relative_bounding_box.xmin*width)
			ymin = int(detection.location_data.relative_bounding_box.ymin*height)
			w = int(detection.location_data.relative_bounding_box.width*width)+xmin
			h = int(detection.location_data.relative_bounding_box.height*height)+ymin

			# controllo immagine croppata che resti dentro all'immagine originale
			if xmin - padding >= 0:
				xmin = xmin - padding
			else:
				xmin = 0

			if ymin - padding >= 0:
				ymin = ymin - padding
			else:
				ymin = 0

			if w + padding <= width:
				w = w + padding
			else:
				w = width

			if h + padding <= height:
				h = h + padding
			else:
				h = height


			print(xmin)
			print(ymin)
			print(w)
			print(h)

			# print('Nose tip:')
			# print(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
			cropped_image = image[ymin:h, xmin:w]
			cv2.imwrite('face_of_' + str(file[:-4]) + '_face' + str(idx) + '.jpg', cropped_image)


			cv2.waitKey(0)
			cv2.destroyAllWindows()


			mp_drawing.draw_detection(annotated_image, detection)
		cv2.imwrite('annotated_image' + str(idx) + '.png', annotated_image)


# obj = DeepFace.analyze(img_path = "lec2.jpg")
# print(obj)
# result = DeepFace.verify(img1_path = "lec3.jpg", img2_path = "face_of_lec2_face0.jpg")
# print(result)
