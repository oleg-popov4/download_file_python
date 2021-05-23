#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import sys
import os
import requests #pip install requests 
import subprocess #pip install subprocess.run
from PyQt5.QtWidgets import (QFileDialog, QApplication) #pip install PyQt5 pip install pyqt5-tools
import download_file_23_05 as download_file
#import platform
#import platform print (platform.system())
#Текущая рабочая директория возвращается os.getcwd()

#-----------------------------------------------
#-----------------------Einstelungen------------
#os.chdir(r"E:\Video WD\Temp\X Manga\Parsing_Python_Manhva\Test")
Benutzer_eingabe = True
Save_fail_liste = False
Trenzeichen_liste = '$'
Folder_create_Patern = 'Folder_name'
Subfolder_create_Patern = 'Subfolder_name'
Chunk_size = 8192
Bildformat_default = '_def.png'
DOWNLOUD_PROGRAMM = 2 #1)Linux wget 2)Python requests funktion Rest) Teste alle Variablen 
#-----------------------Einstelungen------------
#-----------------------------------------------


#-----------------------------------------------
#-----------------------------------------------

#Datei_name = None#'Links_Downloud.txt' # or None
#Download_verzeichniss = os.path.abspath(Datei_name)[:-len(Datei_name)] if Datei_name != None else QFileDialog.getExistingDirectory()
#Download_verzeichniss = os.path.abspath(Datei_name).replace(Slash_win_linux+Datei_name,'')
#-----------------------------------------------
#-----------------------------------------------

def read_liste(datei_name):
    output_liste = []
    with open(datei_name, "rt", encoding="UTF-8") as file:
        for zeile in file:
            string = zeile
            string = string.replace("\n","")
            if ( ( string and not string.isspace() ) ):
                output_liste.append(string)
    return output_liste
#end read_liste

def save_liste_to_file(file_name,liste):
    with open(file_name, 'tw', encoding='utf-8') as file:
        for elem in liste:
            file.write(elem+"\n")
        #end for
    #end with
#end def

def uberprufe_path (path,element):
    if (path == ''):
        print('Problem mit path beim Element = ' + element)
        return False
    else:
        return True
#end uberprufe_path

def uberprufe_string(string):
    if ( len(string)!=2 ):
        print("Problem mit Trenzeichen.")
        print('Programm beendet')
        return False
    else:
        return True
#end uberprufe_string

def make_folder(absolut_path):
    if os.path.isdir(absolut_path):
        print("Verzeichniss exestiert bereits")
        return True
    else:
        print("Verzeichniss wird erzeugt")
        try:
            os.makedirs(absolut_path)
        except OSError:
            print ("Создать директорию %s не удалось" % absolut_path)
            return False
        else:
            print ("Успешно создана директория %s" % absolut_path)
            return True
#end make_folder

def downloud_datei(absolut_path,datei_name,datei_url):
    output_success = False
    if (DOWNLOUD_PROGRAMM == 1):
        #Nur fuer Linux
        os.chdir(absolut_path)
        subprocess.call(["wget", "-c", "-nv", "-a", "wget.log", "-O", datei_name, datei_url])
        output_success = True
    elif (DOWNLOUD_PROGRAMM == 2):
        #Meine eigene Funktion, universel
        try:
            download = download_file.DownloadFile(datei_url,os.path.join(absolut_path,datei_name))
            output_success = download.dowload_status
            #output_success = downloud_file_requests(datei_url,os.path.join(absolut_path,datei_name))
        except:
            output_success = False
    else:
        #Prufe ob datei_url ein link ist!
        print('absolut_path = ' + absolut_path)
        print('datei_name = ' + datei_name)
        print('datei_url = ' + datei_url)
        output_success = True
    return output_success
#end downloud_datei

def downloud_file_requests(url,file_name):
    r = requests.get(url,stream=True)
    Download_erfolg = False
    if(r.status_code == 200):
        #file_len = len(r.content)
        file_len = r.headers.get('Content-Length')
        file_len = int(file_len)
        save_len = 0
        prozent = 100/file_len
        prozent_schritt = 5
        prozent_anzeigen = list(range(100 + prozent_schritt,0,-prozent_schritt))#in prozent_schritt
        aktuelle_prozent = 0
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(Chunk_size):
                save_len = save_len + len(chunk)
                f.write(chunk)
                save_prozent = round(prozent * save_len,1)
                if (save_prozent > aktuelle_prozent or save_prozent == aktuelle_prozent):
                    anzeige = round(save_len*prozent,1)
                    anzeige = str( anzeige )+ '%'
                    print( anzeige, end=' ',flush=True )
                    aktuelle_prozent = prozent_anzeigen.pop()
            #end for
        #end with
    else:
        print("Website ist offline?")
        return False
    if ( save_len == file_len ):
        print('\nDownload von ' + file_name + ' erfolgreich abgeschlossen [1]')
        Download_erfolg = True
    return Download_erfolg
#end downloud_file

def find_file_extension_from_link(str_link):
    alle_bild_formate = [ 
        '.jpg','.jpe','.jpeg','.png','.bmp','.gif','.tif','.cdr','.svg','jfif','.ico','.webp','.esp'
                        ]
    for iter in alle_bild_formate:
        if  ( iter in str_link ):
            return iter
        #end if
    #end for
    return Bildformat_default
#end find_file_extension_from_link

def begin_downloud_liste(downloud_list:list, download_verzeichniss=os.getcwd()) -> list:
    output_fail_liste = []
    path = ''
    temp_path = ''
    Verzeichniss_flag = False
    for element in downloud_list:
        string = element.split(Trenzeichen_liste)
        if ( not(uberprufe_string(string)) ):
            output_fail_liste = downloud_list
            return output_fail_liste
        else:
            first_str = string[0]
            second_str = string[1]
        #end if
        if ( first_str == Folder_create_Patern ):
            output_fail_liste.append(element)
            path = download_verzeichniss
            os.chdir(path)
            print('Neues Manga begint. Gehe in Skript verzeichnis :' + path)
            if ( uberprufe_path (path,element) ): 
                path = os.path.join(path, second_str)
                temp_path = path
                print('Neues Manga Name erkannt. Erzeuge einen Ordner dafur')
                Verzeichniss_flag = make_folder(temp_path)
            #end if
        elif ( first_str == Subfolder_create_Patern):
            output_fail_liste.append(element)
            if ( uberprufe_path (path,element) ):
                temp_path = os.path.join(path,second_str)
                Verzeichniss_flag = make_folder(temp_path)
                #print('Neues Chapter erkannt. Erzeuge einen Ordner dafur')
                #print('Erzeuge ein Ordner in ' + temp_path + ' verzeichniss')
            #end if
        else:
            if ( uberprufe_path (temp_path,element) ):
                #Name der Datei mit endung erganzen
                datei_endung = find_file_extension_from_link(second_str)
                first_str = first_str if datei_endung in first_str else first_str+datei_endung
                if ( Verzeichniss_flag ):
                    erfolg = downloud_datei(temp_path,first_str,second_str)
                else:
                    print('Problem mit verzeichniss. Die Datei wir in ' + download_verzeichniss + 'gespeichert')
                    erfolg = downloud_datei(download_verzeichniss,first_str,second_str)
                if ( not(erfolg) ): output_fail_liste.append(element)
            #end if 
        #end if
    #end for
    return output_fail_liste
#end begin_downloud_liste

def ask_user():
    #Fenster fuer benutzer eingaben
    app = QApplication(sys.argv)
    Datei_names = QFileDialog.getOpenFileNames(None, "Select a file...",filter="*.txt")
    download_verzeichniss = QFileDialog.getExistingDirectory()
    download_verzeichniss = download_verzeichniss if download_verzeichniss !='' else os.getcwd()
    del app
    return (Datei_names,download_verzeichniss)
#end ask_user

def main(Datei_names,download_verzeichniss):
    download_fail_liste = []
    #Schleife uber alle listen
    for down_datei_str in Datei_names[0]:
        downloud_list = read_liste(down_datei_str)
        resultat_liste = begin_downloud_liste(downloud_list,download_verzeichniss)
        download_fail_liste.extend(resultat_liste)
    if (Save_fail_liste):
        list_name ='fail_liste_' + datetime.datetime.today().strftime("%d_%m_%Y_%H_%M_%S") + '.txt'
        save_liste_to_file(list_name,download_fail_liste)
    else:
        print(download_fail_liste)
    #Beende Programm
#end main

if __name__=='__main__':
    Datei_names = []
    download_verzeichniss = ''
    if (Benutzer_eingabe):
        Datei_names,download_verzeichniss = ask_user()
        main(Datei_names,download_verzeichniss)
        input()
    else:
        main(Datei_names,download_verzeichniss)
    sys.exit(0)

