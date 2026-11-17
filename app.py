from flask import Flask, app

app = Flask(__name__) #Creates a new Flask application instance

@app.route('/') 
def home():
    return "Welcome to WebWatch the Website Vulnerability Scanner!"

if __name__ == '__main__': 
    app.run(debug=True)