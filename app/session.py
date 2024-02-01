
# flask package to help in sessions

from flask import session

# function to start our session, get the user id and the username

def start_session(id, username): 
    
    session['loggedin'] =True # give the session a name
    session['id'] = id # session id
    session['username'] = username # session username

# function to end the session

def end_session():
    session.pop('loggedin', None) # remove the session name
    session.pop('id', None) # remove the session id
    session.pop('username', None) # remove the session username
    
# function to verify if a session is established

def verify_session():
    
    if session.get('loggedin')==True:
    
        return True

def session_data():

	return session.get('id')