from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, LoginManager
import logging.config
from app import app
from users import *
from User import *
from blogs import *
from system import *

app = Flask(__name__)

# ################
# Welcome page
# ################
@app.route('/')
def main():
    return render_template('welcome.html')
  
# ################
# authentication  
# ################
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = loginUser(login, password)

    # check if user actually exists
    if not user: 
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    userClass = User(user['name'], user['login'], user['role'])
    login_user(userClass, remember=remember)
    return redirect(url_for('profile'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    user = getUserByLogin(request.form.get('login'))
    # if this returns a user, then the email already exists in database
    if user:    
        flash('Login  already exists')
        return redirect(url_for('signup'))

    # create new user with the form data
    createUserFromForm(request.form)

    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))

# ################
# Admin
# ################
@app.route('/admin')
@login_required
def showUsers():
    users = getAllUsers()
    return render_template('users.html', users = users)

@app.route('/system/<command>')
@login_required
def system(command):
    result = execute(command)
    return render_template('system.html', result = result, command = command)

# ################
# blogs
# ################
@app.route('/showblogs')
@login_required
def showblogs():
    blogs = getAllBlogs()
    return render_template('blogs.html', blogs = blogs)

@app.route('/addblog')
@login_required
def addblog():
        return render_template('addblog.html')
    
@app.route('/addblog', methods=['POST'])
@login_required
def addblog_post():
    createBlog(request.form)
    return redirect(url_for('showblogs'))

@app.route('/searchblogs', methods=['GET'])
@login_required
def searchblogs():
    searchparameter = request.args.get('search')
    blogs = searchAllBlogs(searchparameter)
    return render_template('blogs.html', blogs = blogs)

@app.route('/updateblog', methods=['GET'])
@login_required
def updateblog():
    blog = getBlogById(request.args.get('id'))
    return render_template('updateblog.html', blog = blog)

@app.route('/updateblog', methods=['POST'])
@login_required
def updateblog_post():
    blog = updateBlog(request.form)
    return redirect(url_for('showblogs'))

@app.route('/deleteblog', methods=['GET'])
@login_required
def deleteblog():
    deleteBlog(request.args.get('id'))
    return redirect(url_for('showblogs'))


# ################
# api 
# ################
@app.route('/api')
def usersAPI():
    users = getAllUsers()
    resp = jsonify(users)
    resp.status_code = 200
    return resp

# ################
# Main  
# ################
if __name__ == "__main__":
    
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    login_manager = LoginManager()
    login_manager.login_view = 'app.login'
    login_manager.init_app(app)
 
    @login_manager.user_loader
    def load_user(login):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        user = getUserByLogin(login)    
        userClass = User(user['name'], user['login'], user['role'])
        return userClass
   
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
    app.logger.info("App is started ...")
    app.run(debug=True, host='0.0.0.0')