import yaml

# Load the contents of file1.yaml
with open('K18.devices.yaml', 'r') as file:
    data_from_file1 = yaml.safe_load(file)

# Load the contents of file2.yaml
with open('K19.devices.yaml', 'r') as file:
    data_from_file2 = yaml.safe_load(file)

with open('file2.yaml', 'r') as file:
    data = yaml.safe_load(file)

# print(product)
# Merge the two dictionaries
merged_data = data_from_file1.copy()
merged_data1=data_from_file2.copy()
data1=dict(merged_data)
print(data1)
data2=dict(merged_data1)
print(data2)
# merged_dict = dict(data1, **data2)
# # mm=data1.update(data2)
# # print("after",merged_dict)

# merged_data.update(**data_from_file2)
# print(merged_data)
# merged_data1=data_from_file2.copy()
# print(merged_data1)
# merged_dict = dict(merged_data, **merged_data1)


# merged_dict = {**dict1, **dict2}
# merged_data.update(merged_data1)
# print("updated",merged_data)
# print("updated",merged_data)


data_list = {'DevelopmentInformation': {'Products': [data1, data2]}}
#
data.update(data_list)
# data=data_list
# product=merged_data

# merged_data=data
# merged_data = {product:data_from_file1}
# Save the merged data back to file2.yaml
with open('file2.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)