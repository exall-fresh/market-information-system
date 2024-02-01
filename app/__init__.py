from flask import Flask
from .home import home
from .auth import auth
from .admin import admin
from .seller import seller
from .scout import scout

# our mysql database packages

# blueprint of the application created!

def create_app():

	app = Flask(__name__) # instance of our app
	
	app.config['SECRET_KEY'] = "gaza ontime"
	app.config["UPLOAD_FOLDER"] = "project/static/images/uploads"
 
    # register our blueprints

	app.register_blueprint(home,url_prefix="/") # home page routes
	app.register_blueprint(auth, url_prefix="/") # auth routes
	app.register_blueprint(admin, url_prefix='/') # admin routes
	app.register_blueprint(seller, url_prefix='/') # sellers routes
	app.register_blueprint(scout, url_prefix='/') # scout routes
 
	return app

