# EmailClassifier
Automation for industries: Streamline employee email management with artificial intelligence.

This project classifies emails using a pre-trained machine learning model. It uses a Flask backend to handle email classification and a Streamlit frontend to allow users to interact with the system.

## Features

- **Email Classification**: Classify emails based on their subject and body.
- **User Interface**: A simple Streamlit frontend for interacting with the backend.
- **Pre-trained Model**: The backend uses a pre-trained model to classify emails into categories.

## Installation

### 1. Clone the Repository

```bash

# Step 1: Clone the repository to your local machine
# This command will download the repository from GitHub to your local machine.
git clone https://github.com/yourusername/email-classifier.git

# Step 2: Navigate into the project directory
# This moves you into the root project directory where the backend and frontend folders are located.
cd email-classifier

# Step 3: Backend Installation
# Navigate to the backend directory and install required dependencies
cd backend
pip install -r requirements.txt  # Installs dependencies for the Flask backend

# Step 4: Frontend Installation
# Navigate to the frontend directory and install required dependencies
cd ../frontend
pip install -r requirements.txt  # Installs dependencies for Streamlit frontend

# Step 5: Run the Backend (Flask)
# Now, return to the backend directory and run the Flask server
cd ../backend
python app.py  # Starts the Flask server on http://localhost:5000

# Step 6: Run the Frontend (Streamlit)
# Return to the frontend directory and run the Streamlit app
cd ../frontend
streamlit run streamlit_app.py  # Starts the Streamlit interface on http://localhost:8501
