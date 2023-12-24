# import filecmp
#
# f1 = "D:\KARNAK_36_STAB\SxS\src\DataFiles\Device_xml\ShiraitoSCI_UWWLInfo.xml"
# f2 = "D:\KARNAK_34_STAB\SxS\src\DataFiles\Device_xml\Gaheris_UWLInfo.xml"
#
# f1_data = f1.readlines()
# f2_data = f2.readlines()
#
# i = 0
#
# for line1 in f1_data:
#     i += 1
#
#     for line2 in f2_data:
#
#         # matching line1 from both files
#         if line1 == line2:
#             # print IDENTICAL if similar
#             print("Line ", i, ": IDENTICAL")
#         else:
#             print("Line ", i, ":")
#             # else print that line from both files
#             print("\tFile 1:", line1,"/n")
#             print("\tFile 2:", line2, "/n")
#         break
#
# # closing files
# f1.close()
# f2.close()


from pyspark import SparkContext

# Initialize a SparkContext
sc = SparkContext("local", "RDD Example")

# Create an RDD from a list of elements
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Perform transformations on the RDD
squared_rdd = rdd.map(lambda x: x ** 2)

# Perform an action to collect and print the results
result = squared_rdd.collect()

# Print the original and squared data
print("Original Data:", data)
print("Squared Data:", result)

# Stop the SparkContext
sc.stop()

