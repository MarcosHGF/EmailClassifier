from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Carregar o modelo já treinado
model = joblib.load("classifier.pkl")  # Certifique-se de que classifier.pkl está no diretório correto
vectorizer = joblib.load("vectorizer.pkl")  # Carregar o vetorizador também

@app.route("/classificar_email", methods=["POST"])
def classificar_email():
    try:
        # Receber o JSON com assunto e corpo do e-mail
        data = request.get_json()
        subject = data.get("subject", "")
        body = data.get("body", "")
        
        if not subject and not body:
            return jsonify({"error": "Assunto e corpo do e-mail não podem estar vazios."}), 400

        # Combinar assunto e corpo para a análise
        texto = [f"{subject} {body}"]

        # Vetorização e classificação
        X = vectorizer.transform(texto)
        categoria = model.predict(X)[0]

        return jsonify({"classificacao": categoria})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
