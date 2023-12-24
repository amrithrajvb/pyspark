import pyspark
import os
import findspark
findspark.init()
import pandas as pd
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import *
import pandas as pd
import PySimpleGUI as sg
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def read_file(input_file):
    df = pd.read_excel(input_file)

    # Print all values in the DataFrame
    print(df)

    spark = SparkSession.builder.appName("NewApp").getOrCreate()
    print(spark.sparkContext.appName)
    # creating table
    df.createOrReplaceTempView("emp")
    spark.sql("select name from emp").show()

    # # try:
    # #     with open(input_file, 'r', encoding='utf-8') as file:
    # #         content = file.read()
    # #         print(content)
    # # except Exception as e:
    # #     sg.popup_error(f"Error: {str(e)}")
    #
    # # Create a blank white image
    # width, height = 1200, 1200  # Adjust dimensions as needed
    # background_color = (255, 255, 255)
    # image = Image.new("RGB", (width, height), background_color)
    # draw = ImageDraw.Draw(image)
    #
    # # Load a font
    # font_size = 40
    # font = ImageFont.truetype("arial.ttf", font_size)
    #
    # # Draw data onto the image
    # text = "\n".join(df[row])
    # text_color = (0, 0, 0)  # Black
    # text_position = (50, 50)
    # draw.multiline_text(text_position, text, font=font, fill=text_color)
    #
    # # Save the image
    # image.save("cd_label.png")
    # print("Image created successfully.")


def main():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Welcome:")],
        [sg.Text("Enter the Input file")], [sg.Input(key="inFilePath", enable_events=True), sg.FileBrowse()],
        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar', bar_color=('green', 'black'),
                        visible=False)],
        [sg.Button("OK"), sg.Button("Exit")]
    ]

    window = sg.Window("ARTWORK", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "OK" and values["inFilePath"].strip():
            successFlag = True
            input_file = values["inFilePath"]
            window['progressbar'].Update(visible=True)
            read_file(input_file)
            window['progressbar'].Update(visible=False)
            window.disappear()
            sg.popup("Success!!!!" if successFlag else "Failed!!!", title="Status", icon=r"R.ico")
            window.reappear()

    window.close()


if __name__ == "__main__":
    main()

