from flask import Flask, render_template, request, redirect, session
import sqlite3
import pickle
import os

from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from sklearn.linear_model import LinearRegression


# -----------------------------------
# FLASK SETUP
# -----------------------------------

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("FLASK_SECRET_KEY")


# -----------------------------------
# LOAD AI CATEGORY MODEL
# -----------------------------------

with open("expense_category_model.pkl", "rb") as model_file:
    category_model = pickle.load(model_file)


# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------

def get_db_connection():
    connection = sqlite3.connect("finance.db")
    connection.row_factory = sqlite3.Row
    return connection


# -----------------------------------
# LOGIN REQUIRED FUNCTION
# -----------------------------------

def login_required():
    if "user_id" not in session:
        return False
    return True


# -----------------------------------
# HOME PAGE
# -----------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------
# REGISTER
# -----------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        # Input validation
        if username == "":
            return "Username cannot be empty."

        if password == "":
            return "Password cannot be empty."

        if len(username) < 3:
            return "Username must contain at least 3 characters."

        if len(password) < 6:
            return "Password must contain at least 6 characters."

        connection = get_db_connection()

        existing_user = connection.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        if existing_user:
            connection.close()
            return "Username already exists."

        hashed_password = generate_password_hash(password)

        connection.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, hashed_password)
        )

        connection.commit()
        connection.close()

        return redirect("/login")

    return render_template("register.html")


# -----------------------------------
# LOGIN
# -----------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        if username == "" or password == "":
            return "Username and password are required."

        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect("/dashboard")

        return "Invalid username or password."

    return render_template("login.html")


# -----------------------------------
# LOGOUT
# -----------------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# -----------------------------------
# ADD EXPENSE
# -----------------------------------

@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():

    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        amount_text = request.form["amount"].strip()
        description = request.form["description"].strip()
        date = request.form["date"].strip()

        # -----------------------------------
        # INPUT VALIDATION
        # -----------------------------------

        if amount_text == "":
            return "Amount cannot be empty."

        if description == "":
            return "Description cannot be empty."

        if date == "":
            return "Date cannot be empty."

        # Convert amount into number
        try:
            amount = float(amount_text)
        except ValueError:
            return "Amount must be a valid number."

        # Check amount
        if amount <= 0:
            return "Amount must be greater than 0."

        # -----------------------------------
        # AI CATEGORY PREDICTION
        # -----------------------------------

        predicted_category = category_model.predict(
            [description]
        )[0]

        # -----------------------------------
        # SAVE EXPENSE
        # -----------------------------------

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO expenses
            (amount, category, description, date, user_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                amount,
                predicted_category,
                description,
                date,
                session["user_id"]
            )
        )

        connection.commit()
        connection.close()

        return redirect("/expenses")

    return render_template("add_expense.html")


# -----------------------------------
# EXPENSE HISTORY
# -----------------------------------

@app.route("/expenses")
def expenses():

    if not login_required():
        return redirect("/login")

    connection = get_db_connection()

    expenses = connection.execute(
        """
        SELECT *
        FROM expenses
        WHERE user_id = ?
        ORDER BY date DESC
        """,
        (session["user_id"],)
    ).fetchall()

    connection.close()

    return render_template(
        "expenses.html",
        expenses=expenses
    )


# -----------------------------------
# DELETE EXPENSE
# -----------------------------------

@app.route("/delete-expense/<int:id>")
def delete_expense(id):

    if not login_required():
        return redirect("/login")

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        AND user_id = ?
        """,
        (id, session["user_id"])
    )

    connection.commit()
    connection.close()

    return redirect("/expenses")


# -----------------------------------
# EDIT EXPENSE
# -----------------------------------

@app.route("/edit-expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    if not login_required():
        return redirect("/login")

    connection = get_db_connection()

    expense = connection.execute(
        """
        SELECT *
        FROM expenses
        WHERE id = ?
        AND user_id = ?
        """,
        (id, session["user_id"])
    ).fetchone()

    if expense is None:
        connection.close()
        return "Expense not found."

    if request.method == "POST":

        amount_text = request.form["amount"].strip()
        description = request.form["description"].strip()
        date = request.form["date"].strip()

        # -----------------------------------
        # INPUT VALIDATION
        # -----------------------------------

        if amount_text == "":
            connection.close()
            return "Amount cannot be empty."

        if description == "":
            connection.close()
            return "Description cannot be empty."

        if date == "":
            connection.close()
            return "Date cannot be empty."

        try:
            amount = float(amount_text)
        except ValueError:
            connection.close()
            return "Amount must be a valid number."

        if amount <= 0:
            connection.close()
            return "Amount must be greater than 0."

        # -----------------------------------
        # AI CATEGORY PREDICTION
        # -----------------------------------

        predicted_category = category_model.predict(
            [description]
        )[0]

        # -----------------------------------
        # UPDATE EXPENSE
        # -----------------------------------

        connection.execute(
            """
            UPDATE expenses
            SET amount = ?,
                category = ?,
                description = ?,
                date = ?
            WHERE id = ?
            AND user_id = ?
            """,
            (
                amount,
                predicted_category,
                description,
                date,
                id,
                session["user_id"]
            )
        )

        connection.commit()
        connection.close()

        return redirect("/expenses")

    connection.close()

    return render_template(
        "edit_expense.html",
        expense=expense
    )


# -----------------------------------
# DASHBOARD
# -----------------------------------

@app.route("/dashboard")
def dashboard():

    if not login_required():
        return redirect("/login")

    connection = get_db_connection()

    user_id = session["user_id"]

    # -----------------------------------
    # SUMMARY
    # -----------------------------------

    total_expenses = connection.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()[0]

    total_transactions = connection.execute(
        """
        SELECT COUNT(*)
        FROM expenses
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()[0]

    average_expense = connection.execute(
        """
        SELECT COALESCE(AVG(amount), 0)
        FROM expenses
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()[0]

    # -----------------------------------
    # HIGHEST EXPENSE
    # -----------------------------------

    highest_expense = connection.execute(
        """
        SELECT *
        FROM expenses
        WHERE user_id = ?
        ORDER BY amount DESC
        LIMIT 1
        """,
        (user_id,)
    ).fetchone()

    # -----------------------------------
    # CATEGORY DATA
    # -----------------------------------

    category_data = connection.execute(
        """
        SELECT category, SUM(amount) AS total
        FROM expenses
        WHERE user_id = ?
        GROUP BY category
        """,
        (user_id,)
    ).fetchall()

    categories = [
        row["category"]
        for row in category_data
    ]

    category_amounts = [
        row["total"]
        for row in category_data
    ]

    # -----------------------------------
    # MONTHLY DATA
    # -----------------------------------

    monthly_data = connection.execute(
        """
        SELECT
            strftime('%Y-%m', date) AS month,
            SUM(amount) AS total
        FROM expenses
        WHERE user_id = ?
        GROUP BY month
        ORDER BY month
        """,
        (user_id,)
    ).fetchall()

    months = [
        row["month"]
        for row in monthly_data
    ]

    monthly_amounts = [
        row["total"]
        for row in monthly_data
    ]

    # -----------------------------------
    # AI SPENDING INSIGHT
    # -----------------------------------

    if total_expenses == 0:

        ai_insight = (
            "Start adding expenses to receive "
            "personalized spending insights."
        )

    elif highest_expense:

        ai_insight = (
            f"Your highest recorded expense is "
            f"₹{highest_expense['amount']:.2f} "
            f"for {highest_expense['description']}."
        )

    else:

        ai_insight = (
            "Keep tracking your expenses to "
            "understand your spending habits."
        )

    # -----------------------------------
    # BUDGET RECOMMENDATION
    # -----------------------------------

    if average_expense > 0:

        recommended_budget = total_expenses * 1.10

        budget_message = (
            f"Based on your current spending, "
            f"a simple monthly budget estimate is "
            f"₹{recommended_budget:.2f}."
        )

    else:

        budget_message = (
            "Add more expenses to generate a "
            "budget recommendation."
        )

    # -----------------------------------
    # ANOMALY DETECTION
    # -----------------------------------

    if highest_expense and highest_expense["amount"] > average_expense * 2:

        anomaly_message = (
            f"An unusually high expense of "
            f"₹{highest_expense['amount']:.2f} "
            f"was detected."
        )

    else:

        anomaly_message = (
            "No major spending anomaly detected."
        )

    # -----------------------------------
    # MACHINE LEARNING PREDICTION
    # -----------------------------------

    prediction_months = []
    prediction_amounts = []

    if len(monthly_amounts) >= 2:

        X = [[i + 1] for i in range(len(monthly_amounts))]
        y = monthly_amounts

        model = LinearRegression()

        model.fit(X, y)

        next_month_number = len(monthly_amounts) + 1

        predicted_amount = model.predict(
            [[next_month_number]]
        )[0]

        predicted_amount = max(0, predicted_amount)

        prediction_months = months + ["Next Month"]

        prediction_amounts = (
            monthly_amounts +
            [predicted_amount]
        )

        prediction_message = (
            f"Based on your historical spending trend, "
            f"next month's estimated spending is "
            f"₹{predicted_amount:.2f}."
        )

    elif len(monthly_amounts) == 1:

        prediction_message = (
            "Add expenses from at least one more "
            "month to generate a spending prediction."
        )

        prediction_months = months
        prediction_amounts = monthly_amounts

    else:

        prediction_message = (
            "Add expenses from at least two different "
            "months to generate a spending prediction."
        )

    connection.close()

    return render_template(
        "dashboard.html",

        total_expenses=total_expenses,
        total_transactions=total_transactions,
        average_expense=average_expense,

        categories=categories,
        category_amounts=category_amounts,

        months=months,
        monthly_amounts=monthly_amounts,

        ai_insight=ai_insight,
        budget_message=budget_message,
        anomaly_message=anomaly_message,

        prediction_months=prediction_months,
        prediction_amounts=prediction_amounts,
        prediction_message=prediction_message
    )


# -----------------------------------
# RUN APPLICATION
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)