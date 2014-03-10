# This URL: http://www.pythonchallenge.com/pc/return/disproportional.html
# Next URL: http://www.pythonchallenge.com/pc/return/italy.html

import xmlrpclib

server = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()
print server.phone('Bert')
