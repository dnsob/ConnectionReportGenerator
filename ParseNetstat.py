#!/usr/bin/python

import psutil
import numpy as np
import whois
from ipwhois import IPWhois
from pylatex import Document, Section, Subsection, Table, Math, TikZ, Axis, Plot, Figure, Package, Matrix, Tabular
from pylatex.utils import italic, escape_latex

for conn in psutil.net_connections():
	try:
		connIp = conn[4][0]
		print("Checking %(ip)s" % {"ip":connIp})
		dataObj = IPWhois('%(ip)s' % {"ip":connIp})
		res = dataObj.lookup()
		print(res["nets"][0]["description"])
		print ("")
		print ("")
	except Exception:
		pass

#w = whois.whois('8.8.8.8')
#print(w)
