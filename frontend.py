from rag_pipeline import answer_query, retrieve_docs, llm_model

import streamlit as st

uploaded_file=st.file_uploader("Upload PDF",
                               type="pdf",
                               accept_multiple_files=False)

user_query=st.text_area("Enter your promot:",height=150,placeholder="Ask Anything!")

ask_question=st.button("Ask Medical Chatbot")

if ask_question:

  if uploaded_file:
      st.chat_message("user").write(user_query)

      #Rag  Pipeline
      retrieved_docs=retrieve_docs(user_query)
      response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
      #fixed_response = "Hi, this is a fixed response!"
      st.chat_message("AI Lawyer").write(response)

  else:
     
      st.error("Kindly upload a valid PDF file first!")
      
   