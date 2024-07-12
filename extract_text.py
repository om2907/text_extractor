import tkinter as tk
from tkinter import filedialog
import cv2
import pytesseract
import os

def extract_text_from_image(image_path):
    try:
        # Load the image from the specified file
        image = cv2.imread(image_path)
        
        # Check if the image was successfully loaded
        if image is None:
            print(f"Error: Unable to load image from path: {image_path}")
            return ""
        
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply some preprocessing (e.g., thresholding)
        gray_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(gray_image)
        
        return text
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    return file_path

def main():
    try:
        # Ensure Tesseract OCR is installed and accessible
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        if not os.path.isfile(tesseract_path):
            print("Error: Tesseract OCR executable not found. Please install it and set the correct path.")
            return
        
        # Set the tesseract_cmd path
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
        # Select image file using file dialog
        image_path = select_image_file()
        if not image_path:
            print("No image selected.")
            return
        
        # Extract text from the selected image
        extracted_text = extract_text_from_image(image_path)
        if extracted_text:
            print("Extracted Text:")
            print(extracted_text)
    
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
