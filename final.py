# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jqhYGzIbJxkf-J9m0S7-GahL4_lv6ghU
"""

!pip install face_recognition

import sys
import os
import cv2
import tensorflow as tf
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.resnet50 import preprocess_input
from IPython.display import clear_output
import numpy as np
import matplotlib.pyplot as plt
import dlib
import face_recognition

!git clone https://github.com/shyamsundar233/MaskDetection---ResNet50.git

sys.path.insert(0,'/content/MaskDetection---ResNet50')

from traindataset import training_dataset
from resnet50 import ResNet50

train_path = '/content/drive/MyDrive/Datasets/maskdata/maskdata/train'
test_path = '/content/drive/MyDrive/Datasets/maskdata/maskdata/test'
validation_path = '/content/drive/MyDrive/Datasets/maskdata/maskdata/validation1'

CLASSES=['GOOD! YOU ARE SAFE!!','PLEASE!! WEAR YOUR MASK!']

train_dataset,test_dataset = training_dataset(train_path,test_path)

model = ResNet50(input_shape=(224,224,3),classes=2)
  
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
clear_output()

model.fit(train_dataset,
          epochs=20,
          batch_size=32)

val_loss,val_acc = model.evaluate(train_dataset)
print(val_loss,val_acc)

path = '/content/drive/MyDrive/Datasets/maskdata/maskdata/validation1/validphotos'

for i in os.listdir(path):
  p = path + '/' + i
  img = load_img(p,target_size=(224,224))
  x = img_to_array(img)
  x = np.expand_dims(x,axis=0)
  x = preprocess_input(x)
  out = model.predict(x)
  prediction = (int) (out[0][1])
  print("-------------------------------------------------------------------------------------------------------------------")
  plt.imshow(img)
  plt.show()
  print()
  print(CLASSES[0]) if (prediction==0)  else print(CLASSES[1])

"""# **With Face Recognition**"""

from google.colab.patches import cv2_imshow

p = '/content/drive/MyDrive/Datasets/maskdata/maskdata/validation1/validphotos/Copy of 53.jpg'
img = load_img(p,target_size=(224,224))
x = img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)
out = model.predict(x)
prediction = (int) (out[0][1])
print("-------------------------------------------------------------------------------------------------------------------")
if (prediction==0):
  print(CLASSES[0])
  img1 = face_recognition.load_image_file(p)
  img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  faceLoc = face_recognition.face_locations(img1)[0]
  a,b,c,d = faceLoc
  faceEncode = face_recognition.face_encodings(img1)[0]
  cv2.rectangle(img1,(int (d),int (a)),(int (b),int (c)),(0,0,255),2)
  cv2_imshow(img1)
else:
  print(CLASSES[1])
  img1 = face_recognition.load_image_file(p)
  img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  faceLoc = face_recognition.face_locations(img1)[0]
  a,b,c,d = faceLoc
  faceEncode = face_recognition.face_encodings(img1)[0]
  cv2.rectangle(img1,(int (d),int (a)),(int (b),int (c)),(0,0,255),2)
  cv2_imshow(img1)