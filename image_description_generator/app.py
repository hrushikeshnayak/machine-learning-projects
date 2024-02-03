import streamlit as st
from dotenv import load_dotenv
import os
import PIL.Image
import google.generativeai as genai
load_dotenv()

prompt = '''Please provide a thorough description of the image, including the objects, people, animals, scenery, colors, textures, and any notable details. Pay attention to the composition, lighting, and overall mood conveyed by the image. Describe any actions or interactions happening within the scene, as well as any emotions or atmosphere you perceive. Additionally, discuss any cultural or historical context that may be relevant to understanding the image. Your description should be detailed and vivid, enabling someone who hasn't seen the image to visualize it as accurately as possible.'''

def analyze_image(path):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open(path)
    response = model.generate_content([prompt , img], stream=True)
    response.resolve()
    pred_res = response.text
    
    return pred_res

def main():
    st.title("Image Description App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Analyzing...")

        description = analyze_image(uploaded_file)
        st.write("Description:")
        st.write(description)

if __name__ == "__main__":
    main()

