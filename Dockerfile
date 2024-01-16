# Pulling the base image from docker hub 
FROM python:3.9
#Setting the working directory
WORKDIR /app
#Copying the requirements.txt into the Docker image
COPY requirements.txt .
# installing the requirements on to the container
RUN pip install --no-cache-dir -r requirements.txt
# Copying rest of the files
COPY . /app
# Streamlit runs on this port, so we expose this port
EXPOSE 8501
# We run the "streamlit run app.py" on the container by using CMD command
CMD ["streamlit", "run", "app.py"]
