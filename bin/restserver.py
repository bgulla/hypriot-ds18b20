#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import json
import mimerender
import ds18b20

# Callback function for temperature callback (parameter has unit °C/100)
def cb_temperature(temperature):
  global currentTemperature
  currentTemperature = temperature/100.0

mimerender = mimerender.FlaskMimeRender()

render_xml = lambda rtn: '<?xml version="1.0" encoding="UTF-8"?><weather><description>Current Temperature in Bochum, Germany</description<currentTemp>%s</currentTemp></weather>'%rtn
render_json = lambda **args: json.dumps(args)
render_html = lambda rtn: '<html><body><p>Current Temperature in Bochum, Germany: <strong>%s</strong></p></body></html>'%rtn
render_txt = lambda rtn: rtn

app = Flask(__name__)

@app.route('/')
@mimerender(
    default = 'json',
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
)
def index():
        return {'rtn': 'Please call: <a href="/rest/v1.0/temperature/">/rest/v1.0/temperature/</a> to get the current temperature'}

@app.route('/rest/v1.0/temperature/')
@mimerender(
    default = 'json',
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
)

def getTemperatureJSON():
  temperature_dict = ds18b20.get_readings()
  return json.dumps(temperature_dict, ensure_ascii=False)

def getTemp():
  #print('Temperature: ' + str(temp))
  print getTemperatureJSON()
  return {'rtn': str(currentTemperature)}
    #return{temp}


if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
