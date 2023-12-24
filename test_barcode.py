# import barcode
# from barcode.writer import ImageWriter
#
# def generate_barcode_data(data):
#     # Join the list elements into a single string
#     code_str = ''.join(data)
#
#     # Generate a Code 39 barcode
#     code39 = barcode.get_barcode_class('code39')
#     code = code39(code_str, writer=ImageWriter(), add_checksum=False)
#     filename = code.save('my_barcode')
#
#     # Load the generated barcode image
#     with open(filename, 'rb') as f:
#         barcode_data = f.read()
#
#     return barcode_data
#
# def split_barcode_into_columns(barcode_data, num_columns=12):
#     # Split barcode data into columns
#     barcode_length = len(barcode_data)
#     segment_size = barcode_length // num_columns
#     barcode_columns = [barcode_data[i:i + segment_size] for i in range(0, barcode_length, segment_size)]
#
#     return barcode_columns
#
# # Example usage:
# barcode_data = generate_barcode_data(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2'])
# columns = split_barcode_into_columns(barcode_data)
#
# for i, column in enumerate(columns, start=1):
#     print(f"Column {i}: {column}")
#
#
# from PIL import Image
#
# def split_image_into_columns(image_path, num_columns):
#     img = Image.open(image_path)
#     img_width = img.width
#     column_width = img_width // num_columns
#     columns = []
#
#     for i in range(num_columns):
#         left = i * column_width
#         right = (i + 1) * column_width
#         column = img.crop((left, 0, right, img.height))
#         columns.append(column)
#
#     return columns
#
# def join_columns(columns):
#     # Get the width and height of the first column
#     width, height = columns[0].size
#
#     # Create a new image with a width equal to the sum of column widths
#     joined_image = Image.new('RGB', (len(columns) * width, height), color='white')
#
#     # Paste each column into the new image
#     for i, column in enumerate(columns):
#         joined_image.paste(column, (i * width, 0))
#
#     return joined_image
#
# # Example usage:
# image_path = r"C:\Users\ISLUSER\Desktop\amrith\old\Validator\vv_.png.png"
# num_columns = 13
#
# columns = split_image_into_columns(image_path, num_columns)
#
# # Save or display the individual columns as needed
# for i, column in enumerate(columns):
#     column.save(f"column_{i+1}.jpg")
#
# # Join the columns into a single image
# joined_image = join_columns(columns)
#
# # Save the joined image
# joined_image.save("joined_images.jpg")
#
# # Display the joined image
# joined_image.show()



# Replace 'your_number_here' with the actual barcode number
import barcode
from barcode.writer import ImageWriter
from pathlib import Path

barcode_format = barcode.get_barcode_class('code39')

# Replace '499N4-60101' with the actual barcode number
number = '499N4-60101'

# Create the barcode without specifying the number
my_barcode = barcode_format(number, writer=ImageWriter(), add_checksum=False)

# Get the path to save the image
pa = Path.cwd() / "{}_SIVs".format(number)
image_path = str(pa) + ".png"
print(image_path)

# Save the barcode image without the number
my_barcode.save(image_path)



