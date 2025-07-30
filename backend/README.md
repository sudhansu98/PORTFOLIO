# Portfolio Website Backend

This is the backend of the portfolio website, built using FastAPI. It serves as the API for the frontend application.

## Getting Started

To set up and run the backend application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine.

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd portfolio-website/backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To start the FastAPI application, run the following command:
```
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

### API Endpoints

- `GET /`: Returns a welcome message.
- `GET /projects`: Returns a list of projects with their names and descriptions.

### License

This project is licensed under the MIT License.