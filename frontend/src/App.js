import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import ProjectList from './components/ProjectList';


const App = () => {
  return (
    <div className="app">
      <Header />
      <main>
        <h2>My Projects</h2>
        <ProjectList />
      </main>
      <Footer />
    </div>
  );
};

export default App;