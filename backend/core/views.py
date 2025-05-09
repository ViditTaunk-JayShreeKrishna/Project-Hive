import pickle
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, SkillForm

# # Load the trained model and encoders
# with open('project_suggestion_model.pkl', 'rb') as f:
#     model, skills_mlb, interests_mlb = pickle.load(f)

# # Home Page
# def home(request):
#     return render(request, 'home.html')

# # Signup Page
# from .forms import CreateUserForm

# from django.shortcuts import render, redirect
# from .forms import CreateUserForm
# from django.contrib import messages

# def signupPage(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#         else:
#             print(form.errors)  # DEBUG: will show why form fails
#     else:
#         form = CreateUserForm()

#     context = {'form': form}
#     return render(request, 'signup.html', context)



# # Login Page
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('skills')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid Credentials'})

#     return render(request, 'login.html')

# # Skill Form Page
# def skillsPage(request):
#     form = SkillForm()

#     if request.method == 'POST':
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             skills = form.cleaned_data['skills']
#             interests = form.cleaned_data['interests']
#             difficulty = form.cleaned_data['difficulty']

#             # Save them in session for simplicity
#             request.session['skills'] = skills
#             request.session['interests'] = interests
#             request.session['difficulty'] = difficulty

#             return redirect('suggestions')

#     context = {'form': form}
#     return render(request, 'skills.html', context)

# # Suggestions Page
# from django.shortcuts import render, redirect

# import random

# from django.shortcuts import render, redirect

# from django.shortcuts import render, redirect
# import numpy as np

# def suggestionsPage(request):
#     skills = request.session.get('skills')
#     interests = request.session.get('interests')
#     difficulty = request.session.get('difficulty')

#     if not skills or not interests or not difficulty:
#         return redirect('skills')

#     # Encode user inputs
#     user_skills_encoded = skills_mlb.transform([skills])
#     user_interests_encoded = interests_mlb.transform([interests])

#     difficulty_map = {'Easy': 0, 'Medium': 1, 'Hard': 2}
#     difficulty_encoded = np.array([[difficulty_map[difficulty]]])

#     final_input = np.hstack((user_skills_encoded, user_interests_encoded, difficulty_encoded))

#     # Predict Probabilities
#     proba = model.predict_proba(final_input)

#     # Get Top 5 Indices with highest probabilities
#     top_indices = np.argsort(proba[0])[::-1][:5]

#     # Get Project Names from model classes_
#     top_projects = [model.classes_[i] for i in top_indices]

#     context = {
#         'projects': top_projects
#     }
#     return render(request, 'suggestions.html', context)



# from django.contrib.auth import logout

# def logoutPage(request):
#     logout(request)
#     return redirect('home')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import pickle
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

import os
import pandas as pd
import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Get BASE_DIR as root (where manage.py is)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import joblib
from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = 'index.html' 
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# views.py
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.middleware.csrf import get_token
@ensure_csrf_cookie
def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})



# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import openai
from django.conf import settings



import openai
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai
from django.conf import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

@csrf_exempt
def generate_project_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            skills = data.get('skills', [])

            if not title:
                return JsonResponse({'error': 'Project title is required'}, status=400)

            # 🔧 Gemini Prompt
            prompt = f"""
You are an expert project advisor. A student has selected the project: "{title}" and they have the following skills: {', '.join(skills)}.

Generate the project plan with the following structure:
1. Title
2. Problem Description
3. Proposed Solution
4. System Design (high level)
5. Technology Stack (tools/libraries they can use based on their skills)
6. Working Principle
7. Functional Requirements
8. Workflow (step-by-step how to build)

Be descriptive, clear, explanatory and use bullet points where needed. Keep it practical for a student-level project.
"""

            # 🔁 Use Gemini model
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)

            return JsonResponse({
                'id': 1,
                'title': title,
                'description': response.text  # Gemini returns text
            })

        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'GET not allowed'}, status=405)





class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Points to backend/core/
PARENT_DIR = os.path.dirname(BASE_DIR)  # Points to backend/

MODEL_PATH = os.path.join(PARENT_DIR, 'project_suggestion_model.pkl')
CSV_PATH = os.path.join(PARENT_DIR, 'project_dataset.csv')


class SuggestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            skills = data.get('skills', [])
            interests = data.get('interests', [])
            difficulty = data.get('difficulty', 'Medium')
            print("Received data:", request.data)

            input_text = ' '.join(skills + interests + [difficulty])

            # Load model and vectorizer
            tfidf, model = joblib.load(MODEL_PATH)

            # Load dataset
            df = pd.read_csv(CSV_PATH)
            df['combined_text'] = df['skills'] + ' ' + df['interests'] + ' ' + df['difficulty']

            vectors = tfidf.transform(df['combined_text'])
            input_vec = tfidf.transform([input_text])

            scores = (vectors * input_vec.T).toarray().flatten()
            top_indices = scores.argsort()[-5:][::-1]

            suggestions = df.iloc[top_indices]['project_title'].tolist()
            return Response({'projects': suggestions})

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({'error': str(e)}, status=500)

from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            # Dummy response — implement your token or real reset link logic
            # In production, you'd use Django's password reset mechanisms
            send_mail(
                subject='Password Reset Request',
                message='Click here to reset your password...',
                from_email='noreply@example.com',
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({'message': 'Reset link sent'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SignupAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'message': 'Login successful'})
        return data

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
