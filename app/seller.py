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

# blueprint of the seller..
seller = Blueprint('seller',__name__)

@seller.route('/seller/dashboard')
def seller_dashboard():

    seller_id = session_data() # session_id
    # lets get the number of products offered by the seller
    products_query = "SELECT COUNT(*) FROM sellers_products WHERE seller_id = %s"
    products = cursor.execute(products_query, (seller_id,))
    products_count = cursor.fetchall()[0][0]

    # lets get market that the seller sells in

    market_query = "SELECT seller_market.market_id, markets.market_name " \
               "FROM seller_market " \
               "JOIN markets ON markets.market_id = seller_market.market_id " \
               "WHERE seller_market.seller_id = %s"
    market = cursor.execute(market_query, (seller_id,))
    market_info = cursor.fetchone()

    # if the user is part of a market
    if market_info:
        market_id, market_name = market_info
    
    else:
        market_name = "none"

    # lets get the list of all markets
        
    markets = cursor.execute("SELECT * FROM markets")
    markets = cursor.fetchall()

    return render_template('seller/dashboard.html', products_count=products_count, market_name=market_name, markets=markets)


# method to list products sold by the seller
@seller.route('/seller/products')
def seller_products():

    # lets get the id of the seller

    seller_id = session_data()

    # lets get all products 

    products_query = "SELECT * FROM sellers_products WHERE seller_id=%s"
    products = cursor.execute(products_query, (seller_id,))
    products = cursor.fetchall()

    return render_template('seller/products.html', products=products)

# method to add products to the database
@seller.route('/seller/add-product', methods=['POST'])
def seller_add_product():

    # lets get the seller_id

    seller_id = session_data()

    if request.method=='POST':
        data = request.form

        product_name = data.get('product_name')
        price = data.get('price')

        # lets see if the seller is not already offering the same product

        products_query = "SELECT * FROM sellers_products WHERE product_name=%s AND seller_id=%s"
        product = cursor.execute(products_query, (product_name,seller_id,))
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
        
        VALUES = (seller_id, product_name, price, date)
        insert_query = "INSERT INTO sellers_products (seller_id, product_name, price, date) VALUES(%s,%s,%s,%s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()            
        flash('Product Created', category='success')
        return redirect('/seller/products')

# method to edit products
    
@seller.route('/seller/edit-product/<product_id>', methods=['POST'])
def seller_edit_product(product_id):

    # the sellers id

    seller_id = session_data()
    
    # lets receive the form data

    if request.method=="POST":

        data = request.form
        product_name = data.get('product_name')
        price = data.get('price')

        # now lets update the data

        update_query = "UPDATE sellers_products SET product_name = %s, price = %s WHERE seller_id = %s AND seller_product_id=%s"
        cursor.execute(update_query, (product_name, price, seller_id, product_id))
        connection.commit()

        flash('Details of '+product_name+' Have successfully been updated', category='success')
        return redirect('/seller/products')


# method to delete products

@seller.route('/seller/delete-product/<product_id>')
def seller_delete_product(product_id):

    # delete product
    delete_query = "DELETE FROM sellers_products WHERE seller_product_id = %s"
    cursor.execute(delete_query, (product_id,))
    connection.commit()
    flash('Product Deleted Successfully', category='success')
    return redirect('/seller/products')

# method to let seller join a market

@seller.route("/seller/join-market", methods=['POST'])
def join_market():

    # lets have the seller_id

    seller_id = session_data()

    # if post request

    if request.method=="POST":

        data = request.form

        market_id = data.get('market_id')

        date = datetime.today()

        VALUES = (seller_id, market_id, date)

        # now lets insert the data into the database

        insert_query = "INSERT INTO seller_market (seller_id, market_id, date) VALUES(%s, %s, %s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()

        flash('Congrats you are now part of a market', category='success')
        return redirect('/seller/dashboard')