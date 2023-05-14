# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:16:20 2023

@author: msria
"""
import streamlit as st
import openai
import urllib.request
from PIL import Image

openai.api_key="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"

def generateImages(img_description):
    img_response=openai.Image.create(
        prompt=img_description,
        n=1,
        size="512x512")
    img_url=img_response['data'][0]['url']
    urllib.request.urlretrieve(img_url,'img.png')
    img=Image.open('img.png') 
    return img
st.title("DALL E Image Generation")
image_description=st.text_input("Image Description")

if st.button("Generate Image"):
   generated_img=generateImages(image_description)
   st.image(generated_img)
#streamlit run "C:\Users\msria\anaconda3\envs\MachineLearning\DALLE Image generation.py" in Anaconda prompt