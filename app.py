from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '🎉 Hello from ShareSafely App deployed via Azure!'

if __name__ == '__main__':
    import os
app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))

