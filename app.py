#Daniel Kareti
########
#Check the age of the user to make sure it is valid 
#(i.e., not in the future)
########

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')

    birthday_str = request.form.get('birthday')

    try:
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        valid = True
        today = datetime.today()

        if(birthday > today):
            valid = False
            message = "Your birthday cannot be in the future!"
        else:
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            message = f"Hello {name}, your birthday is valid! As of today you are {age} years old."
    except ValueError:
        valid = False
        message = "You didn't select a day! INVALID date format"
    return render_template()