import os
import json
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash # our security library

# our custom modules
from .db_conn import db_conn
from .session import start_session, end_session, verify_session
# end of our custom modules


# lets get our database objects
cursor, connection = db_conn() # the cursor and the database connection objects

auth = Blueprint('auth',__name__)

# method to render the login page
@auth.route('/login')
def login():
    return render_template('auth/login.html')    
# end of the method to render the login page

# method to authenticate the input credintials
@auth.route('/login-auth', methods=['POST'])
def login_auth():
    if request.method=="POST":
        # when everything goes on ok
        try:
            # now lets receive the form data
            data = request.form
            username = data.get('username') # input username
            password = data.get('password') # input password

            # now lets read the database credintials in relation to the entered credintials
            user = cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            # now the details from the database
            user_id = user[0]
            db_username = user[1]
            db_password = user[4]
            user_role = user[5]
            # if a user is found
            if user:
                # compare the input and the db_password
                if check_password_hash(db_password, password):
                     # if admin
                    if user_role == 1:
                        start_session(user_id,username)
                        return redirect('/admin/dashboard')
                    
                    # else if seller
                    elif user_role==2:
                        start_session(user_id,username)
                        return redirect('/seller/dashboard')
                    
                    # else if scout
                    elif user_role==3:
                        start_session(user_id,username)
                        return redirect('/scout/dashboard')
                    
                else:
                    flash(category='error', message='Wrong credintials')
                    return redirect('/login')
            else:
                flash(category='error', message='Wrong credintials')
                return redirect('/login')
        
        # when an error is encurred
        except Exception as e:
            print(e)
            flash(category='error', message='Login failed check your credintials')
            return redirect('/login')

# end of the method to authenticate the input credintials

# method to render the register page

@auth.route('/register')
def register():
    return render_template('auth/register.html')

# end of the method to render the register page
    
# method to authenticate the registration details

@auth.route('/register-auth', methods=['POST'])
def register_auth():

    if request.method=="POST":
        data = request.form

        # lets have variables for us to validate 

        db_username = []
        db_phone = []
        db_email = []

        username = data.get('username')
        phone= data.get('phone')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        role = data.get('role')

        # now lets see if any record matches the entered details

        user = cursor.execute('SELECT * FROM users')
        user = cursor.fetchall()

        # loop through all records
        for user_data in user: 
            # loop through all columns
            for col in user_data:
                db_username.append(user_data[1]) # append to db_usernames list
                db_phone.append(user_data[2]) # app the the db_phones list
                db_email.append(user_data[3]) # append to the db_email list

        if username in db_username:
               
               flash('username already taken up', category='error')
               return redirect('/register')
               
        elif phone in db_phone:
               flash('phone number already exists',category='error')
               return redirect('/register')
        elif email in db_email:
            flash('email already exists', category='error')
            return redirect('/register')
        # check if the 2 passwords match
        elif password1!=password2:
            flash('the passwords do not match', category='error')
            return redirect('/register')
            
        # if nothing is wrong let us go ahead to create the account
        encrypted_password = generate_password_hash(password1, method="scrypt")
        # values to be inserted
        VALUES = (username,phone, email,role, encrypted_password )
        insert_query = "INSERT INTO users(username,phone,email,role,password) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(insert_query, VALUES) # execute the query
        connection.commit()
        flash('Account Created', category='success')
        print('account created')
        return redirect('/register') 
        
    return redirect('/register')

# logout

@auth.route('/logout')
def logout():
    end_session() # we end the session
    flash('login again to access the system', category='error')
    return redirect('/login')