import streamlit as st
from langchain_helper import generate_restaurant

st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Select a Cuisine", ("Indian","Chinese","Mexican","Italian","Arabic","American"))

# def generate_restaurant(cuisine):
#     return {'cuisine': 'Indian', 'res_name': 'Tandoori Nights', 'res_menu': 'Chicken Tikka Masala, Palak Paneer, Tandoori Chicken, Saag Aloo, Garlic Naan, Raita, Vegetable Biryani, Lamb Korma'}

if cuisine:
    response=generate_restaurant(cuisine)
    st.header(response['res_name'].strip())
    men_items=response['res_menu'].strip().split(',')
    st.write("^^Menu^^")
    for item in men_items:
        st.write('-',item)