from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Create a directory for storing messages if it doesn't exist
MESSAGES_FOLDER = 'messages'
os.makedirs(MESSAGES_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    if 'message' not in request.form:
        return 'No message provided', 400

    message = request.form['message']

    # Create a filename using the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(MESSAGES_FOLDER, f'message_{timestamp}.txt')

    # Write the message to a text file
    with open(filename, 'w') as f:
        f.write(message)

    return 'Message sent successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
