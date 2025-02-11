import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dados de exemplo
emails = ["Problema técnico", "Oferta especial de marketing", 
          "Atualização financeira"]
categorias = ["Suporte Técnico", "Marketing", "Financeiro"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

model = LogisticRegression()
model.fit(X, categorias)

# Salvando o modelo e o vetorizador
joblib.dump(model, "classifier.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
