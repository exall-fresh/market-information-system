# this file contains definition of all admin routes
import os
import json
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

# our custom modules
from .db_conn import db_conn
from .session import verify_session,session_data
# end of our custom modules

cursor, connection = db_conn() # import the cursor and the database connection objects

# blueprint of the scout..
scout = Blueprint('scout',__name__)

# scout dashboard
@scout.route('/scout/dashboard')
def scout_dashboard():

    # id of the user
    scout_id = session_data()

    # get the number of products uploaded by scout
    products_count = cursor.execute("SELECT COUNT(*) FROM scouts_products WHERE scout_id=%s",(scout_id,))
    products_count = cursor.fetchall()[0][0]

    # lets get the market_id that the scout belongs

    market = cursor.execute("SELECT market_id from scout_market WHERE scout_id=%s", (scout_id,))
    market_id = cursor.fetchone()

    # when the scout does has a market
    if market_id != None:


        market_id = market_id[0]
        print('market id')
        print(market_id)

        # get the number of trending products uploaded
        trending_products_count = cursor.execute("SELECT COUNT(*) FROM trending_products WHERE market_id = %s", (market_id,))
        trending_products_count = cursor.fetchall()[0][0]

        # the market that the scout is

        market_name = cursor.execute("SELECT m.market_name FROM scout_market AS sm INNER JOIN markets AS m ON m.market_id = sm.market_id WHERE sm.scout_id = %s", (scout_id,))
        market_name = cursor.fetchone()[0]

        # list of all markets
        markets = cursor.execute("SELECT * FROM markets")
        markets = cursor.fetchall()
        return render_template('scout/dashboard.html', products_count=products_count, trending_products_count=trending_products_count, market_name=market_name, markets=markets)
    
    # if the scout does not have a market

    else:

        market_id = 0

        # get the number of trending products uploaded
        trending_products_count = cursor.execute("SELECT COUNT(*) FROM trending_products WHERE market_id = %s", (market_id,))
        trending_products_count = cursor.fetchall()[0][0]

        # the market that the scout is

        market_name = "None"
        # list of all markets
        markets = cursor.execute("SELECT * FROM markets")
        markets = cursor.fetchall()
        return render_template('scout/dashboard.html', products_count=products_count, trending_products_count=trending_products_count, market_name=market_name, markets=markets)


# method to let scout join a market

@scout.route('/scout/join-market', methods=['POST'])
def scout_join_market():

    if request.method=="POST":
        data = request.form

        # the id of the market from the form
        market_id = data.get('market_id')

        # id of the scout
        scout_id = session_data()

        VALUES = (market_id, scout_id)

        # insert the data into database

        insert_query = "INSERT INTO scout_market (market_id, scout_id) VALUES(%s, %s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()

        flash('Successfully joined the market', category='success')
        return redirect('/scout/dashboard')
    
# method for products list
    
@scout.route('/scout/products')
def scout_products():
    
    # lets get the id of the scout

    scout_id = session_data()

    # get the list of products uploaded by the scout
    products = cursor.execute("SELECT * FROM scouts_products WHERE scout_id=%s", (scout_id,))
    products = cursor.fetchall()

    # lets get the list of products trending on the market    
    trending_products = cursor.execute("SELECT * FROM trending_products WHERE scout_id=%s", (scout_id,))
    trending_products = cursor.fetchall()

    return render_template("scout/products.html", products=products, trending_products=trending_products)

# method to let scout add product

@scout.route('/scout/add-product', methods=['POST'])
def scout_add_product():
    # lets get the seller_id

    scout_id = session_data()

    if request.method=='POST':
        data = request.form

        product_name = data.get('product_name')
        price = data.get('price')

        # lets see if the seller is not already offering the same product

        products_query = "SELECT * FROM scouts_products WHERE product_name=%s AND scout_id=%s"
        product = cursor.execute(products_query, (product_name,scout_id,))
        product = cursor.fetchone()

        # if there are some products sold

        if product:

            # name of the product in the db
            db_product_name = product[2]

            if db_product_name == product_name:
                flash('You already sell '+product_name, category='error')
                return redirect('/seller/products')


        # now lets insert the product in the database
            
        date = datetime.today()
        
        VALUES = (scout_id, product_name, price, date)
        insert_query = "INSERT INTO scouts_products (scout_id, product_name, price, date) VALUES(%s,%s,%s,%s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()            
        flash('Product Created', category='success')
        return redirect('/scout/products')
    
# method to add trending products
    
@scout.route('/scout/add-trending-product', methods=['POST'])
def scout_add_trending_product():

    if request.method=="POST":
        # get id of the scout
        scout_id = session_data()

        # get the market id of the scout
        market_id = cursor.execute("SELECT market_id from scout_market WHERE scout_id=%s",(scout_id,))
        market_id = cursor.fetchall()[0][0]

        # get the form data

        data = request.form

        product_name = data.get('product_name')

        date = datetime.today()

        VALUES = (scout_id, market_id, product_name, date)

        insert_query = "INSERT INTO trending_products (scout_id, market_id, product_name, date) VALUES(%s,%s,%s,%s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()

        flash(product_name+' has now been set to trending', category='success')
        return redirect('/scout/products')