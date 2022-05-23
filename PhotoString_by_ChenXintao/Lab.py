from flask import Flask
from search_bp import search_bp
from show_bp import show_bp
from upload_bp import upload_bp
from api_bp import api_bp

app=Flask(__name__)

app.register_blueprint(search_bp)
app.register_blueprint(show_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(api_bp)

if __name__=='__main__':
    app.run(debug=True)