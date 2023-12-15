from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from PIL import Image
from keras.preprocessing.image import load_img
from keras.preprocessing import image
import numpy as np
import os

def loadModel():
    model_path = 'resnet_model_35epoch.h5'
    model = load_model(model_path)
    return model

def trainData():
    train=ImageDataGenerator()
                                
    train_dataset=train.flow_from_directory('M_app/dataset/train')

    return train_dataset
 
def preprocess():
    # 'dataset/input' klasöründeki tüm dosya yollarını al
    image_folder = 'uploads'
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder)]

    # Giriş verilerini oluştur
    input_images = []
    for img_path in image_paths:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale to [0, 1]
        input_images.append(img_array)

    input_images = np.vstack(input_images)  # Birleştirerek tek bir matris oluştur
    return input_images

def predict():
    # Tahmin yap
    predictions = loadModel().predict(preprocess())

    # Tahmin sonuçlarını incele
    class_indices = trainData().class_indices
    predicted_classes = np.argmax(predictions, axis=1)

    for i, predicted_class_index in enumerate(predicted_classes):
        predicted_class_name = [k for k, v in class_indices.items() if v == predicted_class_index][0]
        return predicted_class_name


