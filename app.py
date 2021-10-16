from flask import Flask, render_template, request,redirect
import smtplib
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('sender mail', 'password')
        subject = "Hello Buddy Good Evening!"
        body = "Hey! If you recieve this mail your code works fine."
        msg = f"Subject:{subject}\n\n{body}"
        server.sendmail(
        'Sender mail',
        email,
        msg
         )
        server.quit
        return redirect('/mailsent')
    
    else:
        return render_template('index.html')
        
@app.route('/mailsent')
def sentmail():
    return '<h1>Mail Sent sucessfully</h1>'

if __name__ =="__main__":
    app.run(debug=True)