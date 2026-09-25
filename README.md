# AI-Powered Personal Finance & Expense Intelligence Platform

A full-stack personal finance web application that helps users track expenses, analyze spending patterns, receive automated financial insights, and predict future spending using machine learning.

## Live Demo

**[Live Application](https://ai-finance-platform-b0yp.onrender.com)**

**[GitHub Repository](https://github.com/gurudaspawar18/AI-Finance-Platform)**

---

## Overview

The **AI-Powered Personal Finance & Expense Intelligence Platform** is a Flask-based web application designed to help users manage and understand their personal expenses.

The application allows users to create accounts, securely log in, add and manage expenses, automatically categorize expenses using machine learning, visualize spending patterns, detect unusual expenses, receive budget recommendations, and estimate future spending.

The project combines:

* Full-stack web development
* Database management
* Authentication and security
* Machine learning
* Data visualization
* Automated financial insights

---

## Key Highlights

* Secure user registration and login
* User-specific expense management
* Machine learning-based expense categorization
* Spending trend analysis
* Future spending prediction
* Spending anomaly detection
* Interactive dashboard with Chart.js
* Deployed live using Render and Gunicorn

---

## Features

### User Authentication

* User registration
* User login and logout
* Password hashing
* Session-based authentication
* Protected application routes
* User-specific expense data

### Expense Management

* Add expenses
* View expense history
* Edit expenses
* Delete expenses
* Expense validation
* Automatic expense categorization

### Dashboard Analytics

The dashboard provides:

* Total spending
* Total number of transactions
* Average expense
* Highest expense
* Category-wise spending
* Monthly spending
* Spending charts
* Automated spending insights
* Budget recommendations
* Spending anomaly detection
* Future spending prediction

### Machine Learning

The application uses machine learning for:

* Automatic expense category prediction
* Spending prediction using Linear Regression
* Expense text classification using TF-IDF and Logistic Regression
* Basic spending anomaly detection

### Data Visualization

Chart.js is used to visualize:

* Category-wise expenses
* Monthly spending
* Spending prediction

---

## Technology Stack

### Backend

* Python
* Flask

### Database

* SQLite

### Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Linear Regression

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Security

* Werkzeug password hashing
* Flask sessions
* Environment variables
* Protected routes
* Parameterized SQL queries

### Deployment

* GitHub
* Render
* Gunicorn

---

## Machine Learning

### Expense Categorization

The application predicts an expense category based on the expense description.

Example:

```text
Description: Lunch at restaurant
Predicted Category: Food
```

The classification system uses:

* `TfidfVectorizer`
* `LogisticRegression`

The trained model is stored in:

```text
expense_category_model.pkl
```

### Spending Prediction

The application uses **Linear Regression** to analyze historical monthly spending and estimate the next month's spending.

The prediction is displayed on the dashboard together with historical spending data.

### Anomaly Detection

The application compares a user's highest expense with their average expense to identify potentially unusual spending.

---

## Application Workflow

```text
User
  |
  v
Register / Login
  |
  v
Dashboard
  |
  +----> Add Expense
  |          |
  |          v
  |    ML Category Prediction
  |          |
  |          v
  |    Save Expense
  |
  +----> Expense History
  |          |
  |          +----> Edit
  |          |
  |          +----> Delete
  |
  +----> Spending Analytics
  |
  +----> Automated Insights
  |
  +----> Budget Recommendation
  |
  +----> Anomaly Detection
  |
  +----> Spending Prediction
```

---

## Application Architecture

```text
Frontend
HTML + CSS + JavaScript
        |
        v
Flask Application
        |
        +----------------+
        |                |
        v                v
   SQLite Database   ML Models
                         |
                         +---- TF-IDF
                         |
                         +---- Logistic Regression
                         |
                         +---- Linear Regression
        |
        v
Dashboard Analytics
```

---

## Project Structure

```text
AI-Finance-Platform/
│
├── app.py
├── database.py
├── train_model.py
├── expense_category_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── expenses.html
    ├── add_expense.html
    └── edit_expense.html
```

> `finance.db`, `.env`, and the virtual environment are excluded from GitHub using `.gitignore`.

---

## Database

The application uses SQLite to store user and expense information.

### Users Table

Stores:

* User ID
* Username
* Hashed password

### Expenses Table

Stores:

* Expense ID
* Amount
* Category
* Description
* Date
* User ID

Each user's expenses are associated with their account.

---

## Security

The application includes several security measures:

* Passwords are stored using secure hashing.
* User sessions are used for authentication.
* Protected routes require login.
* SQL queries use parameterized values.
* User-specific queries prevent users from accessing other users' expenses.
* Sensitive configuration is stored using environment variables.
* `.env` is excluded from GitHub.

---

## Environment Variables

Create a `.env` file locally:

```text
FLASK_SECRET_KEY=your-secret-key-here
```

Do not commit the `.env` file to GitHub.

A template is provided in:

```text
.env.example
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gurudaspawar18/AI-Finance-Platform.git
```

### 2. Open the Project

```bash
cd AI-Finance-Platform
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file:

```text
FLASK_SECRET_KEY=your-secret-key-here
```

### 7. Run the Application

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

---

## Deployment

The application is deployed using:

* GitHub for source code
* Render for hosting
* Gunicorn as the production WSGI server

Production start command:

```bash
gunicorn app:app
```

### Live Application

**[Open the Live Application](https://ai-finance-platform-b0yp.onrender.com)**

---

## Database Initialization

The application automatically creates the required database tables when the Flask application starts.

This allows the application to initialize correctly when deployed on a new hosting environment.

---

## Testing

The deployed application was tested for:

* User registration
* User login
* User logout
* Database initialization
* Adding expenses
* Viewing expense history
* Editing expenses
* Deleting expenses
* User-specific expense data
* Dashboard functionality
* Machine learning expense categorization
* Spending analytics

---

## Current Limitations

* The application currently uses SQLite.
* Spending prediction is based on available historical spending data.
* Anomaly detection uses a basic statistical comparison.
* Automated insights are rule-based rather than generated by a large language model.
* The application is intended as a portfolio project and not as professional financial advice.

---

## Future Improvements

Possible future improvements include:

* PostgreSQL database
* Cloud-based database
* Advanced financial forecasting
* Improved anomaly detection
* More advanced financial insights
* Financial goal tracking
* Monthly budget management
* Expense reminders
* Export reports as PDF/CSV

---

## Project Status

**Status: Completed and Deployed**

The application is currently available as a live web application.

### Live Demo

**https://ai-finance-platform-b0yp.onrender.com**

### Source Code

**[GitHub Repository](https://github.com/gurudaspawar18/AI-Finance-Platform)**

---

## Author

**Gurudas Pawar**

Computer Engineering Student

* **GitHub:** [gurudaspawar18](https://github.com/gurudaspawar18)
* **LinkedIn:** [Gurudas Pawar](https://www.linkedin.com/in/gurudas-pawar-605019333/)

