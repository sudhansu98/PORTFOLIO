from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to my portfolio website"}

@app.get("/projects")
def get_projects():
    return [
        {"name": "Project Alpha", "description": "An innovative solution for problem A."},
        {"name": "Project Beta", "description": "A web application for managing tasks."},
        {"name": "Project Gamma", "description": "A mobile app for tracking fitness."},
        {"name": "Project Delta", "description": "An e-commerce platform for small businesses."},
        {"name": "Project Epsilon", "description": "A data visualization tool for analytics."},
    ]