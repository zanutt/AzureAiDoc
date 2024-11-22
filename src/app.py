import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title("Upload File DIO - Challenge 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Choose a png, pdf or jpeg file", type = ["png", "pdf", "jpeg"])
    

    if uploaded_file is not None:
        file_name = uploaded_file.name        
        blob_url = upload_blob(uploaded_file, file_name)
        
        if blob_url:
            st.write(f"File {file_name} was sent successfully to Azure Blob Storage.")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Error sending file {file_name} to Azure Blob Storage.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Image sent", use_container_width=True)
    st.write("Validation Result: ")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Valid Credit Card</h1>", unsafe_allow_html=True)
        st.write(f"Credit card Holder: {credit_card_info['card_name']}")
        st.write(f"Bank: {credit_card_info['bank_name']}")
        st.write(f"Expiry date: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Invalid Credit Card</h1>", unsafe_allow_html=True)
        st.write("This is not a valid credit card.")


if __name__ == "__main__":
    configure_interface()