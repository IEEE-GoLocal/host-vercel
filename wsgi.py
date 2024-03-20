from app import app

# start the flask app, allow remote connections 
if __name__ == 'main':
    app.run(debug=True)