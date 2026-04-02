# Secret Santa Generator 🎅
Automated Secret Santa drawer and emailer built with Python and Flask.

## Key Features
* **Pair Drawing:** The algorithm guarantees that no participant will draw themselves.
* **SMTP Integration:** Automated email notifications sent directly to participants with their results.
* **Dynamic UI:** Easily add or remove any number of participants through a responsive web interface.

## Tools and Technologies
* **Backend:** Python (Flask, Flask-Mail)
* **Frontend:** JavaScript, HTML5, CSS3
* **Configuration:** python-dotenv

## Quick Start

### 1. Install dependencies:
`pip install -r requirements.txt`

### 2. Configuration (.env):
Create a .env file in the project's root directory:
```
#.env file
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=twoj@email.pl
MAIL_PASSWORD=twoje-haslo
```

### 3. Run the application:
`python app.py`
The application will be available at: `http://127.0.0.1:5000`

## License
MIT

