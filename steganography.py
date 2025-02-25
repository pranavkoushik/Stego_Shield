import streamlit as st
import numpy as np
from PIL import Image
import io
from utils import encode_message, decode_message
from styles import apply_styles

def main():
    apply_styles()
    
    st.title("🔒 Steganography Tool")
    st.subheader("Hide Secret Messages in Images")
    
    tab1, tab2 = st.tabs(["Hide Message", "Extract Message"])
    
    with tab1:
        st.subheader("Hide a Secret Message")
        
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'], key='hide')
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Original Image", use_column_width=True)
            
            message = st.text_area("Enter your secret message:")
            password = st.text_input("Enter password for encryption:", type="password")
            
            if st.button("Hide Message"):
                if not message or not password:
                    st.error("Please enter both message and password!")
                    return
                
                try:
                    # Convert image to numpy array
                    img_array = np.array(image)
                    
                    # Encode the message
                    encoded_image = encode_message(img_array, message, password)
                    
                    # Convert back to PIL Image
                    encoded_pil = Image.fromarray(encoded_image)
                    
                    # Create download button
                    buf = io.BytesIO()
                    encoded_pil.save(buf, format="PNG")
                    st.download_button(
                        label="Download Encoded Image",
                        data=buf.getvalue(),
                        file_name="encoded_image.png",
                        mime="image/png"
                    )
                    st.success("Message hidden successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
    
    with tab2:
        st.subheader("Extract Hidden Message")
        
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'], key='extract')
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image with Hidden Message", use_column_width=True)
            
            password = st.text_input("Enter password for decryption:", type="password", key='decrypt')
            
            if st.button("Extract Message"):
                if not password:
                    st.error("Please enter the password!")
                    return
                
                try:
                    # Convert image to numpy array
                    img_array = np.array(image)
                    
                    # Decode the message
                    decoded_message = decode_message(img_array, password)
                    
                    if decoded_message:
                        st.success("Message extracted successfully!")
                        st.code(decoded_message)
                    else:
                        st.error("Invalid password or no message found!")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
