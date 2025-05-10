import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-indigo-500 to-purple-600 flex items-center justify-center">
      <div className="text-center text-white p-10">
        <h1 className="text-5xl font-bold mb-6">Welcome to ProjectHive 🧠</h1>
        <p className="text-xl mb-8">AI-powered Project Idea Generator for CS Engineers</p>
        <div className="flex justify-center space-x-4">
          <Link to="/signup" className="bg-white text-indigo-600 px-6 py-2 rounded-full font-semibold hover:bg-gray-200">Signup</Link>
          <Link to="/login" className="border border-white px-6 py-2 rounded-full hover:bg-white hover:text-indigo-600">Login</Link>
        </div>
      </div>
    </div>
  );
}

export default Home;