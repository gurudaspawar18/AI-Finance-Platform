from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle


descriptions = [
    "pizza", "burger", "restaurant", "lunch", "dinner", "groceries", "food",
    "uber", "bus", "taxi", "petrol", "fuel", "train", "transport",
    "amazon", "clothes", "shoes", "headphones", "shopping", "shirt",
    "movie", "cinema", "gaming", "netflix", "entertainment",
    "college fees", "books", "notebook", "stationery", "course", "education"
]


categories = [
    "Food", "Food", "Food", "Food", "Food", "Food", "Food",
    "Transport", "Transport", "Transport", "Transport", "Transport", "Transport", "Transport",
    "Shopping", "Shopping", "Shopping", "Shopping", "Shopping", "Shopping",
    "Entertainment", "Entertainment", "Entertainment", "Entertainment", "Entertainment",
    "Education", "Education", "Education", "Education", "Education", "Education"
]


model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])


model.fit(descriptions, categories)


with open("expense_category_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("AI expense category model trained successfully!")