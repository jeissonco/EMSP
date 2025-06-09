import json
from operator import itemgetter

# Sample JSON array of dictionaries
json_array = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 22}]'

# Parse JSON into a Python list of dictionaries
data_list = json.loads(json_array)

# Parse JSON into a Python list of dictionaries
data_list = json.loads(json_array)

# Sort based on the 'age' key
sorted_data_age = json.dumps(sorted(data_list, key=itemgetter('age')))

print('Sorted based on age ', sorted_data_age)