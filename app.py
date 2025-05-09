from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '🎉 Hello from ShareSafely App deployed via Azure!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Azure provides PORT as an environment variable
    app.run(debug=True, host='0.0.0.0', port=port)

