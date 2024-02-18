import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import imutils

# Function to crop brain contour
def crop_brain_contour(image, plot=False):
    # Convert the image to grayscale, and blur it slightly
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    
    # crop new image out of the original image using the four extreme points (left, right, top, bottom)
    new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]]            
    
    return new_image

# Function to preprocess image for prediction
def preprocess_image_for_prediction(img_path, image_size):
    # Read the image using OpenCV
    image = cv2.imread(img_path)
    # Crop the brain contour
    image = crop_brain_contour(image, plot=False)
    # Resize the image to match the model input shape
    image = cv2.resize(image, dsize=image_size, interpolation=cv2.INTER_CUBIC)
    # Normalize values
    image = image / 255.
    # Convert image to numpy array
    img_array = np.expand_dims(image, axis=0)  # Add batch dimension
    return img_array

# Function to make predictions
def predict_image(img_path, image_size):
    img_array = preprocess_image_for_prediction(img_path, image_size)  # Preprocess the image
    prediction = model.predict(img_array)  # Make prediction
    return prediction

# Streamlit App
def main():
    st.title("Brain Tumor Detection App")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", width=300)

        # Make prediction button
        if st.button("Make Prediction"):
            # Preprocess and make prediction
            image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
            image = crop_brain_contour(image, plot=False)
            image = cv2.resize(image, dsize=(IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_CUBIC)
            image = image / 255.
            img_array = np.expand_dims(image, axis=0)
            prediction = model.predict(img_array)

            # Output the prediction
            if prediction[0][0] > 0.5:
                st.error("Brain tumor detected")
            else:
                st.success("No brain tumor detected")

    else:
        st.info("Please upload an image.")

if __name__ == "__main__":
    # Load the pre-trained model
    model = load_model('brain_tumor_detection/final_model.h5')

    # Set image dimensions
    IMG_WIDTH = 240
    IMG_HEIGHT = 240

    main()
