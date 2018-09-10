from flask import Flask, session, redirect, url_for, escape, request, render_template

from notification import send_push_message

app = Flask(__name__)
app.secret_key = "/btPL/w79Wy21NYAkzXIa8U57Cc+z9DYRm8wH0OAwOxLJhJroaMFhF1i4K0Ng3Dk/IZOpo5j2IvsEbVw0vAegcdM4TtRGK9q6Ep8ow8jFyATacx1GgL9QKwlr83KSvgdMtH3Ecsvq+OKlPIvtoUvLAFWZedGqDXZ/ZrTMX70gaU="
# app.config.update(SERVER_NAME="0.0.0.0:80")

@app.route("/")
def index():
    if 'logged_in' in session:
        return redirect(url_for('push'))
        
    return render_template('index.html')

@app.route("/push")
def push():
    if not 'logged_in' in session:
        return redirect(url_for('index'))
    return render_template('push.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        if request.form['password'] == "password":
            session['logged_in'] = True
            return redirect(url_for('push'))
        else:
            return render_template('index.html', error="Incorrect password. Please try again.")

@app.route("/logout")
def logout():
    del session['logged_in']
    return redirect(url_for('index'))

@app.route("/send_notification", methods=['POST'])
def send_notification():
    send_push_message("ExponentPushToken[0vWyuUGUjqenh4J7_OI1oe]", "This is a test", None)


@app.route("/register", methods=['POST'])
def register():
    print(request.json)