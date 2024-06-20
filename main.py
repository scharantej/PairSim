
# app.py

from flask import Flask, render_template, request
from pair_trading_rl import trade

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trade', methods=['POST'])
def initiate_trade():
    pairs = request.form.getlist('pairs')
    timeframe = request.form.get('timeframe')
    return trade(pairs, timeframe)

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run()
