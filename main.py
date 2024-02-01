from app import create_app

app = create_app() # call the class method from _ _ init __.py
# register our blueprints

if __name__ =='__main__':
    
    app.run(debug=True)