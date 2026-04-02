import os
import random
from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

def generate_secret_santa(participants_dict):
    names = list(participants_dict.keys())
    random.shuffle(names)
    
    assignments = {}
    for i in range(len(names)):
        giver = names[i]
        receiver = names[(i + 1) % len(names)]
        assignments[giver] = receiver
        
    return assignments

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/draw", methods=["POST"])
def draw_and_send():
    participants = request.get_json()
    
    if not participants or len(participants) < 3:
        return jsonify({"error": "Wymaganych jest przynajmniej 3 uczestników."}), 400

    assignments = generate_secret_santa(participants)
    
    emails_sent = 0
    errors = []

    for giver, receiver in assignments.items():
        email = participants[giver]

        msg = Message(
            subject='🎄 Bożonarodzeniowe losowanie!', 
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )

        msg.html = f"""
        <h3>Cześć {giver}! 🎅</h3>
        <p>Skrypt wyciągnął ze słoiczka karteczkę z imieniem: <strong>{receiver}</strong>.</p>
        <p>Życzę Ci dużo kreatywności, pomysłowości i radości z wybierania prezentu.</p>
        <br>
        <p><em>Wesołych Świąt!</em></p>
        """

        try:
            mail.send(msg)
            emails_sent += 1
        except Exception as e:
            errors.append({"user": giver, "error": str(e)})

    response = {
        "message": "Losowanie zakończone.",
        "emails_sent": emails_sent,
        "errors": errors
    }
    
    status_code = 200 if not errors else 207
    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(debug=True)