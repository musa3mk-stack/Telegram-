import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_dir, 'index.html')

if __name__ == '__main__':
    # Render yana bukatar port ya tashi ta dynamic environment
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
