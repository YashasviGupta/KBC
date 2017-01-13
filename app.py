from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run()
