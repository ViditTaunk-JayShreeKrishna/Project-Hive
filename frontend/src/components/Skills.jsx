// src/pages/Skills.jsx  
import React, { useState } from 'react';  
import axios from 'axios';  
import { useNavigate } from 'react-router-dom';  

const skillOptions = [  
  "Python", "Java", "C++", "HTML", "CSS", "JavaScript", "ReactJS", "NodeJS", "Django", "Flask",  
  "SQL", "MongoDB", "Git", "Docker", "Kubernetes", "AWS", "Azure", "GCP", "TensorFlow", "PyTorch",  
  "Pandas", "NumPy", "OpenCV", "Blockchain", "Firebase", "Linux", "CI/CD", "Matplotlib", "Scikit-Learn",  
  "Flutter", "Android", "iOS"  
];  

const interestOptions = [  
  "Web Development", "App Development", "Machine Learning", "Deep Learning", "Computer Vision",  
  "Cybersecurity", "Cloud Computing", "Game Development", "IoT", "Data Science", "Big Data",  
  "AR/VR", "DevOps", "AI Ethics", "Blockchain"  
];  

function Skills() {  
  const navigate = useNavigate();  
  const [formData, setFormData] = useState({  
    skills: [],  
    interests: [],  
    difficulty: 'Medium'  
  });  

  const handleCheckboxChange = (e, field) => {  
    const { checked, value } = e.target;  
    setFormData(prev => ({  
      ...prev,  
      [field]: checked ? [...prev[field], value] : prev[field].filter(v => v !== value),  
    }));  
  };  

  const handleSubmit = async (e) => {  
    e.preventDefault();  
    const token = localStorage.getItem('accessToken');  
    if (!token) {  
      alert('You must be logged in to get suggestions!');  
      return;  
    }  
    try {  
      const res = await axios.post(  
        'http://127.0.0.1:8000/api/suggest/',  
        formData,  
        {  
          headers: { Authorization: `Bearer ${token}` },  
        }  
      );  
      localStorage.setItem('suggestedProjects', JSON.stringify(res.data.projects));  
      localStorage.setItem('skills', JSON.stringify(formData.skills));  
      navigate('/suggestions');  
    } catch (err) {  
      console.error('💥 API ERROR:', err.response?.data || err.message);  
      alert('Failed to get suggestions!');  
    }  
  };  

  return (  
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-6">  
      {/* Card container */}  
      <div className="w-full max-w-4xl bg-white rounded-xl shadow-lg p-8 border border-gray-200 hover:scale-105 transition-transform duration-300">  
        {/* Header */}  
        <h2 className="text-3xl font-bold text-center mb-6 border-b-4 border-indigo-300 pb-2 text-indigo-700">  
          Select Skills & Interests  
        </h2>  
        {/* Form */}  
        <form onSubmit={handleSubmit} className="space-y-6">  
          
          {/* Skills */}  
          <div>  
            <h4 className="text-lg font-semibold mb-3 text-indigo-600">Skills:</h4>  
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">  
              {skillOptions.map((skill, i) => (  
                <label key={i} className="flex items-center bg-gray-100 p-2 rounded-lg cursor-pointer hover:bg-gray-200 transition">  
                  <input  
                    type="checkbox"  
                    value={skill}  
                    onChange={(e) => handleCheckboxChange(e, 'skills')}  
                    className="mr-2 accent-indigo-600"  
                  />  
                  <span className="text-sm">{skill}</span>  
                </label>  
              ))}  
            </div>  
          </div>  

          {/* Interests */}  
          <div>  
            <h4 className="text-lg font-semibold mb-3 text-indigo-600">Interests:</h4>  
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">  
              {interestOptions.map((interest, i) => (  
                <label key={i} className="flex items-center bg-gray-100 p-2 rounded-lg cursor-pointer hover:bg-gray-200 transition">  
                  <input  
                    type="checkbox"  
                    value={interest}  
                    onChange={(e) => handleCheckboxChange(e, 'interests')}  
                    className="mr-2 accent-indigo-600"  
                  />  
                  <span className="text-sm">{interest}</span>  
                </label>  
              ))}
              </div>
            </div>
  
            {/* Difficulty Selector */}
            <div>
              <label className="block mb-2 font-semibold text-indigo-600">Difficulty Level:</label>
              <select
                value={formData.difficulty}
                onChange={(e) => setFormData({ ...formData, difficulty: e.target.value })}
                className="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-400 transition"
              >
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>
            </div>
  
            {/* Submit Button */}
            <button
              type="submit"
              className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition-colors duration-200"
            >
              Get Suggestions
            </button>
          </form>
        </div>
      </div>
    );
  }
  
  export default Skills;