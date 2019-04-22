import csv
import json

try:
    conf_list = []
    conf_list = list(csv.DictReader(open('List.csv')))

    with open('config.json', 'w') as f:
    	f.write('{')
    	for entry in conf_list[:-1]:
    		f.write('"'+entry['NAME']+'": {')
    		f.write('"desc": "' + entry['DESC'] + '",')
    		f.write('"url": "' + entry['URL'] + '"},')
    	else:
    		f.write('"'+conf_list[-1]['NAME']+'": {')
    		f.write('"desc": "' + conf_list[-1]['DESC'] + '",')
    		f.write('"url": "' + conf_list[-1]['URL'] + '"}')
    		f.write('}')
except Exception as e:
	print(str(e))