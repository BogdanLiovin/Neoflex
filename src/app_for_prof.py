from flask import Flask, render_template, request, redirect, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для сессий

# Функция хэширования пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Проверка авторизации пользователя
def is_authenticated():
    return 'username' in session


# Вход пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = hash_password(password)

        conn = sqlite3.connect('my_db.db')
        c = conn.cursor()
        c.execute("SELECT * FROM profile WHERE email = ? AND password = ?",
                  (email, hashed_password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[0]  # Сохранение имени пользователя в сессии
            return redirect('/')
        else:
            return "Неверное имя пользователя или пароль"

    return render_template('login.html')

# Главная страница
@app.route('/')
def index():
    if is_authenticated():
        return "Привет, {session['username']}! Вы вошли в систему."
    else:
        return "Вы не вошли в систему. <a href='/login'>Войти</a>"

# Выход пользователя
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)