import geocoder

def get_current_city():
    try:
        # Using the geocoder library to get the current location based on IP address
        g = geocoder.ip('me')
        if g.city:
            return g.city
        else:
            return "City information not available"
    except Exception as e:
        return f"Error occurred: {e}"
