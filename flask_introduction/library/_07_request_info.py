"""Request information.

HTTP communication starts with an HTTP Request. It's a request from a client
to access a particular resource.
Flask wraps the request info in a `request` object which can be used
in any view or template (automatically available).

Docs: http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/request-info')
def request_info():
    # Get location info using https://freegeoip.net/
    #geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    geoip_url = 'https://api.ipgeolocation.io/ipgeo?apiKey=37639be1018e4a44ab3d7241589e919c'
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html',
                           client_location=client_location)
