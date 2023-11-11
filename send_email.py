from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Load SMTP email server details from environment variables
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = os.environ.get('SMTP_PORT', 587)
SMTP_USERNAME = os.environ.get('SMTP_USERNAME', 'hannahsooahlee2004@gmail.com')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', 'PASSWORD')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL', 'hannahsooahlee2004@gmail.com')
RECEIVER_EMAIL = os.environ.get('RECEIVER_EMAIL', 'sales@coomiexpress.com')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create a message
        subject = 'New Contact Form Submission'
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}', 'plain'))

        try:
            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            server.quit()
            return 'Message sent successfully!'
        except Exception as e:
            return f'An error occurred: {str(e)}'


if __name__ == '__main__':
    app.run(debug=True)
