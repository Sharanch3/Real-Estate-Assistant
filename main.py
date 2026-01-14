import streamlit as st
from rag_utils import process_urls, generate_answer

st.set_page_config(
    page_title= "Real-Estate Assistant",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Real-Estate Assistant")
st.divider()

url1 = st.sidebar.text_input(label="URL1")
url2 = st.sidebar.text_input(label="URL2")
url3 = st.sidebar.text_input(label="URL3")

placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")


if process_url_button:
    urls = [url for url in (url1, url2, url3) if url]
    if len(urls) == 0:
        st.sidebar.warning("You must provide one url")

    else:
        for status in process_urls(urls= urls):
            placeholder.status(status)

query = placeholder.text_area("Question:")

if query:
    answer, sources = generate_answer(query)

    st.header("Answer:")
    st.write(answer)
    if sources:
        st.subheader("Sources:")
        st.write(sources)
        