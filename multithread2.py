# import threading
# import os
#
# def task_1():
#     print("first task thread name:{}".format(threading.current_thread().name))
#     print("first task process_id :{}".format(os.getpid()))
# 
# def task_2():
#     print("second task thread name:{}".format(threading.current_thread().name))
#     print("second task process_id :{}".format(os.getpid()))
#
# if __name__== "__main__":
#     print("main program thread name:{}".format(threading.current_thread().name))
#     print("main program process_id :{}".format(os.getpid()))
#
#
#     t1=threading.Thread(target=task_1,name='t1')
#     t2=threading.Thread(target=task_2,name='t2')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
# import yaml
#
# # Load the contents of file1.yaml
# with open('K18.devices.yaml', 'r') as file:
#     data_from_file1 = yaml.safe_load(file)
#
# # Load the contents of file2.yaml
# with open('K19.devices.yaml', 'r') as file:
#     data_from_file2 = yaml.safe_load(file)
#
# # Merge the two dictionaries
# merged_data = {**data_from_file2, **data_from_file1}
#
# # Save the merged data back to file2.yaml
# with open('file2.yaml', 'w') as file:
#     yaml.dump(merged_data, file, default_flow_style=False)
#


import os
import yaml
#
# # Load the contents of file1.yaml
# with open('K18.devices.yaml', 'r') as file:
#     data_from_file1 = yaml.safe_load(file)
#
# # Load the contents of file2.yaml
# with open('K19.devices.yaml', 'r') as file:
#     data_from_file2 = yaml.safe_load(file)
#
# with open('file2.yaml', 'r') as file:
#     data = yaml.safe_load(file)
#
#
# with open('setup.yaml', 'r') as file:
#     datas = yaml.safe_load(file)
#
# # print(product)
# # Merge the two dictionaries
# merged_data = data_from_file1.copy()
# merged_data1=data_from_file2.copy()
# data1=dict(merged_data)
# print(data1)
# data2=dict(merged_data1)
# print(data2)
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
# global product
# product=datas["DevelopmentInformation"]["Branches"]
# print("Branch_Data",product,len(product),product[0])



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









# for i in range(len(product)):


#
# data_list = {'DevelopmentInformation': {'Products': [data1, data2]}}
# #
# data.update(data_list)
# # data=data_list
# # product=merged_data
#
# # merged_data=data
# # merged_data = {product:data_from_file1}
# # Save the merged data back to file2.yaml
# with open('file2.yaml', 'w') as file:
#     yaml.dump(data, file, default_flow_style=False)
