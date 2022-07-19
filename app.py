from flask import Flask

#create flask app- instantiate
app= Flask(__name__)
app.config['SECRET_KEY'] = 'gibberish'
app.config['SQLALCHEMY_DATBASE_URI']= 'sqlite:///data.db'


from routes import *

#app is run
if __name__ == '__main__':
    app.run(debug=True)