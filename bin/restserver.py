#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import json
import mimerender
import ds18b20

mimerender = mimerender.FlaskMimeRender()

render_json = lambda **args: json.dumps(args)
render_html = lambda rtn: '<html><body><p>Current Temperature in Bochum, Germany: <strong>%s</strong></p></body></html>'%rtn
render_txt = lambda rtn: rtn

app = Flask(__name__)

@app.route('/')
@mimerender(
    default = 'json',
    html = render_html,
    json = render_json,
    txt  = render_txt
)
def index():
        return {'rtn': 'Please call: <a href="/rest/v1.0/temperature/">/rest/v1.0/temperature/</a> to get the current temperature'}

@app.route('/rest/v1.0/temperature/')
@mimerender(
    default = 'json',
    html = render_html,
    json = render_json,
    txt  = render_txt
)

def getTemperatureJSON():
  temperature_dict = ds18b20.get_readings()
  return temperature_dict

def getTemp():
  tjson =  getTemperatureJSON()
  currentTemperature = "100.5"
  return {'rtn': tjson}

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
