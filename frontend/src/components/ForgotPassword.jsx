// src/pages/ForgotPassword.jsx
import React, { useState } from 'react';
import axios from 'axios';
import StyledCard from '../components/StyledCard';
import BASE_URL from '../config';


function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${BASE_URL}/reset_password/`, { email });
      setMessage('Password reset link sent. Check your inbox!');
    } catch (err) {
      setMessage('Failed to send reset link.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <StyledCard>
        <h2 className="text-2xl font-bold mb-4 text-center text-indigo-600 border-b-4 border-indigo-300 pb-2">Forgot Your Password?</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="email"
            placeholder="Enter your email"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 transition"
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg font-semibold transition duration-200"
          >
            Send Reset Link
          </button>
        </form>
        {message && (
          <p className="mt-4 text-center text-sm text-gray-600">{message}</p>
        )}
      </StyledCard>
    </div>
  );
}

export default ForgotPassword;