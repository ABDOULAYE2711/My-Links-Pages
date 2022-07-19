import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('bd.png'))

st.header('ABDOULAYE BADJI')

st.info('Data analyst, créateur de contenu et passionné de la data.')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/channel/UCZ_Sor5J6415zV8k3hNlk6Q', 'ABDOULAYE BADJI YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/Badji2711', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/abdoulaye-badji-a24697a0//', 'Follow me on LinkedIn', icon_size)
st_button('facebook', 'https://www.facebook.com/abdoulaye.badji.779', 'Follow me on Facebook', icon_size)
