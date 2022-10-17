from flask import Flask
import os

# Configuration

app = Flask(__name__)

# Routes

@app.route('/')
def root():
    return "Welcome to my demo app!"

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9412))
    
    app.run(port=port)