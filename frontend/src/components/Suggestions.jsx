// src/pages/Suggestions.jsx
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Suggestions() {
  const [projects, setProjects] = useState([]);
  const [loadingProject, setLoadingProject] = useState(null);
  const navigate = useNavigate();

  // Load suggestions from localStorage on component mount
  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem('suggestedProjects') || '[]');
    setProjects(saved);
  }, []);

  // Function to handle viewing project details
  const viewDetails = async (proj) => {
    setLoadingProject(proj);
    try {
      // Get CSRF token from cookies
      const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          for (let cookie of document.cookie.split(";")) {
            const trimmed = cookie.trim();
            if (trimmed.startsWith(name + "=")) {
              cookieValue = decodeURIComponent(trimmed.slice(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      };

      const csrfToken = getCookie('csrftoken');

      // Get skills from localStorage
      const savedSkills = JSON.parse(localStorage.getItem('skills') || '[]');

      // Request project details from backend
      const response = await fetch('http://127.0.0.1:8000/api/generate-project-details/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        credentials: 'include',
        body: JSON.stringify({ title: proj, skills: savedSkills }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error fetching project details:', {
          status: response.status,
          body: errorText,
        });
        setLoadingProject(null);
        return;
      }

      const data = await response.json();
      localStorage.setItem('selectedProjectDetails', JSON.stringify(data));
      localStorage.setItem('selectedProject', proj);
      navigate(`/project/${data.id}`);
    } catch (error) {
      console.error('Fetch error:', error);
      alert('An unexpected error occurred. Check console for details.');
    }
    setLoadingProject(null);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8 flex flex-col items-center">
      <h2 className="text-3xl font-bold text-center text-indigo-700 mb-8 border-b-4 border-indigo-300 pb-2">AI-Recommended Project Ideas</h2>
      
      {projects.length > 0 ? (
        <ul className="space-y-4 w-full max-w-3xl">
          {projects.map((proj, i) => (
            <li
              key={i}
              className="flex justify-between items-center bg-white p-4 rounded-xl shadow hover:shadow-lg transition-all duration-200"
            >
              <div className="text-gray-800 font-semibold">{proj}</div>
              <button
                onClick={() => viewDetails(proj)}
                disabled={loadingProject === proj}
                className={`px-4 py-2 rounded-lg text-white font-semibold transition duration-200 ${
                  loadingProject === proj ? 'bg-gray-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700'
                }`}
              >
                {loadingProject === proj ? 'Loading...' : 'View Details'}
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-center text-gray-600 mt-12 text-lg">No suggestions found. Please fill the form first.</p>
      )}
    </div>
  );
}

export default Suggestions;