# this file contains definition of all admin routes
import os
import json
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for

# our custom modules
from .db_conn import db_conn
# end of our custom modules

cursor, connection = db_conn() # import the cursor and the database connection objects

# blueprint of the admin..
admin = Blueprint('admin',__name__)

# admin dashboard
@admin.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')
# end of the admin dashboard

# the markets list page
@admin.route('/admin/markets')
def admin_markets_list():

    markets = cursor.execute('SELECT * FROM markets')
    markets = cursor.fetchall()

    return render_template('admin/markets.html', markets=markets)
# end of the markets list page

# method to add market into the database

@admin.route('/admin/add-market', methods=['POST'])
def admin_add_market():

    # when user makes a post request to add a market
    if request.method=="POST":

        data = request.form

        # lets receive the data from the forms

        market_name = data.get('market_name') # market_name
        city = data.get('city') # city market is located
        coordinates = data.get('coordinates') # coordinates market is located

        # lets find a market with the same name or coordinates

        markets = cursor.execute('SELECT * FROM markets WHERE market_name=%s OR coordinates=%s', (market_name, coordinates,))

        markets = cursor.fetchone()

        # if we have some markets
        if markets:

            db_market_name = markets[1]
            db_coordinates = markets[3]

            # lets check if there is any market in the db with the same name as the input market

            if db_market_name == market_name:

                flash('The market already exists. Try a different name', category='error')
                return redirect('/admin/markets')
            
            # check if the input coordinates and the ones in the db are similar

            elif db_coordinates == coordinates:
                flash(db_market_name+' Is already situated on the coordinates given! try modifying the coordinates of '+db_market_name+' Then give these coordinates to '+market_name, category='error')
                return redirect('/admin/markets')

            # lets insert the market data into the database

        VALUES = (market_name, city, coordinates)
        insert_query = "INSERT INTO markets (market_name, city, coordinates) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, VALUES)
        connection.commit()

        # now lets upload and insert the image
        if 'photo' in request.files:
            photo = request.files['photo']

            # when image variable is not null
            if photo.filename != '':
                photo_location = 'app/static/uploads/'+photo.filename
                # upload the image in the server
                photo.save(photo_location)

                # store the location of the image in the database

                market_id = cursor.lastrowid

                VALUES = (market_id, photo_location)
                insert_query = "INSERT INTO market_images (market_id, image_location) VALUES(%s,%s)"
                cursor.execute(insert_query, VALUES)
                connection.commit()

                print(photo_location)
            
            # if image variable is null
            else:
                flash('Market Added Successfully. However no image has been uploaded. You can upload an image by clicking on the edit button next to the market name', category='success')
                return redirect('/admin/markets')

        flash('Market Added Successfully', category='success')
        return redirect('/admin/markets')
# end of method to add market to the database

# method to edit the details of a market
    

@admin.route('/admin/edit-market/<market_id>', methods=['POST'])
def admin_edit_market(market_id):
    
    # lets receive the form data

    if request.method=="POST":

        data = request.form
        market_name = data.get('market_name')
        city = data.get('city')
        coordinates = data.get('coordinates')

        # now lets update the data

        update_query = "UPDATE markets SET market_name = %s, city = %s, coordinates = %s WHERE market_id = %s"
        cursor.execute(update_query, (market_name, city, coordinates, market_id))
        connection.commit()

        # now lets upload and update the image
        if 'photo' in request.files:
            photo = request.files['photo']

            # when image variable is not null
            if photo.filename != '':

                # the newly uploaded photo
                photo_location = 'app/static/uploads/'+photo.filename
                # upload the image in the server
                photo.save(photo_location)
                update_query = "UPDATE market_images SET image_location = %s WHERE market_id = %s"
                # Execute the query with parameters
                cursor.execute(update_query, (photo_location, market_id))
                connection.commit()

            else:
                print('')
        flash('Details of '+market_name+' Have successfully been updated', category='success')
        return redirect('/admin/markets')
    
# end of the market update method
    
# method to delete market
@admin.route('/admin/delete-market/<market_id>')
def admin_delete_market(market_id):

    # delete market
    delete_query = "DELETE FROM markets WHERE market_id = %s"
    cursor.execute(delete_query, (market_id,))
    connection.commit()

    # delete images associated to market

    try:
        delete_query = "DELETE FROM market_images WHERE market_id = %s"
        cursor.execute(delete_query, (market_id,))
        connection.commit()
    except:

        flash('Market Has been removed successfully', category='success')
        return redirect('/admin/markets')

    flash('Market Has been removed successfully', category='success')
    return redirect('/admin/markets')

# end of the method to delete market

# method to show all sellers

@admin.route("/admin/sellers")
def admin_sellers():

    # lets read all sellers in the database

    sellers = cursor.execute('SELECT * FROM users WHERE role=2')
    sellers = cursor.fetchall()

    return render_template('admin/sellers.html', sellers=sellers)


# method to show all scouts

@admin.route('/admin/scouts')
def admin_scouts():
    # lets read all sellers in the database

    scouts = cursor.execute('SELECT * FROM users WHERE role=3')
    scouts = cursor.fetchall()

    return render_template('admin/scouts.html', scouts=scouts)

