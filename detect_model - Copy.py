import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from keras.models import load_model
from keras.utils import to_categorical

model = load_model('total1.h5')

#img_path = 'Put you image path'

###test image ###
img_path = 'E:\\source\\practice\\hackfest\\detect_model\\detect_model\\obj\\1.70.jpg'

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.resize(img, (300, 300))
img = np.array(img)
img = img.reshape(1, 300, 300, 3)
print(model.predict(img))


