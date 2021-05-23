import re

def find_duplikate_in_liste(suche_str, liste_str):
    gefunden_flag = False
    for elem in liste_str:
        if ( suche_str == elem ):
            gefunden_flag = True
    return gefunden_flag
#def find_duplikate_in_liste

def load_urls(datei_name):
    output_liste = []
    with open(datei_name, "rt", encoding="UTF-8") as file:
        for zeile in file:
            string = zeile
            #Uberprufe nach Kommentare
            result = re.search('\s*#',string)
            if( result != None):
                string = string[:result.end()-1]
            string = string.replace("\n","")
            if ( ( string and not string.isspace() ) and not(find_duplikate_in_liste(string,output_liste)) ):
                output_liste.append(string)
    return output_liste
#def load_urls

def read_between_tags(datei, tag_start, tag_end):
    flag_read = False
    liste = []
    with open( datei, "rt", encoding="UTF-8") as file:
        for zeile in file:
            zeile = zeile.replace("\n","")
            if (zeile == tag_start):
                flag_read = True
            elif (zeile == tag_end):
                flag_read = False
            else:
                if ( flag_read and zeile !="" ):
                    liste.append(zeile)
                #end if
            #end if
    #end with
    return liste
#end read_between_tags

def save_to_file(file_name,liste):
    with open(file_name, 'tw', encoding='utf-8') as file:
        for elem in liste:
            if (elem != liste[-1]):
                file.write(elem+"\n")
            else:
                file.write(elem)
        #end for
    #end with
#end def