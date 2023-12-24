import PySimpleGUI as sg
import datetime
from pathlib import Path
from docxtpl import DocxTemplate
from docx2pdf import convert
from num2words import num2words


#-----------view settings-----------#
# def view_window():
#     layout = [
#         [sg.Text(settings["Admin"]["Username"])],
#         [sg.Text(settings["Admin"]["Password"])],
#         [sg.Text(settings["PackageRate"]["PRate"])],
#         [sg.Button("Exit")]
#     ]
#     window = sg.Window("View Settings",layout)
#     while True:
#         event, values = window.read()
#         if event in (sg.WINDOW_CLOSED, "Exit"):
#             break
#     window.close()
#-----------------main window---------#
def main_window():

    #----------GUI definition-----------#
    layout = [
        [sg.Button("Admin")],
        [sg.Text("QUOTATION", font=("Arial" + "bold" + "underline", 14), justification="centre")],
        [sg.Text("Recepient Name            ")], [sg.Input(key="RECEPIENT", do_not_clear=True)],
        [sg.Text("Contact Number            ")], [sg.Input(key="RECEPIENTNUM", do_not_clear=True)],
        [sg.Text("Project Name              ")], [sg.Input(key="PROJECT", do_not_clear=True)],
        [sg.Text("Rate per hour             ")], [sg.Input(key="RATEPERHOUR", do_not_clear=True)],
      #  [sg.Text("Additional Hours          ")], [sg.Input(key="ADDITIONAL", do_not_clear=True)],
        [sg.Text("Tax type                  ")], [sg.Input(key="TAX", do_not_clear=True)],
        [sg.Text("('GST' for State . 'IGST' for InterState)", font=("Arial", 8))],
        [sg.Text("Tax Rate                  ")], [sg.Input(key="TAXRATE", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Download"), sg.Exit()]
    ]
    title = settings["GUI"]["title"]
    window = sg.Window(title, layout, icon="VMedia.ico", size=(400, 600), finalize=True)
    #-------- For checking all the values for mandatory fields are entered----- #
    input_key_list = [key for key, value in window.key_dict.items()
                      if isinstance(value, sg.Input)]
    del input_key_list[4]


    while True:
        event,values = window.read()
        # if event == "View":
        #     window.disappear()
        #     view_window()
        #     window.reappear()
        sg.theme(settings["GUI"]["theme"])
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "Admin":
            window.disappear()
            admin_window()
            window.reappear()
        if event == "Download":
            if all(map(str.strip, [values[key] for key in input_key_list])):
                documentPath = Path(__file__).parent / "VMedia.docx"

                if (documentPath and Path(documentPath).exists()):
                    # sg.popup_no_titlebar("Path exists")
                    doc = DocxTemplate(documentPath)
                    values["QUOTATION"] = settings["Quotation"]["Number"]
                    values["PLANRATE"] = settings["PackageRate"]["PRate"]
                    date = datetime.datetime.today().strftime("%d-%m-%Y")
                    values["DATE"] = date
                    ImproperVal = ""
                    rateperhr = values["RATEPERHOUR"]
                   # additional = values["ADDITIONAL"]
                    taxrate = values["TAXRATE"]
                    contact = values["RECEPIENTNUM"]
                    ImproperVal = checkValues(rateperhr, taxrate,contact)

                    if ImproperVal != "":
                        # sg.popup_no_titlebar(ImproperVal)
                        if (ImproperVal == "Rate"):
                            window["RATEPERHOUR"]('')
                            window.disappear()
                            sg.popup_no_titlebar("Improper Rate per hour")
                            window.reappear()
                        # if (ImproperVal == "Additional"):
                        #     window["ADDITIONAL"]('')
                        #     window.disappear()
                        #     sg.popup_no_titlebar("Improper Additional hours")
                        #     window.reappear()
                        if (ImproperVal == "Taxrate"):
                            window["TAXRATE"]('')
                            window.disappear()
                            sg.popup_no_titlebar("Improper TaxRate")
                            window.reappear()
                        if (ImproperVal == "Contact"):
                            window["RECEPIENTNUM"]('')
                            window.disappear()
                            sg.popup_no_titlebar("Improper contact number")
                            window.reappear()
                    else:
                        # sg.popup_no_titlebar("All proper values")
                        Tax = 0
                        if values["TAX"] == "GST" or values["TAX"] == "gst":
                            # sg.popup_no_titlebar("1")
                            values["TAX1"] = "CGST :" + values["TAXRATE"] + " %"
                            # sg.popup_no_titlebar("2")
                            values["TAX2"] = "SGST :" + values["TAXRATE"] + " %"
                        else:
                            # sg.popup_no_titlebar("3")
                            values["TAX1"] = "IGST:" + values["TAXRATE"] + " %"
                            # sg.popup_no_titlebar("4")
                        # if values["ADDITIONAL"] == "":
                        #     # sg.popup_no_titlebar("5")
                        #     values["ADDITIONAL"] = "0"
                        #     # sg.popup_no_titlebar("6")
                        #     values["ADDITIONALRATE"] = "0"
                        #     # sg.popup_no_titlebar("7")
                        # else:
                        #     values["ADDITIONALRATE"] = int(values["ADDITIONAL"]) * int(values["RATEPERHOUR"])
                        #     # sg.popup_no_titlebar("8")
                        # intAdditional = int(values["ADDITIONALRATE"])
                        # sg.popup_no_titlebar("9")
                        intPlanRate = int(values["PLANRATE"])
                        # sg.popup_no_titlebar("10")
                        intTaxRate = int(values["TAXRATE"])
                        # sg.popup_no_titlebar("11")
                        intRateWithoutTax = intPlanRate
                        # sg.popup_no_titlebar("12")
                        if values["TAX"] == "GST" or values["TAX"] == "gst":
                            intTotal = int((intRateWithoutTax * intTaxRate * 2 / 100) + intRateWithoutTax)
                            values["TOTALTAX"] = int((intRateWithoutTax * intTaxRate * 2 / 100))
                            # sg.popup_no_titlebar(intTotal)
                        else:
                            intTotal = int((intRateWithoutTax * intTaxRate / 100) + intRateWithoutTax)
                            values["TOTALTAX"] =int((intRateWithoutTax * intTaxRate / 100))
                            # sg.popup_no_titlebar(intTotal)
                        values["AMOUNT"] = AmountinWords(intTotal) + " RUPEES ONLY"
                        # sg.popup_no_titlebar("13")
                        values["TOTAL"] = intTotal
                        # sg.popup_no_titlebar("14")
                        doc.render(values)
                        # sg.popup_no_titlebar("15")
                        pa = Path.cwd()/ "qtn_.docx"

                        # sg.popup_no_titlebar("16")
                        try:
                            doc.save(pa)

                            # sg.popup_no_titlebar("17")
                            outpath = settings["SavePDF"]["FilePath"]
                            # sg.popup_no_titlebar(outpath)
                            if(outpath and Path(outpath).exists()):

                                outpath = outpath+"/QTN_" + values["QUOTATION"] + ".pdf"

                                convert("qtn_.docx", outpath)
                                window.disappear()
                                sg.popup_no_titlebar("Saved successfully!!")
                                window.reappear()
                                
                        except Exception as e:
                            if hasattr(e, 'message'):
                                sg.popup_no_titlebar(e.message)
                            else:
                                sg.popup_no_titlebar(e)

                        else:
                            keys_to_clear = ["RECEPIENT", "RECEPIENTNUM", "PROJECT", "RATEPERHOUR",  "TAX",
                                         "TAXRATE"]
                            for key in keys_to_clear:
                                # sg.popup_no_titlebar("20")
                                window[key]('')
                                # sg.popup_no_titlebar("21")
                            i = values["QUOTATION"]
                            # sg.popup_no_titlebar("22")
                            i = int(i)+1
                            settings["Quotation"]["Number"] = str(i)
                            # sg.popup_no_titlebar("Quote number incremented")
                            # window.disappear()
                            # sg.popup_no_titlebar("Saved successfully!!")
                            # window.reappear()
            else:
                window.disappear()
                sg.popup_no_titlebar("Please fill the required fields")
                window.reappear()

    window.close()

if __name__ == "__main__":
    SETTINGS_PATH =Path.cwd()
    
    settings = sg.UserSettings(path = SETTINGS_PATH, filename = "Config.ini", use_config_file=True,convert_bools_and_none=True)
   
    theme = settings["GUI"]["theme"]
    sg.theme(theme)
    main_window()


