import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/api/projects/')
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the projects!', error);
        setError('Could not fetch projects. Is the backend server running?');
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>SOC Project Management</h1>
      </header>
      <main>
        <h2>Projects</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <ul>
          {projects.length > 0 ? (
            projects.map(project => (
              <li key={project.id}>
                <h3>{project.name}</h3>
                <p>{project.description}</p>
              </li>
            ))
          ) : (
            !error && <p>No projects found. Create one via the backend.</p>
          )}
        </ul>
      </main>
    </div>
  );
}

export default App;
