# -*- coding: utf-8 -*-
"""trainDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iHBOEnFH_jCzRTp6eZttLuQDPXukIYX
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input

def training_dataset(train_path,test_path):
  train_datagen = ImageDataGenerator(preprocessing_function = preprocess_input, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True,validation_split=0.4)
  #test_datagen = ImageDataGenerator(preprocessing_function = preprocess_input, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True,validation_split=0.4)

  train_dataset = train_datagen.flow_from_directory(train_path,
                                          target_size=(224,224),
                                          batch_size=32,
                                          class_mode='categorical',
                                          subset='training')

  test_dataset = train_datagen.flow_from_directory(test_path,
                                        target_size=(224,224),
                                        batch_size=32,
                                        class_mode='categorical',
                                        subset='validation')
  
  return train_dataset,test_dataset