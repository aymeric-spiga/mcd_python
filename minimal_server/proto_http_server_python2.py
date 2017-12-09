#!/usr/bin/python
# -*- coding: UTF-8 -*-

from BaseHTTPServer import HTTPServer 
from CGIHTTPServer import CGIHTTPRequestHandler

# Port du serveur http
port = 8080
# Allocation de l'objet de gestion du serveur
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
 
# On lance le serveur indefiniement
print('Lancement du serveur http sur le port: ' + str(httpd.server_port))
httpd.serve_forever()
