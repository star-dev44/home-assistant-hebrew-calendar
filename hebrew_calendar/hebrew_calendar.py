from flask import Flask, jsonify
from datetime import datetime
from hdate import HDate

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_date():
    """ Convert today's date to Hebrew date """
    today = datetime.today()
    hebrew_date = HDate(today).hebrew_date_string()
    return jsonify({"hebrew_date": hebrew_date})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
