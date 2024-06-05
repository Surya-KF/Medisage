import streamlit as st
import pytesseract
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from PIL import Image


def web_writer(a):
    format_of_data = ".txt"
    file_name = a + format_of_data
    with open(file_name, 'r') as f:
        var = f.read()
    return var


example = web_writer("example")
key = "###########################"
chatllm = ChatOpenAI(openai_api_key=key, temperature=0.8, model='gpt-3.5-turbo')


def ans(inp, lang):
    response = chatllm([
        SystemMessage(
            content=f"Act as a professional pharmacist with 30 years of experience and tell all the details about {inp}"
                    f"if it is a medicine, if it is a disease tell about the curing medicines for this disease in {lang} Language"
                    f" take this as details to be provided "
                    f"{example}"
                    f"and fill the information and give the output in the same format"),
    ])
    content = response.content
    return content


# Centering logo using HTML
st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://www.freepnglogos.com/uploads/medicine-logo-png-1.png" alt="Logo" width="100">
    </div>
    """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>MEDICINE WEB</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>ALL THE DETAILS FOR YOUR MEDICINES</h1>", unsafe_allow_html=True)

st.write("\n\n\n")
st.markdown("<h3 style='text-align: center;'>Language</h1>", unsafe_allow_html=True)
option = st.selectbox('',
    ('English', 'Hindi',  'Nepali')
)
st.markdown("<h3 style='text-align: center;'>Upload your medicine photos</h3>", unsafe_allow_html=True)
file = st.file_uploader("", type=["jpg", "png"])
st.markdown("<h3 style='text-align: center;'>OR</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Name of your medicine or disease</h3>", unsafe_allow_html=True)
user_input = st.text_input("")


def get_text(image_data):
    t = pytesseract.image_to_string(image_data)
    return t


if file:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    text = get_text(image)
    with st.spinner(f'The details is being loaded for {text}'):
        x = ans(text, option)
        st.subheader(text)
        st.write(x)

if user_input:
    text = user_input
    with st.spinner(f'The details is being loaded for {text}'):
        x = ans(text, option)
        st.subheader(text)
        st.write(x)
