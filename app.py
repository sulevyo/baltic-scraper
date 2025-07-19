from flask import Flask, jsonify
from scraper import scrape_baltic_stocks

app = Flask(__name__)

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    data = scrape_baltic_stocks()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
