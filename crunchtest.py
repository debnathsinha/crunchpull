import simplejson, urllib

result = simplejson.load(urllib.urlopen('http://api.crunchbase.com/v/1/company/facebook.js'))
if 'Error' in result:
	print "foo"

comp = result['competitions']
num_emp = result['number_of_employees']
products = result['products']
relations = result['relationships']

print "num_emp: " + str(num_emp)

for i in comp:
	print i

for i in products:
	print i

for i in relations:
	print i

#print comp
#from StringIO import StringIO
#io = StringIO(comp)
#comp1 = simplejson.load(io)

#print comp1
