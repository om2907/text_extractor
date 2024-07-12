import streamlit as st
import cv2
import pytesseract
import tempfile
import os

# Set the path to the Tesseract executable (if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        # Load the image from the specified file
        image = cv2.imread(image_path)

        # Check if the image was successfully loaded
        if image is None:
            st.error(f"Error: Unable to load image from path: {image_path}")
            return ""

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply some preprocessing (e.g., thresholding)
        gray_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(gray_image)

        return text

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""

def main():
    # Set the tesseract_cmd path if necessary
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    st.title("Extract Text from Image")

    # File uploader component
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])

    if uploaded_file is not None:
        # Temporarily save the uploaded file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())

        st.image(temp_file.name, caption="Uploaded Image", use_column_width=True)

        # Extract text from the uploaded image
        extracted_text = extract_text_from_image(temp_file.name)
        if extracted_text:
            st.subheader("Extracted Text:")
            st.write(extracted_text)

        # Remove the temporary file
        os.remove(temp_file.name)

if __name__ == "__main__":
    main()
