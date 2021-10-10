import os
import streamlit as st
import requests, json

st.set_page_config(layout="wide")

st.image(os.path.join('Images','banner.png'), use_column_width  = True)
st.markdown("<h1 style='text-align: center; color: white;'>ERC721 API Explorer</h1>", unsafe_allow_html=True)
with st.expander("Configuration Option"):

    st.write("**Assets** .")
    st.write("**Owner** can be used to to get NFT from specific addres")


endpoint = st.sidebar.selectbox("Endpoints", ["Assets", "Events", "Rarity"])
st.write(f"ERC721 API Explorer - {endpoint}")
st.sidebar.subheader("Filters")
collection = st.sidebar.text_input("Collections")
owner = st.sidebar.text_input("Owner")

if endpoint == 'Assets':
    params = {
        'limit': 2
    }
    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner

    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)


    response = r.json()
    for asset in response['assets']:
        if asset['name']:
            st.write(asset['name'])
        else:
            st.write(f"{asset['collection']['name']} #{asset['token_id']}")
        if asset['image_url']:
            if asset['image_url'].endswith('mp4'):
                st.video(asset['image_url'])
            else:
                st.image(asset['image_url'])


    # r = requests.get("https://api.opensea.io/api/v1/assets", params=params)
    # st.write(r.json())