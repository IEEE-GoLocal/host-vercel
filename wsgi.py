from app import app

# start the flask app, allow remote connections 
if __name__ == '__main__':
    app.run(debug=True)