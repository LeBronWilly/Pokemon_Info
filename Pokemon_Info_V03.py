# -*- coding: utf-8 -*-
"""
Created on 03/12, 2023
@author: Willy Fang

"""

# https://github.com/rayc2045/pokedex
# https://github.com/DetainedDeveloper/Pokedex
# https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json
# https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas
# https://practicaldatascience.co.uk/data-science/how-to-split-a-pandas-column-string-or-list-into-separate-columns
# https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
# https://stackoverflow.com/questions/45306988/column-of-lists-convert-list-to-string-as-a-new-column
# https://stackoverflow.com/questions/20167930/start-index-at-1-for-pandas-dataframe
# https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/
# https://sparkbyexamples.com/pandas/pandas-split-column/
# https://stackoverflow.com/questions/61095091/how-to-strip-and-split-in-pandas
# https://stackoverflow.com/questions/20025882/add-a-string-prefix-to-each-value-in-a-string-column-using-pandas
# https://ithelp.ithome.com.tw/articles/10293715
# https://stackoverflow.com/questions/3558786/setting-a-plain-background-color-for-a-qgraphicsview-widget


from UI_V03 import *
# from PySide2.QtWidgets import QMessageBox
# from PySide2 import QtGui
from PySide2 import QtWidgets
import pandas as pd
import urllib.request
import json
# import numpy as np
# import os
from warnings import filterwarnings

filterwarnings("ignore")


# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 500)


def Pokemon_data_refresh_ETL():
    species_strength = pd.read_csv(
        "https://raw.githubusercontent.com/LeBronWilly/Pokemon_Info/main/data/info/Pokemon_Species_Strength.csv",
        encoding='utf8')
    type_chart = pd.read_csv("https://raw.githubusercontent.com/LeBronWilly/Pokemon_Info/main/data/info/Type_Chart.csv",
                             encoding='utf8')

    # data_source = "https://raw.githubusercontent.com/rayc2045/pokedex/main/data/PokeApi.json"
    data_source = "https://raw.githubusercontent.com/LeBronWilly/Pokemon_Info/main/data/info/PokeApi.json"
    json_url = urllib.request.urlopen(data_source)
    data = json.loads(json_url.read())
    pokemon_data = pd.json_normalize(data)
    pokemon_data.columns = ['ID', 'Name_EN', 'Name', "Type_EN", "Type", "Genus_EN", "Genus", "Desc_EN", "Desc"]
    pokemon_data["Type_EN"] = [', '.join(map(str, lst)) for lst in pokemon_data["Type_EN"]]
    pokemon_data["Type"] = [', '.join(map(str, lst)) for lst in pokemon_data["Type"]]
    pokemon_data["Desc_EN"] = ['\n⭐️'.join(map(str, lst)) for lst in pokemon_data["Desc_EN"]]
    pokemon_data["Desc"] = ['\n⭐️'.join(map(str, lst)) for lst in pokemon_data["Desc"]]
    pokemon_data["Desc_EN"] = "⭐️" + pokemon_data["Desc_EN"]
    pokemon_data["Desc"] = "⭐️" + pokemon_data["Desc"]
    pokemon_data[['Type1', 'Type2']] = pokemon_data["Type"].str.split(",", expand=True)
    pokemon_data['Type2'] = pokemon_data['Type2'].apply(lambda x: x.strip() if x != None else "")
    pokemon_data["ID_Name"] = pokemon_data["ID"].astype(str) + ". " + pokemon_data["Name"]
    pokemon_data = pokemon_data[["ID_Name", 'ID', 'Name', 'Name_EN', "Type1", "Type2", "Type", "Type_EN",
                                 "Genus", "Genus_EN", "Desc", "Desc_EN"]]
    pokemon_data = pokemon_data.merge(species_strength.drop(columns=["#", "Name"]),
                                      how="left", on="ID", validate="one_to_many")
    pokemon_data.index += 1
    return pokemon_data


class AppWindow(QWidget):  # Reusable
    def __init__(self):  # Reusable
        super().__init__()
        self.ui = Ui_Pokemon_Info()  # Ui底線後面改名稱
        self.ui.setupUi(self)
        print("Loading Pokémon Data......")
        self.Pokemon_data_source = Pokemon_data_refresh_ETL()
        self.Pokemon_data = self.Pokemon_data_source.copy()
        self.Pokemon_img = QPixmap()
        self.setup_control()
        self.show()

    def setup_control(self):  # Reusable
        self.ui.WinIcon_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/Pokemon_Info/main/pokeball.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.WinIcon_img.loadFromData(img_data)
        self.ui.WinIcon_img = self.ui.WinIcon_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.WinIcon_img))
        self.ui.Pokemon_Image.setScene(QtWidgets.QGraphicsScene())
        self.ui.Pokemon_Image.setBackgroundBrush(QBrush(Qt.black, Qt.SolidPattern))

        self.ui.KeyWord_Text.clear()
        self.ui.Pokemon_ComboBox.clear()
        self.ui.Pokemon_ComboBox.addItem("Choose Pokémon")
        self.ui.Pokemon_ID_Name = sorted(set(self.Pokemon_data["ID_Name"]), key=lambda x: int(x.split('.')[0]))
        for ID_Name in self.ui.Pokemon_ID_Name:
            self.ui.Pokemon_ComboBox.addItem(ID_Name)
        self.ui.Pokemon_ComboBox.setCurrentIndex(25)  # 初始預設皮卡丘

        self.ui.Type_ComboBox.clear()
        self.ui.Type_ComboBox.addItem("All Types")
        self.ui.Pokemon_Type = sorted(set(self.Pokemon_data["Type1"]))
        for PType in self.ui.Pokemon_Type:
            self.ui.Type_ComboBox.addItem(PType)

        self.ui.Search_Button.clicked.connect(
            lambda: self.Search_Button_Clicked(self.ui.Pokemon_ComboBox.currentText()))
        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)
        self.Search_Button_Clicked(self.ui.Pokemon_ComboBox.currentText())

        self.ui.Type_ComboBox.currentTextChanged.connect(
            lambda: self.Filter_Change(self.ui.KeyWord_Text.text().strip(), self.ui.Type_ComboBox.currentText()))
        self.ui.KeyWord_Text.textChanged.connect(
            lambda: self.Filter_Change(self.ui.KeyWord_Text.text().strip(), self.ui.Type_ComboBox.currentText()))

    def Filter_Change(self, Pokemon_Name_Keyword, Pokemon_Type):
        if Pokemon_Type is None:
            return None

        self.Pokemon_data = self.Pokemon_data_source.copy()
        if Pokemon_Type == "All Types" and Pokemon_Name_Keyword != "":
            self.Pokemon_data = self.Pokemon_data[
                self.Pokemon_data["Name"].str.contains(Pokemon_Name_Keyword, regex=False)]
        elif Pokemon_Type == "All Types" and Pokemon_Name_Keyword == "":
            pass
        elif Pokemon_Type != "All Types" and Pokemon_Name_Keyword != "":
            self.Pokemon_data = self.Pokemon_data[self.Pokemon_data["Type"].str.contains(Pokemon_Type, regex=False)]
            self.Pokemon_data = self.Pokemon_data[
                self.Pokemon_data["Name"].str.contains(Pokemon_Name_Keyword, regex=False)]
        elif Pokemon_Type != "All Types" and Pokemon_Name_Keyword == "":
            self.Pokemon_data = self.Pokemon_data[self.Pokemon_data["Type"].str.contains(Pokemon_Type, regex=False)]
        else:
            return None

        self.ui.Pokemon_ComboBox.clear()
        self.ui.Pokemon_ComboBox.addItem("Choose Pokémon")
        self.ui.Pokemon_ID_Name = sorted(set(self.Pokemon_data["ID_Name"]), key=lambda x: int(x.split('.')[0]))
        for ID_Name in self.ui.Pokemon_ID_Name:
            self.ui.Pokemon_ComboBox.addItem(ID_Name)

    def Search_Button_Clicked(self, Pokemon_ID_Name):
        selected_Pokemon_data = self.Pokemon_data[self.Pokemon_data["ID_Name"] == Pokemon_ID_Name]
        if len(selected_Pokemon_data) == 0:
            print("Please Choose Pokémon!")
            return None
        print(Pokemon_ID_Name)
        self.ui.Genus_Text.setText(selected_Pokemon_data["Genus"].values[0])
        self.ui.Type1_Text.setText(selected_Pokemon_data["Type1"].values[0])
        self.ui.Type2_Text.setText(selected_Pokemon_data["Type2"].values[0])
        self.ui.Desc_TextEdit.setText(selected_Pokemon_data["Desc"].values[0])
        # self.ui.Desc_TextEdit.setAlignment(Qt.AlignLeft)
        url = "https://raw.githubusercontent.com/LeBronWilly/Pokemon_Info/main/data/images/official-artwork/" + \
              Pokemon_ID_Name.split(".")[0] + ".png"
        img_data = urllib.request.urlopen(url).read()
        self.Pokemon_img.loadFromData(img_data)
        self.Pokemon_img = self.Pokemon_img.scaled(350, 350)
        Pokemon_scene = QtWidgets.QGraphicsScene()
        Pokemon_scene.addPixmap(self.Pokemon_img)
        self.ui.Pokemon_Image.setScene(Pokemon_scene)
        # self.ui.Pokemon_Image.setAlignment(Qt.AlignCenter)

    def Refresh_Button_Clicked(self):
        print("Refreshing Pokémon Data......")
        self.Pokemon_data_source = Pokemon_data_refresh_ETL()
        self.Pokemon_data = self.Pokemon_data_source.copy()

        self.ui.KeyWord_Text.clear()
        self.ui.Pokemon_ComboBox.clear()
        self.ui.Pokemon_ComboBox.addItem("Choose Pokémon")
        self.ui.Pokemon_ID_Name = sorted(set(self.Pokemon_data["ID_Name"]), key=lambda x: int(x.split('.')[0]))
        for ID_Name in self.ui.Pokemon_ID_Name:
            self.ui.Pokemon_ComboBox.addItem(ID_Name)
        # self.ui.Pokemon_ComboBox.setCurrentIndex(25)  # 初始預設皮卡丘

        self.ui.Type_ComboBox.clear()
        self.ui.Type_ComboBox.addItem("All Types")
        self.ui.Pokemon_Type = sorted(set(self.Pokemon_data["Type1"]))
        for PType in self.ui.Pokemon_Type:
            self.ui.Type_ComboBox.addItem(PType)

        self.ui.Genus_Text.clear()
        self.ui.Type1_Text.clear()
        self.ui.Type2_Text.clear()
        self.ui.Desc_TextEdit.clear()
        self.ui.Pokemon_Image.setScene(QtWidgets.QGraphicsScene())


if __name__ == "__main__":  # Reusable
    import sys

    app = QApplication(sys.argv)
    Pokemon_Info = AppWindow()  # 改名稱
    Pokemon_Info.show()  # 改名稱
    sys.exit(app.exec_())
