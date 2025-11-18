import json

# Read the JSON file
with open('text_dictionary.json', 'r') as f:
    data = json.load(f)

# Sort the brands alphabetically by the "name" field
data_sorted = sorted(data, key=lambda x: x['name'])

# Write the sorted data back to the file
with open('text_dictionary.json', 'w') as f:
    json.dump(data_sorted, f, indent=2)

print("Brands sorted alphabetically!")
print("\nSorted order:")
for brand in data_sorted:
    print(f"- {brand['name']}")