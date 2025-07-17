# Interior Design Website

This is a Flask-based web application for an interior design service, inspired by Decorilla.

## Live Demo

The live version of this application is deployed on Render:

[**Visit the Live Site**](https://interior-design-website.onrender.com)

## Features

- **Portfolio Management**: Dynamic portfolio display with filtering
- **Admin Dashboard**: Content management for portfolio, FAQs, and services
- **User Authentication**: Registration, login, and profile management
- **Interactive Elements**: Quizzes, consultations, and reviews
- **Responsive Design**: Mobile-friendly interface

## Admin Access

- URL: [https://interior-design-website.onrender.com/admin](https://interior-design-website.onrender.com/admin)
- Default credentials: admin / admin123

## Local Development

To run this project locally:

1. Clone the repository:
```
git clone https://github.com/Abhii-04/Interior-Design-Website.git
cd Interior-Design-Website
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Set up the database and admin user:
```
python setup_admin.py
```

5. Start the Flask development server:
```
python run_app.py
```

6. Open your browser to: `http://localhost:5000`

## Repository

The source code is available on GitHub: [Abhii-04/Interior-Design-Website](https://github.com/Abhii-04/Interior-Design-Website)