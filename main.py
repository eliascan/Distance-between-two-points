from urllib.parse import urlparse
from geopy.distance import geodesic


def cal_dist(url):
    u = urlparse(url)
    t = u.query
    t = t.split("&")

    t[0] = t[0][5:]  # longitude first point
    t[1] = t[1][5:]  # latitude first point
    t[2] = t[2][5:]  # longitude second point
    t[3] = t[3][5:]  # latitude second point

    start = (t[1], t[0])  # Start point
    end = (t[3], t[2])    # End point

    return geodesic(start, end).km

'''
    CALLING FUNCTION
    
    The url have to be like this: http://mysite/coordenates?lon1=-73.7611174&lat1=45.4804818&lon2=-73.6376267&lat2=45.5947285
'''

http = input("Set the http with the coordinates to calculate: ")

print(cal_dist(http))
