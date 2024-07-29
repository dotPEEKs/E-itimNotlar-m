#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

# This code written for explaining x-frame-options header how it works and you can set up options from cmd-line and just available 3 settings
# DENY
# SAMEORIGIN
# ALLOW FROM URI
import os
from flask import Flask
from flask import url_for
from flask import render_template
from argparse import ArgumentParser
from flask_talisman import Talisman

flask_app = Flask(__name__,static_url_path="",static_folder="templates/")
class App:
    def __init__(self,template,app: Flask):
        self.template = template
        self.app = app
        self.app.add_url_rule("/",endpoint = "template",view_func=self.view_for_template)
        self.keyword_args = {"frame_options":self.template.upper(),"force_https":False}
        self.set_x_frame_option()
    def view_for_template(self):
        return render_template(f"{self.template}_template.html")
    def set_x_frame_option(self):
        if self.template == "deny":
            self.keyword_args["content_security_policy"] = {"frame-ancestors":'\'none\''} # IFrame'leri engellemek için sadece X-Frame-Options yeterli olmuyor bu yüzden content security policy ayarınıda eklememiz gerekiyor 
        Talisman(self.app,
            **self.keyword_args,
        )

if __name__ == "__main__":
    cli_parser = ArgumentParser(epilog = "X-Frame-Option Example test server")
    cli_parser.add_argument("--ip-addr","-i",default = "127.0.0.1",help = "IP addr for server")
    cli_parser.add_argument("--port","-p",default = 8090,help = "Port number for server")
    cli_parser.add_argument("--option","-o",default="same-origin",choices = ["deny","same-origin","allow-from"])

    parsed_cli_args = cli_parser.parse_args()
    server_app = App(parsed_cli_args.option,flask_app)
    flask_app.run(parsed_cli_args.ip_addr,parsed_cli_args.port)