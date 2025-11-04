from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form['email']
    password = request.form['password']

    if email == 'faqih@gmail.com' and password == '12345':
        return redirect(url_for('home'))
    else:
        error_message = "Email atau password yang Anda masukkan salah."
        return render_template('login.html', error=error_message)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)