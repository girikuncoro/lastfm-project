'''
	This script will merge multiple JSON files
	into array of JSON written in one file named 'merged_seeds.json'
	Specify the filename on commandline as below example:
	# python merge_json.py artist_chart_fans_data.json metro_artist_chart_data.json 
'''
import json
from collections import OrderedDict

filename = OrderedDict()
output = []
# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    for i in range(1,len(sys.argv)):
    		filename[sys.argv[i]] = sys.argv[i]

for files in filename:
	json_data = open(files)
	data = json.load(json_data)
	output.append(data)
	json_data.close()

json_out = open('merged_seeds.json', 'w')
json_out.write(json.dumps(output, ensure_ascii=False).encode('utf-8'))
json_out.close()
print "Completed!"