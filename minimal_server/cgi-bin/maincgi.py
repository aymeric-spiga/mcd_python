#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb 
#from modules import *

########################################
tryimage = False # set to True to try a simple matplotlib server use
if tryimage:
  import numpy as np
  from matplotlib.figure import Figure
  from matplotlib.backends.backend_agg import FigureCanvasAgg
  xx = np.arange(24)/(np.pi)
  yy = np.sin(xx)
  fig = Figure()
  yeah = fig.add_subplot(1,1,1)
  yeah.plot(yy,xx,'go')
  FigureCanvasAgg(fig).print_png("webapp.png")
########################################

# for debugging in web browser
cgitb.enable()

## Create instance of FieldStorage 
#form = cgi.FieldStorage() 

##### NOW WRITE THE HTML PAGE TO USER
print "Content-type:text/html;charset=utf-8\n"
print     #Apache needs a space after content-type
header="""<html><head><title>Mars Climate Database: The Web Interface</title></head><body>"""
print header
print "THIS IS A TEST!"
if tryimage:
  print "<img src='../webapp.png'><br />"
bottom = "</body></html>"
print bottom

