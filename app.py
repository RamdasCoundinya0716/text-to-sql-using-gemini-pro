from dotenv import load_dotenv
load_dotenv() # load all env variables
import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configuring API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Loading Gemini model and providing query as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    # '''
    #     prompt says how the model should behave 
    #     question is the text which should be converted into sql query
    # '''
    return response.text

# Getting result by passing sql query
def read_query(query, db):
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM student ;
    \nExample 2 - Tell me all the student studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM student 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title = "Text to SQL")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print("Generated SQL query:", response)
    result = read_query(response, "student.db")
    st.subheader("The Response is")
    for row in result:
        st.header(row)

