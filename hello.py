from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '29d00ec05209b0baba6c9677bf43ed94'
posts = [
    {
     'author': 'Chashi Islam',
     'title' : 'Post 1',
     'content' : 'First content',
     'date_posted': 'Oct 17, 2022'
     },
    {
     'author': 'Kazi Misbah',
     'title' : 'Post 2',
     'content' : 'Second content',
     'date_posted': 'Oct 18, 2022'
     }
    ]
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['Get', 'Post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)
