import os
from flask import Flask, render_template, url_for, request, \
    session, redirect, flash

from flask_mail import Mail, Message

from forms import ContactForm, csrf

mail = Mail()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'test'
csrf.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', title='6G-Студия разработки сайтов')


@app.route('/about/', methods=['POST', 'GET'])
def about():
    form = ContactForm()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['message'])
        print('-------------------------')
        print("\nData received. Now redirecting ...")
        flash("Message Received", "success")

        send_message(request.form)
        return redirect('/success')
    print(url_for('about'))
    return render_template('about.html', form=form, title='Подробнее 6G-Студия разработки сайтов')


@app.route('/success')
def success():
    return render_template('index.html')


def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender=message.get('email'),
                  recipients=['id1@gmail.com'],
                  body=message.get('message')
                  )
    mail.send(msg)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page_404.html', title='страница не найдена'), 404


if __name__ == '__main__':
    app.run()
