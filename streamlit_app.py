import streamlit as st
import requests

st.title("Classificador de E-mails com IA")

email_subject = st.text_input("Assunto do E-mail")
email_body = st.text_area("Corpo do E-mail")

if st.button("Classificar E-mail"):
    payload = {"subject": email_subject, "body": email_body}
    try:
        response = requests.post("http://localhost:5000/classificar_email", json=payload)
        if response.status_code == 200:
            classificacao = response.json().get("classificacao")
            st.success(f"Classificação: {classificacao}")
        else:
            st.error(f"Erro: {response.json().get('error')}")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
