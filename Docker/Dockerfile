FROM python:3.9-slim

# Set the working directory inside the container where your application code will be copied:
WORKDIR /app

# Copy the requirements.txt file to the container and install the dependencies:
# Copy the file root-directory-of-this-project/Docker/requirements.txt to /app
Copy ./Docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container's working directory:
# Copy from root-directory-of-this-project/src to /app
COPY ./src .

# Expose the port that your FastAPI application will be running on:
# Make sure this port matches the port set in your FastAPI application's uvicorn.run command.
EXPOSE 8000

# Start the FastAPI application using the uvicorn command:
# Make sure the main:app matches the name of your FastAPI application file and the variable that holds the FastAPI() instance.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]