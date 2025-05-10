import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import StyledCard from '../components/StyledCard';

function Login() {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/login/', formData);
      localStorage.setItem('accessToken', res.data.access);
      setMessage('Login successful!');
      setTimeout(() => navigate('/skills'), 1000);
    } catch (err) {
      setMessage('Login failed. Check credentials.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <StyledCard>
        <h2 className="text-3xl font-extrabold mb-6 text-center text-indigo-700 border-b-4 border-indigo-300 pb-2">Login to ProjectHive</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            name="username"
            placeholder="Username"
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-lg font-semibold transition duration-200"
          >
            Login
          </button>
        </form>
        <p className="mt-3 text-center text-sm text-gray-600">
          Forgot password?{' '}
          <Link to="/forgot-password" className="text-indigo-600 hover:underline font-medium">
            Reset here
          </Link>
        </p>
        {message && <p className="mt-4 text-center text-sm text-red-600">{message}</p>}
      </StyledCard>
    </div>
  );
}

export default Login;