#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import mqtt_publish
from src import parser_json
from src import io

import json


def get_geo(self):
    print("geo !")

def get_image(self):
    self.send_response(200)
    self.send_header("Content-type", "image/bmp")
    self.end_headers()
    self.wfile.write(io.load_binary(cla.hubium.path_image))

def get_falsealarm(self):
    mqtt_publish.publish_false_alarm()

def get_test(self):
    self.send_response(200)

def get_state_hu(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    data = parser_json.get_json_encoded(cla.hubium.path_state_hu)
    self.wfile.write(data)

def get_state_py(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    data = parser_json.get_json_encoded(cla.hubium.path_state_py)
    self.wfile.write(data)
