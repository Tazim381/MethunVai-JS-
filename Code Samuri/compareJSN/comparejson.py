import json

json1_file = 'data1.json'
json2_file = 'data2.json'

# Load the data from the JSON files
json1_data = json.load(open(json1_file))
json2_data = json.load(open(json2_file))

# Convert the data to Python objects
json1_obj = json.dumps(json1_data)
json2_obj = json.dumps(json2_data)

# Compare the objects
if json1_obj == json2_obj:
   print('The JSON files are equal.')
else:
   print('The JSON files are not equal.')
