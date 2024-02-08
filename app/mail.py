from flask import Blueprint, current_app, render_template, redirect, request, flash, url_for
from app.db import get_db


bp = Blueprint('mail', __name__, url_prefix='/')


@bp.route("/", methods=['GET'])
def index():
    search = request.args.get('search')
    db, c = get_db()

    if search is None:    
        c.execute(
            'SELECT * FROM email'
        )
    else:
        c.execute(
            'SELECT * FROM email WHERE content like %s', 
            ('%' + search + '%',)
        )
    mails = c.fetchall()
    return render_template('mails/index.html', mails = mails)

@bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not email:
            errors.append("Email es requerido")
        
        if not subject:
            errors.append("Asunto es requerido")
        
        if not content:
            errors.append("Contenido es requerido")
        
        if len(errors) == 0:
            send(email, subject, content)
            db, c = get_db()
            c.execute(
                'INSERT INTO email(email, subject, content) VALUES (%s, %s, %s)',
                (email, subject, content)
            )
            db.commit()
            return redirect(url_for('mail.index'))

        else:
            for error in errors:
                flash(error)
        
    return render_template('mails/create.html')

from email.message import EmailMessage
import ssl
import smtplib
import os

def send(to, subject, content):
    sender_email = 'caninodaniel92@gmail.com'
    password_email = os.environ.get('PASSWORD_KEY')
    

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = to
    em['Subject'] = subject
    em.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(sender_email, password_email )
        smtp.sendmail(sender_email, to, em.as_string() )

