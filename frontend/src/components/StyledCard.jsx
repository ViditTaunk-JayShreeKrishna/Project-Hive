// src/components/StyledCard.jsx
import React from 'react';

const StyledCard = ({ children }) => (
  <div className="bg-white p-6 rounded-xl shadow-md hover:scale-105 hover:shadow-xl transition-transform transition-shadow duration-300 w-full max-w-3xl mx-auto mb-8">
    {children}
  </div>
);

export default StyledCard;