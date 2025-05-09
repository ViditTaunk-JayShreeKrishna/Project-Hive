from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class SkillForm(forms.Form):
    SKILLS_CHOICES = [
    ('C', 'C'),
    ('C++', 'C++'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Go', 'Go'),
    ('Kotlin', 'Kotlin'),
    ('Swift', 'Swift'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript', 'JavaScript'),
    ('ReactJS', 'ReactJS'),
    ('NodeJS', 'NodeJS'),
    ('Angular', 'Angular'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('Flutter', 'Flutter'),
    ('React Native', 'React Native'),
    ('Android Native', 'Android Native'),
    ('iOS Swift', 'iOS Swift'),
    ('Machine Learning', 'Machine Learning'),
    ('Deep Learning', 'Deep Learning'),
    ('NLP', 'Natural Language Processing (NLP)'),
    ('Computer Vision', 'Computer Vision'),
    ('Generative AI', 'Generative AI'),
    ('LLMs', 'Large Language Models (LLMs)'),
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Network Security', 'Network Security'),
    ('Cryptography', 'Cryptography'),
    ('Cyber Forensics', 'Cyber Forensics'),
    ('Data Analysis', 'Data Analysis'),
    ('Data Visualization', 'Data Visualization'),
    ('Big Data', 'Big Data'),
    ('Docker', 'Docker'),
    ('Kubernetes', 'Kubernetes'),
    ('CI/CD', 'CI/CD Pipelines'),
    ('AWS', 'AWS'),
    ('Azure', 'Azure'),
    ('GCP', 'Google Cloud Platform'),
    ('Ethereum', 'Ethereum Development'),
    ('Solidity', 'Solidity Smart Contracts'),
    ('Hyperledger', 'Hyperledger Blockchain'),
    ('IoT', 'Internet of Things (IoT)'),
    ('Arduino', 'Arduino Projects'),
    ('Raspberry Pi', 'Raspberry Pi Projects'),
    ('Embedded Systems', 'Embedded Systems Development'),
    ('MySQL', 'MySQL Database'),
    ('PostgreSQL', 'PostgreSQL Database'),
    ('MongoDB', 'MongoDB'),
    ('Firebase', 'Firebase'),
    ('Web3', 'Web3 Development'),
    ('AR/VR', 'Augmented & Virtual Reality'),
    ('Game Development', 'Game Development (Unity, Unreal)'),
    ('Automation', 'Automation Scripting'),
    ]


    INTERESTS_CHOICES = [
    ('Web Development', 'Web Development'),
    ('Mobile App Development', 'Mobile App Development'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Machine Learning', 'Machine Learning'),
    ('Data Science', 'Data Science'),
    ('Cyber Security', 'Cyber Security'),
    ('Blockchain Technology', 'Blockchain Technology'),
    ('Cloud Computing', 'Cloud Computing'),
    ('DevOps', 'DevOps Engineering'),
    ('Internet of Things', 'Internet of Things (IoT)'),
    ('Augmented/Virtual Reality', 'AR/VR Development'),
    ('Gaming', 'Gaming and Game Development'),
    ('Big Data', 'Big Data and Analytics'),
    ('Automation', 'Process Automation'),
    ('Web3', 'Web3 and Decentralized Apps'),
    ('Embedded Systems', 'Embedded System Design'),
    ('Startups/Entrepreneurship', 'Startups and Innovation'),
    ]


    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    skills = forms.MultipleChoiceField(choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple)
    interests = forms.MultipleChoiceField(choices=INTERESTS_CHOICES, widget=forms.CheckboxSelectMultiple)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, widget=forms.RadioSelect)
