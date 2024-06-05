# Langchain Medicine Assistant

Langchain Medicine Assistant is a Python application that utilizes OpenAI's GPT-3.5 Turbo model to provide detailed information about medicines and diseases. It allows users to input the name of a medicine, disease, or condition and receive comprehensive descriptions about it, including active ingredients, dosage, indications, contraindications, warnings, side effects, cost, instructions for use, and manufacturer information. Additionally, the application supports multiple languages, including English, Hindi, and Nepali. It also features image recognition capabilities using pytesseract to extract text from medicine packet images.

## Features
- Provides detailed information about medicines and diseases using OpenAI's GPT-3.5 Turbo model
- Supports multiple languages: English, Hindi, and Nepali
- Extracts text from medicine packet images using pytesseract
- Displays information in a structured format including active ingredients, dosage, indications, contraindications, warnings, side effects, cost, and instructions for use

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```
3. Make sure you have an OpenAI API key and replace '#############################' in the code with your actual key.

## Usage
1. Run the `app.py` file:
    ```
    streamlit run app.py
    ```
2. Select the language (English, Hindi, Nepali).
3. Upload an image of a medicine packet or enter the name of a medicine or disease in the provided text box.
4. The application will display detailed information about the medicine or disease.

## Contributing
Contributions to Langchain Medicine Assistant are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

