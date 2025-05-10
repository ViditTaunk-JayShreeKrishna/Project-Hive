import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';

function ProjectDetails() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem('selectedProjectDetails'));
    if (data) {
      setTitle(data.title);
      setDescription(data.description);
    }
  }, []);

  return (
    <div className="p-8 max-w-4xl mx-auto bg-gradient-to-r from-purple-50 via-indigo-50 to-pink-50 rounded-xl shadow-lg border border-gray-300 transition-transform hover:scale-105 hover:shadow-xl">
      {/* Main Title with decorative underline */}
      <h2 className="text-4xl font-extrabold mb-6 text-indigo-700 tracking-wide border-b-4 border-indigo-300 pb-2">
        {title}
      </h2>

      <ReactMarkdown
        components={{
          // Section headers with colorful accents
          h2: ({ node, ...props }) => (
            <h2 className="text-3xl font-semibold mb-4 text-purple-800 relative pl-4">
              <span className="absolute left-0 top-1/2 transform -translate-y-1/2 w-3 h-3 bg-indigo-500 rounded-full"></span>
              {props.children}
            </h2>
          ),
          // Styled paragraphs
          p: ({ node, ...props }) => (
            <p className="mb-4 text-gray-700 leading-relaxed text-lg" {...props} />
          ),
          // Custom list items with icons and subtle hover
          li: ({ node, ...props }) => (
            <li className="mb-2 flex items-start pl-4 hover:bg-indigo-100 p-2 rounded transition-all transition-duration-300">
              <svg className="w-5 h-5 mt-1 mr-2 text-indigo-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <circle cx="10" cy="10" r="6" />
              </svg>
              <div className="text-gray-800">{props.children}</div>
            </li>
          ),
        }}
      >
        {description}
      </ReactMarkdown>
    </div>
  );
}

export default ProjectDetails;