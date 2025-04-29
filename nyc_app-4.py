#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st

# Load and clean data
nyc_data = pd.read_csv('nyc-ideas.csv')
nyc_data['Type'] = nyc_data['Type'].astype(str).str.strip().str.lower()
nyc_data['Genre'] = nyc_data['Genre'].astype(str).str.strip().str.lower()

types = sorted(nyc_data['Type'].dropna().unique())

st.title("Things to do NYC")

# Type selector
selected_type = st.selectbox("Where do you want to go?", [t.capitalize() for t in types])
selected_type = selected_type.lower()

# Genre options
available_genres = sorted(
    nyc_data[nyc_data['Type'] == selected_type]['Genre'].dropna().unique()
)

if available_genres:
    selected_genre = st.selectbox(
        f"Available genres for type '{selected_type.capitalize()}':",
        [g.capitalize() for g in available_genres]
    )
    selected_genre = selected_genre.lower()

    # Filter results
    filtered = nyc_data[
        (nyc_data['Type'] == selected_type) & (nyc_data['Genre'] == selected_genre)
    ]

    if filtered.empty:
        st.warning(f"No results found for type '{selected_type}' and genre '{selected_genre}'.")
    else:
        st.success(f"Results for type '{selected_type}' and genre '{selected_genre}':")
        st.dataframe(filtered)
else:
    st.warning("No genres available for this type.")


# In[ ]:





# In[ ]:




