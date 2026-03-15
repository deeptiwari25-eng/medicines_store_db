import sys
import os
import traceback
from flask import Flask

# Add current directory to path so imports work relative to this file
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app import create_app
    app = create_app()
except Exception:
    # If the app crashes during startup, create a fallback app to show the error
    app = Flask(__name__)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return f'<h1>Start-up Error</h1><pre>{traceback.format_exc()}</pre>', 500

if __name__ == '__main__':
    app.run()
