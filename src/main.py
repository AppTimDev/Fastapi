from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.exceptions import HTTPException

# Create an instance of FastAPI: Initialize FastAPI by creating a new instance:
app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome"
    }

@app.get("/message/{message_id}")
def get_message(message_id: str, opt: Optional[str]= None):
    return {
        "message_id": message_id,
        "opt": opt
    }

# Define a route for login: Create a route to handle the login request:
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    if credentials.username != "tim" or credentials.password != "123456":
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    return {"message": "Login successful"}

# In this example, we're using HTTP Basic Authentication for simplicity. Replace "username" and "password" with your desired login credentials. 
# You can implement more secure authentication mechanisms like OAuth or JWT as needed.
# Run the FastAPI server: Start the FastAPI server by adding the following code below all other code in the script:
# Now you can access the login endpoint by sending a POST request to http://localhost:8000/login with the provided login credentials. If the credentials match, the API will respond with a JSON message saying "Login successful". If the credentials are incorrect, the API will respond with an HTTP 401 Unauthorized status code and an error message.
# Note: Remember to customize the authentication and authorization mechanism to fit your specific requirements and security needs.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # You should be able to access your FastAPI application at http://localhost:8000
    # and testing the api at http://localhost:8000/docs