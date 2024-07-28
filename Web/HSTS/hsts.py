#/usr/bin/python3 

# -*- encoding: utf-8 -*-
import sys
import urllib.request as urllib
import threading
from flask import Flask
from flask_talisman import Talisman
from argparse import ArgumentParser
from flask_talisman.talisman import ONE_YEAR_IN_SECS
flask_app = Flask(__name__)
@flask_app.route("/")
def route():
    return """
    <html>
      <head>
        <title>
          HSTS EXAMPLE
        </title>
      </head>
      <body>
        <h1>This is simple HSTS app Well done</h1>
      </body>
    </html>
    """
if __name__ == "__main__":
    talisman = Talisman(
      app = flask_app,
      force_https = True, # HTTPS zorlamak için
      strict_transport_security = True, # Sunucu başlığına HSTS bilgisini eklemek için
      strict_transport_security_max_age = ONE_YEAR_IN_SECS, # HSTS başlığınının geçerlilik süresi tarayıcı bu süre zarfı içersinde bağlantılar https üzerinden yapacaktır olurda http olursa buna izin vermeyecektir
      strict_transport_security_include_subdomains = True, # İlgili sitenin bütün alt domainlerine HSTS özelliğini aktifleştirmek için
      force_https_permanent = True # bu ise HTTP üzerinden gelen bağlantıları HTTPS'e yönlendirmek için
    )
    https_thread = threading.Thread(target=flask_app.run,args=("192.168.1.96",443,),kwargs={"ssl_context":("cert.pem","key.pem")},)
    https_thread.daemon = True
    https_thread.start()
    flask_app.run("192.168.1.96",80)