# Portfolio Website Frontend

This is the frontend part of the portfolio website project built using React. Below are the instructions to set up and run the application.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd portfolio-website/frontend
   ```

2. **Install dependencies**:
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Run the application**:
   Start the development server with:
   ```bash
   npm start
   ```

   The application will be available at `http://localhost:3000`.

## Project Structure

- `src/`: Contains all the source code for the React application.
  - `App.js`: Main component that renders the layout.
  - `components/`: Contains reusable components.
    - `Header.js`: Renders the header of the website.
    - `ProjectList.js`: Fetches and displays the list of projects.
    - `Footer.js`: Renders the footer of the website.
  - `data/`: Contains data files.
    - `projects.js`: Exports an array of project objects.
  - `index.js`: Entry point of the React application.

- `public/`: Contains static files.
  - `index.html`: Main HTML file for the React application.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.