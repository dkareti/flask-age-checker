#Daniel Kareti
########
#Check the age of the user to make sure it is valid 
#(i.e., not in the future)
########

from flask import Flask, render_template, request
from datetime import datetime
from predict import predict_age_group

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
            age_group = None
        else:
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            age_group = predict_age_group(age)
            message = (f"Hello {name}, your birthday is valid! As of today you are {age} years old."
                       f" and you're in the '{age_group}' age group.")
    except ValueError:
        valid = False
        message = "You didn't select a day! INVALID date format"
        age_group = None
    return render_template('result.html', message=message, valid=valid, age_group = age_group)

if __name__ == "__main__":
    app.run(port=5001)