import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Set up your environment variable for Google Gemini API
os.environ['GEMINI_API_KEY'] = ''

# Configure the generative AI
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Function to get AI response
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flas')  # model name
    
    # Generating response based on input and image
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)

    return response.text

# Streamlit app settings
st.set_page_config(page_title='IMAGE CREATION')
st.header("IMAGE ANALYSIS AND CONTENT CREATION APP")

st.markdown("<h3 style='font-size: 23px;'>Developed by : Mohd Sameer Hussain</h3>", unsafe_allow_html=True)

# Input prompt
input_text = st.text_input('Input Prompt : ', key='input')

# Upload image
upload_file = st.file_uploader('Choose an Image', type=['jpg', 'jpeg', 'png'])

image = None
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Submit button to get AI response
submit = st.button('Explain brief about Image')

# When submit is clicked
if submit:
    if image is not None:
        response = get_gemini_response(input_text, image)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload an image to get a response.")

# mohdsameerhussain28@gmail.com