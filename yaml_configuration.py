
import os
import yaml
def read_yaml_files(folder_path):

    #collecting path
    paths=[]

    #read yaml file
    with open('setup.yaml', 'r') as file:
        datas = yaml.safe_load(file)
    # print("duplicate",type(datas))

    #taking Branch details from Yaml file
    product = datas["DevelopmentInformation"]["Branches"]
    print("Branch_Data", product)

    #storing Branch names
    keys=[]
    for key, value in product.items():
        keys.append(key)

    print(keys)

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):



        # Check if the file has a YAML extension
        for branch in range(len(keys)):
            branch_name=keys[branch]
            # print(mm)
            if filename.endswith('.yaml') and filename.startswith(branch_name):
                print(filename.startswith(keys[branch]))
                file_path = os.path.join(folder_path, filename)

                print("path",file_path)
                paths.append(file_path)
                print(paths)
                break

    data_collection={}
    for path in range(len(paths)):


        with open(paths[path], 'r') as file:
            file_data = yaml.safe_load(file)
            print("datas",file_data)
            for key,value in file_data.items():
                print("Values",value)
                data_collection.update(value)
    datas['DevelopmentInformation']['Products'] = data_collection
    print ("loop",datas)
    print(data_collection)

    with open('setup.yaml', 'w') as file:
        yaml.dump(datas, file, default_flow_style=False)



# Provide the path to the folder containing YAML files
folder_path = 'C:\Users\ISLUSER\PycharmProjects\pySPArk'

# Read all YAML files from the folder
result = read_yaml_files(folder_path)

# Print or use the result as needed
print(result)


