# # import yaml
#
# # # Read the main YAML file
# # with open('D:\MAC\MAC_PACKAGING\setup.yaml', 'r') as main_yaml_file:
# #     main_data = yaml.safe_load(main_yaml_file)
#
# # # Include the content of the included YAML file
# # with open('D:\MAC\MAC_PACKAGING\K18.devices.yaml', 'r') as included_yaml_file:
# #     included_data = yaml.safe_load(included_yaml_file)
#
# # main_data['DevelopmentInformation']['Products'] = included_data
#
# # with open('D:\MAC\MAC_PACKAGING\K19.devices.yaml', 'r') as included_yaml_file:
# #     included_data = yaml.safe_load(included_yaml_file)
#
# # main_data['DevelopmentInformation']['Products'] = included_data
#
# # # Write the combined data back to the main YAML file
# # with open('main.yaml', 'w') as main_yaml_file:
# #     yaml.dump(main_data, main_yaml_file, default_flow_style=False)
#
#
#
# import yaml
#
# # Load the contents of file1.yaml
# with open('K18.devices.yaml', 'r') as file:
#     data_from_file1 = yaml.safe_load(file)
#
# # Load the contents of file2.yaml
# with open('K18.devices.yaml', 'r') as file:
#     data_from_file2 = yaml.safe_load(file)
#
# # Merge the two dictionaries
# merged_data = {**data_from_file2, **data_from_file1}
#
# # Save the merged data back to file2.yaml
# with open('file2.yaml', 'w') as file:
#     yaml.dump(merged_data, file, default_flow_style=False)
#
#
#
#
#
#
