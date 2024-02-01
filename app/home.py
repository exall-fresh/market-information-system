import os
import json
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for

# my custom modules

from .my_city import get_current_city
from .db_conn import db_conn

# end of my custom modules

# our database objects
cursor, connection = db_conn() # cursor, connection

home = Blueprint('home',__name__)
@home.route('/')
def home_page():

    # my city 

    city = get_current_city()
    
    city = city.lower() # make the string to lower case

    # markets in the city

    markets = cursor.execute("SELECT * FROM markets WHERE city=%s", (city,))
    markets = cursor.fetchall()
    
    # get the list of trending products
    trending_products = cursor.execute("SELECT * FROM trending_products")
    trending_products = cursor.fetchall()

    # get the list of scouts scout associations to markets

    scout_markets = cursor.execute("SELECT * FROM scout_market")
    scout_markets = cursor.fetchall()
    return render_template('home/home.html', markets=markets, city=city, trending_products=trending_products, scout_markets=scout_markets)



# route to show the profile of a market

@home.route('/market/<market_id>')
def market(market_id):

    # lets get the details of the market

    market = cursor.execute("SELECT * FROM markets WHERE market_id=%s", (market_id,))
    market = cursor.fetchone()

    # lets get the id of the scout for the market

    scout_id = cursor.execute("SELECT scout_id FROM scout_market WHERE market_id=%s", (market_id,))
    scout_id = cursor.fetchone()

    scouts_count = cursor.execute("SELECT COUNT(*) FROM scout_market WHERE market_id=%s", (market_id,))
    scouts_count = cursor.fetchall()[0][0]

    if scouts_count > 0:
        scout_id = scout_id[0][0]
        # now lets get the products uploaded by the scout_id
        products = cursor.execute("SELECT * FROM scouts_products WHERE scout_id=%s", (scout_id,))
        products = cursor.fetchall()
        
        # now lets get the list of trending products uploaded by the scout_id
        trending_products = cursor.execute("SELECT * FROM trending_products WHERE scout_id=%s", (scout_id,))
        trending_products = cursor.fetchall()
        return render_template('home/market.html', products=products, market=market, trending_products=trending_products)
    else:
        products = "None"
        trending_products = "None"
        return render_template('home/market.html', products="None", market=market)
    

# method to show the list of markets on the map
    
@home.route("/markets-list-map")
def markets_list_map():

    return render_template('home/map.html')