# Portfolio Website

This is a portfolio website project that showcases various projects and skills. The project is structured into two main parts: the backend and the frontend.

## Project Structure

```
portfolio-website
├── backend
│   ├── main.py          # Entry point for the FastAPI backend application
│   ├── requirements.txt  # Lists dependencies for the backend
│   └── README.md        # Documentation for the backend
├── frontend
│   ├── src
│   │   ├── App.js       # Main component of the React application
│   │   ├── components    # Contains reusable components
│   │   │   ├── Header.js # Header component
│   │   │   ├── ProjectList.js # Component to display projects
│   │   │   └── Footer.js # Footer component
│   │   ├── data
│   │   │   └── projects.js # Contains project data
│   │   └── index.js     # Entry point for the React application
│   ├── public
│   │   └── index.html    # Main HTML file for the React application
│   ├── package.json      # Configuration file for npm
│   └── README.md         # Documentation for the frontend
└── README.md             # Documentation for the entire project
```

## Getting Started

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```
4. Access the API at `http://localhost:8000`.

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```
4. Access the application at `http://localhost:3000`.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.