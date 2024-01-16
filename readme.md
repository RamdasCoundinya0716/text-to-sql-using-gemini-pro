# Text to SQL using Gemini Pro and Streamlit

# This image shows how the project flow happens.

![Flow Diagram](flow.png)

This project demonstrates the conversion of English questions to SQL queries using the Gemini Pro model through a Streamlit web application. The SQL queries are executed on a SQLite database.

## Prerequisites

- Python version >= 3.9 installed
- [Streamlit](https://docs.streamlit.io/1.5.3/getting_started/installation.html)
- [Google Generative AI](https://pypi.org/project/google-generativeai/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup (Running the app locally)

1. Clone the repository:

   ```bash
   git clone https://github.com/RamdasCoundinya0716/text-to-sql-using-gemini-pro.git
   ```

2. Navigate to the project folder:

   ```bash
   cd text-to-sql-using-gemini-pro
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   # Or
   .\venv\Scripts\activate    # For Windows
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file and set your Gemini API key:

   ```env
   GEMINI_API_KEY=your-gemini-api-key
   ```

6. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

7. Open the provided local or network URL in your browser.

## Usage

- Enter your English query in the input field.
- Click the "Ask the question" button.
- The generated SQL query and its results will be displayed.

## Gemini Pro Model

- The Gemini Pro model is used for language generation. Make sure to configure the API key in the `.env` file.

## SQLite Database

- The SQLite database is named `student.db`.
- The `student` table schema includes columns: `name`, `class`, `section`, and `marks`.

## Data Generation

- The `sql.py` script generates records with random data(marks column to be exact) in the `student` table. You can increase or decrease number of columns based on your wish.

## Note

- Adjust the SQL queries and data generation logic based on your specific use case.

# Running the app on a docker container:
To containerize the application using Docker, follow these steps:

1. Create a Docker image:

   ```bash
   docker build -t text-to-sql-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 text-to-sql-app
   ```

3. Access the Streamlit app in a web browser:

   Open [http://localhost:8501](http://localhost:8501) in your browser.

Make sure to set your Gemini API key in the `.env` file and ensure that your SQLite database (`student.db`) is in the same directory as your Dockerfile and other project files.

Adjust the SQL queries and data generation logic based on your specific use case.
```