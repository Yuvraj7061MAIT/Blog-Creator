import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLaMA 2 model
def get_llama_response(input_text, no_words, blog_style):

   ## LLaMA 2 model calling
   llm = CTransformers(
       model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
       model_type='llama',
       config={'max_new_tokens': 256, 'temperature': 0.01}
   )

   ## Prompt Template
   prompt = PromptTemplate(
       input_variables=["style", "text", "n_words"],
       template="""
Write a blog for {style} job profile for a topic {text} within {n_words} words.
"""
   )

   ## Generate the response from LLaMA 2 model
   response = llm(prompt.format(style=blog_style, text=input_text, n_words=no_words))
   return response


st.set_page_config(
   page_title="Generate Blogs",
   page_icon="@",
   layout='centered',  # Corrected spelling
   initial_sidebar_state='collapsed'
)

st.header("Generate Blogs")

input_text = st.text_input("Enter the blog topic")

## Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
   no_words = st.number_input('No. of Words', min_value=1)  # Use number_input for numerical input
with col2:
   blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'))

if st.button("Generate"):  # Use st.button directly for button
   st.write(get_llama_response(input_text, no_words, blog_style))
