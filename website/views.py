from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from sqlalchemy.sql import func
from complete_function import *
from scrape_yahoo_finance import *
from . import db
from .models import *
from cash_flow_function import *
from balance_function import *
from income_function import *



views = Blueprint("views", __name__)

@views.route("/financials")
def financials():
    ticker = User.query.filter_by(id=current_user.id).first()
    ticker =ticker.current_stock
    data = get_full_data(ticker)
    cash_flow = get_cash_flow_statement(data)
    balance = get_balance_sheet(data)
    income = get_income_statement(data)
    print((cash_flow.get("cfo_net_income")[1][-1]))
    return render_template("financials.html", user=current_user, cash_flow=cash_flow, balance=balance, income=income)

@views.route("/")
def home():
    return render_template("home.html", user=current_user)

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



