from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from sqlalchemy.sql import func
from complete_function import *
from scrape_yahoo_finance import *
from . import db
from .models import *


views = Blueprint("views", __name__)

@views.route("/")
def home():
    tickers = get_trending_tickers()
    print("tickers:", tickers)
    return render_template("home.html", user=current_user, tickers=tickers)

@views.route("/analysis", methods=['GET', 'POST'])
def analysis():
    if request.method == "POST":
        ticker = request.form.get("ticker")
        user_ticker = User.query.filter_by(id=current_user.id).first()
        user_ticker.current_stock = ticker
        db.session.commit()
        data = get_complete(str(ticker))
        prices = get_current_price_yahoo(ticker)
        ratios = get_current_ratios(ticker)
        div = get_current_div(ticker)
        return render_template("analysis.html", user=current_user, current_ticker=ticker, data=data ,prices=prices, ratios=ratios, div=div)

    if request.method == "GET":
        ticker = User.query.filter_by(id=current_user.id).first()
        ticker =ticker.current_stock
        data = get_complete(str(ticker))
        prices = get_current_price_yahoo(ticker)
        ratios = get_current_ratios(ticker)
        div = get_current_div(ticker)
        return render_template("analysis.html", user=current_user, current_ticker=ticker, data=data, prices=prices, ratios=ratios, div=div)

#current_stock



