# 🐝 Project Hive — AI-Powered Project Recommendation & Planning Platform

**Project Hive** is a full-stack web platform built with **Django (Python)** for the backend and **React.js** for the frontend. It offers students smart, personalized project ideas based on their selected **skills** and **interests**, and uses the **Gemini (Google AI) API** to generate detailed, structured project plans.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [How it Works](#-how-it-works)
- [API Reference](#-api-reference)
- [Deployment](#-deployment)
- [Author](#-author)

---

## 🚀 Features

- 🔐 User Authentication — Sign up / Login / Password Reset
- ✅ Skill Selection — Choose from a curated list of 30+ skills & interests
- 🤖 AI Suggestions — ML model recommends tailored project titles
- 📄 Project Plan Generator — Uses Gemini AI to generate detailed plans
- ☁️ Cloud-ready — Easily deploy to Render (backend) and Netlify (frontend)

---

## 🛠 Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Frontend     | React.js, Tailwind CSS              |
| Backend      | Django, Django REST Framework       |
| AI / ML      | Gemini API (via Google GenAI), Sklearn |
| Database     | SQLite (development)                |
| Model        | TF-IDF + Cosine Similarity          |
| Deployment   | Render (backend), Netlify (frontend)|
| Auth         | JWT-based authentication            |

---

## 🧪 Setup & Installation

### 🐍 Backend Setup

```bash
cd backend
python -m venv env
env\Scripts\activate    # For Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
