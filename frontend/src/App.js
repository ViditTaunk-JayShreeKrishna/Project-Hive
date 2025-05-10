import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Login from "./components/Login";
import Skills from "./components/Skills"
import Signup from "./components/Signup";
import ForgotPassword from "./components/ForgotPassword";
import ProjectDetails from "./components/ProjectDetails";
import Suggestions from "./components/Suggestions";
import PrivateRoute from "./components/PrivateRoute";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/skills" element={<Skills />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/project/:id" element={<ProjectDetails />} />
        <Route path="/suggestions" element={<PrivateRoute><Suggestions /></PrivateRoute>} />
      </Routes>
    </Router>
  );
}

export default App;
