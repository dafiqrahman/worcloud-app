import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image



st.title("Wordclouds Generator")

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    #select column
    df = pd.read_excel(uploaded_file)
    column = st.selectbox('Which column should be used?', df.columns)
    #upload image 
    image_file = st.file_uploader("Choose a PNG file")
    if image_file is not None:
        image = Image.open(image_file)
        #generate wordcloud
        from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
        text = " ".join(review for review in df[column])
        stopwords = set(STOPWORDS)
        #input new stopwords
        new_stopwords = st.text_input("Add new stopwords (separate by comma)")
        if new_stopwords is not None:
            new_stopwords = new_stopwords.split(",")
            print(new_stopwords)
            for word in new_stopwords:
                stopwords.add(word)
        #remove stopwords
        text = " ".join([word for word in text.split() if word not in stopwords])
        image_coloring = np.array(image)
        #print(image_coloring.shape)
        image_colors = ImageColorGenerator(image_coloring)
        wc = WordCloud(background_color="white", mask=image_coloring,
             random_state=42)
        wc.generate(text)
        image_colors = ImageColorGenerator(image_coloring)
        fig = plt.figure(figsize=(10,10))
        plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig) 
    