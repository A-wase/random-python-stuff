import streamlit as st

st.set_page_config(initial_sidebar_state="expanded")
st.sidebar.title("Siderbar Title")
page = st.sidebar.radio("Navigation", ["Page 1", "Page 2"])

if page == "Page 1":
    st.title("Data Dashboard - Page 1") # Create a title
    st.header("This is a header!")
    st.write("Hello, World!") # Create text
    st.divider()
    st.image("images/smilecat.jpg", caption="This is a cutiepatootie!", use_container_width=True)
    st.divider()
    st.write("This is a random paragraph of text. You currently reading words on a page. These words, which you are reading, are made up of words. Words, words, words and more words! What are sentances if not words persevering?")

elif page == "Page 2":
    st.title("Welcome to Page 2")
    st.write("This page has a graph!")

    import pandas as pd
    # Create a simple DataFrame
    data = {
        'Name': ['Spongebob', 'Patrick', 'Squidward', 'Sandy'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
