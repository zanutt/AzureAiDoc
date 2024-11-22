# Credit Card Analyzer

> This project is a study project utilizing Azure AI to analyze an image and determine if it depicts a 'valid' credit card based on the image itself. A function to truly validate the card has not been implemented.

---

## 📖 Intro

This project has been developed to analyze credit card images for study purposes. It utilizes technologies such as Python to create functions, along with some resources from Azure AI. The project has been structured with a focus on good practices in organization and modularity to ensure easy maintenance and scalability if needed.

---

## 📦 Installation and Execution

### Prerequisites

Make sure you have the following dependencies installed in your environment:

`Python` 3.8 or higher.
`pip` package manager.

### Installation Steps

Clone this repository:

```bash
   git clone https://github.com/zanutt/AzureAiDoc.git
```

Navigate to the project directory:

```bash
cd AzureAiDoc/src
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Configure the .env file with the required environment variables.

### Running the Application

1. Start the application:
   on the src folder
   streamlit run app.py

2. Access the system in your browser or follow the instructions displayed in the terminal.

---

## 🗂 Project Structure

Below is the main structure of the project to facilitate navigation:

```plaintext
src/
├── .env                 # Environment configuration file
├── app.py               # Main application file
├── requirements.txt     # Project dependencies
├── services/            # Directory containing service logic modules
│   └── ...              # Specific service files
├── utils/               # Directory with utility functions
│   └── ...              # Specific utility files
```

---

## 🔍 Example of Usage

After installation and execution, the project provides the following main features:

When you start the application, it redirects you to the Streamlit app page, where it requests a JPEG, PNG, or PDF file. If you upload a valid credit card image file, the application sends this file to Azure Blob Storage. After that, the app sends the URL of the uploaded image to Azure's Document Analyzer, which performs an OCR analysis of the image and returns a JSON containing the credit card information if it is valid. The app then displays on the screen whether the card is valid or not, along with some additional card details.

## You're all set! Access the application locally and explore the available features. If you need more information or have any questions, feel free to contact me.
