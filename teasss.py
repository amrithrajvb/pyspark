import pandas as pd
from reportlab.pdfgen import canvas

# Read data from Excel
excel_file = "CD_L.xlsx"
df = pd.read_excel(excel_file)
mm=df.head()
print(mm)


# Function to render DataFrame to PDF with handling text overlap
def render_dataframe_to_pdf(dataframe, filename='outputo.pdf'):
    c = canvas.Canvas(filename, pagesize=(6872, 7792))  # Set pagesize for landscape mode
    width, height = c._pagesize
    margin = 50

    # Calculate the available width for text
    available_width = width - 2 * margin

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Calculate the column width based on the number of columns
    column_width = available_width / len(dataframe.columns)

    # Set initial position for text
    x, y = margin, height - margin

    # Iterate through each row and column to add text to the PDF
    for index, row in dataframe.iterrows():
        for col, value in row.items():
            # Check if the text exceeds the available width
            if x + column_width > width - margin:
                # Move to the next row if the text exceeds the width
                x = margin
                y -= 10  # Adjust the spacing between rows

            # Check for overlap with the bottom margin
            if y < margin:
                # Move to the next page
                c.showPage()
                y = height - margin

            c.drawString(x, y, f"{col}: {value}")
            x += column_width

        # Move to the next row
        x = margin
        y -= 15  # Adjust the spacing between rows

    c.save()

# Call the function with your DataFrame and desired output filename
render_dataframe_to_pdf(mm, filename='outputo.pdf')