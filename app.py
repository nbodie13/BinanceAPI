# to run this app, use command
    # python -m flask run

# automatic updates with DEBUG mode, in terminal type
    # $env:FLASK_ENV = "development"

from flask import Flask, render_template
import config, csv
from binance.client import Client

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET, tld='us')

@app.route('/')
def index():
    title = 'CoinView'
    return render_template('coinview.html', title=title)

    info = client.get_account()

    print(info)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'