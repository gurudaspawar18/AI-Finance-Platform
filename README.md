# AI-Powered Personal Finance & Expense Intelligence Platform

A full-stack personal finance management application that helps users track expenses, analyze spending patterns, automatically categorize expenses using Machine Learning, and generate spending insights and predictions.

## Overview

The AI-Powered Personal Finance & Expense Intelligence Platform is a web application built using Python and Flask.

The application allows users to create accounts, securely log in, add and manage expenses, view financial analytics, and receive automated insights based on their spending data.

Machine Learning is used for automatic expense categorization, while Linear Regression is used to estimate future monthly spending.

## Features

### User Authentication

- User registration and login
- Secure password hashing
- Session-based authentication
- Logout functionality
- User-specific expense data
- Protected application routes

### Expense Management

- Add new expenses
- Edit existing expenses
- Delete expenses
- View expense history
- Store expense amount, description, category, and date
- Automatic expense categorization

### Machine Learning Expense Categorization

The application automatically predicts an expense category based on its description.

The classification system uses:

- TF-IDF Vectorization
- Logistic Regression
- Scikit-learn

Example:

Input:

"Burger at restaurant"

Predicted Category:

"Food"

### Financial Dashboard

The dashboard provides:

- Total expenses
- Total number of transactions
- Average expense
- Spending by category
- Monthly spending
- AI-generated spending insight
- Budget recommendation
- Anomaly detection
- Future spending prediction

### Spending Analysis

The application analyzes historical expenses to identify spending patterns.

Visualizations are created using Chart.js, including:

- Spending by category
- Monthly spending
- ML spending prediction

### Anomaly Detection

The application identifies unusually high expenses by comparing individual expenses with the user's average spending.

### Spending Prediction

Linear Regression is used to estimate the next month's spending based on historical monthly expense data.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database |
| HTML | Frontend structure |
| CSS | User interface styling |
| JavaScript | Frontend functionality |
| Chart.js | Data visualization |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Expense classification |
| Linear Regression | Spending prediction |
| Werkzeug | Password hashing |
| Python-dotenv | Environment configuration |
| Git | Version control |
| GitHub | Project repository |

## Machine Learning

### Expense Categorization

The expense categorization model follows this process:

Expense Description
        |
        v
TF-IDF Vectorization
        |
        v
Logistic Regression
        |
        v
Predicted Expense Category

The trained model is stored in:

expense_category_model.pkl

### Spending Prediction

The spending prediction system follows:

Historical Monthly Expenses
        |
        v
Data Preparation
        |
        v
Linear Regression
        |
        v
Predicted Next Month Spending

## Application Architecture

User
 |
 v
Web Browser
 |
 v
HTML / CSS / JavaScript
 |
 v
Flask Application
 |
 +-------------------+
 |                   |
 v                   v
SQLite Database    ML Models
                       |
                       v
              Expense Categorization
              Spending Prediction

## Project Structure

AI-Finance-Platform/
|
├── app.py
├── train_model.py
├── finance.db
├── expense_category_model.pkl
├── README.md
├── .gitignore
├── .env
|
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add_expense.html
    ├── edit_expense.html
    └── expenses.html

## Database

The application uses SQLite to store:

- User accounts
- Password hashes
- Expense records
- User IDs associated with expenses

Each expense is associated with a specific user, allowing the application to keep financial data separated between users.

## Security

The application implements basic security practices including:

- Password hashing using Werkzeug
- Session-based authentication
- User-specific database queries
- Protected routes
- Input validation
- Environment-based Flask secret key

The Flask secret key is stored in a `.env` file instead of being directly written in the source code.

Example:

FLASK_SECRET_KEY=your-secret-key

The `.env` file should not be uploaded to GitHub.

## Installation

### Requirements

- Python 3.x
- Git
- Visual Studio Code
- Web browser

### 1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the Project

cd AI-Finance-Platform

### 3. Create a Virtual Environment

python -m venv venv

### 4. Activate the Virtual Environment

For Windows PowerShell:

venv\Scripts\Activate.ps1

### 5. Install Dependencies

pip install flask python-dotenv scikit-learn

### 6. Configure Environment Variables

Create a `.env` file in the project root:

FLASK_SECRET_KEY=your-secret-key

### 7. Run the Application

python app.py

### 8. Open the Application

http://127.0.0.1:5000

## Application Workflow

Register
   |
   v
Login
   |
   v
Add Expense
   |
   v
ML Expense Categorization
   |
   v
Store Expense
   |
   v
Dashboard
   |
   +--> Spending Analysis
   |
   +--> AI Insight
   |
   +--> Budget Recommendation
   |
   +--> Anomaly Detection
   |
   +--> Spending Prediction

## Dashboard Analytics

### Spending by Category

Displays the distribution of expenses across different categories using a pie chart.

### Monthly Spending

Displays monthly expense totals using a bar chart.

### ML Spending Prediction

Displays historical monthly spending and the estimated next month's spending.

## Testing

The application has been tested for:

- User registration
- User login
- User logout
- Password hashing
- Adding expenses
- Editing expenses
- Deleting expenses
- Expense history
- Dashboard analytics
- Automatic expense categorization
- Spending insights
- Budget recommendations
- Anomaly detection
- Spending prediction
- Input validation
- Multi-user data separation
- Protected routes

## Current Limitations

The Machine Learning expense categorization model uses a relatively small training dataset. Therefore, predictions may not always be accurate for descriptions that are significantly different from the training examples.

The spending prediction system is a basic Linear Regression implementation and is intended for project and educational purposes rather than professional financial forecasting.

The financial insights and budget recommendations are analytical features and should not be considered professional financial advice.

## Future Improvements

Possible future improvements include:

- Larger Machine Learning training dataset
- Improved expense classification
- Advanced spending prediction models
- Expense search and filtering
- CSV and PDF reports
- Recurring expense tracking
- Financial goal tracking
- Advanced budget management
- Cloud deployment
- Mobile application
- More advanced financial analytics
- Automated financial reports

## Project Status

The project is currently a functional full-stack personal finance application with:

- User authentication
- Expense management
- Machine Learning-based categorization
- Financial analytics
- AI-based insights
- Budget recommendation
- Anomaly detection
- Spending prediction
- Multi-user data separation
- Basic security and validation

## Author

Gurudas Pawar

Computer Engineering Student

GitHub: gurudaspawar18

LinkedIn: gurudas-pawar-605019333

## License

This project was developed for educational, learning, and portfolio purposes.