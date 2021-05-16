import re
import os
import subprocess
import requests #pip install requests

def downloud_file_requests(url,file_name, chunk_size = 8192):
    r = requests.get(url,stream=True)
    Download_erfolg = False
    if(r.status_code == 200):
        #file_len = len(r.content)
        file_len = r.headers.get('Content-Length')
        try:
            file_len = int(file_len)
        except ValueError:
            return Download_erfolg
        #end try
        save_len = 0
        prozent = 100/file_len
        prozent_schritt = 5
        prozent_anzeigen = list(range(100 + prozent_schritt,0,-prozent_schritt))#in prozent_schritt
        aktuelle_prozent = 0
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size):
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
#end downloud_file_requests

def create_wget_log() -> str:
    directory = os.getcwd()
    double_slash_index = directory.rfind("\\")+1
    log_name = directory[double_slash_index:] + '.log'
    return log_name
#end create_wget_log_link

def cut_out_wget_status(wget_output :str) ->str:
    successful_status = '\[1\]' #[1] wird fuer re modul angepasst
    search_patern = 'URL:http.+->.+' +successful_status
    match = re.search(search_patern,wget_output)
    status_str = str(match.group()) if (match != None) else ''
    return status_str
#end cut_out_wget_status

def check_downloud_status(output_str :str) ->bool:
    wget_status = cut_out_wget_status(output_str)
    downl_status = False if ( wget_status == '') else True
    return downl_status
#end find_downloud_status

def downloud_wget_win(link :str, name_link = '', wget_log = 'off/on', output = False) -> bool:
    #Leerzeichen am Ende jeden Befehls nicht vergessen
    str_add = ' '
    wget_path = r'path C:\Program Files (x86)\WgetGnuWin32\bin' + str_add
    wget_log_name = 'wget.log' + str_add
    cmd_trenzeichen = '&&' + str_add
    log_befehl = '-a' + str_add + wget_log_name if (wget_log == 'on' or wget_log == 'On' or wget_log == True) else ''
    name_befehl = '-O' + str_add + name_link + ' ' if ( name_link != '') else ''
    downl_befehl = wget_path + cmd_trenzeichen + 'wget -c -nv' + str_add + log_befehl + name_befehl + link
    process  = subprocess.run(downl_befehl,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True )
    wget_output = process.stderr
    if output : print(wget_output)
    return check_downloud_status(wget_output)
    #process  = subprocess.Popen(downl_befehl,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True )
    #output, errors = process.communicate()
    #process.wait()
#end downloud_wget_win

def create_wget_command():
    pass
#end create_wget_befehl

def downloud_wget_linux(link :str, name_link = '', wget_log = 'off/on', output = False)-> bool:
    pass
#end downloud_wget_linux

def check_system() -> str:
    system = ''
    win_sys = 'win'
    linux_sys = 'linux'
    win_str = '\\'
    linux_str = '/'
    test_str = ' '
    slasch_str = os.path.join(test_str, test_str)
    slasch_str = slasch_str.replace(test_str,'')
    sys_output_str = slasch_str.replace(test_str,'')
    if (sys_output_str ==  win_str):
        system = win_sys
    elif (sys_output_str ==  linux_str):
        system = linux_sys
    else:
        print('System wurde nicht erkant', 'wget_python.py','Funktion: check_system')
    #end if
    return system
#end check_system


def main():
    link = "https://h32.mangas.rocks/auto/47/39/65/ZCD_294_006.jpg_res.jpg?t=1621187506&u=0&h=5BHwYS2NTNvd3xvxR34LhQ"
    name = 'page.jpg'
    status1 = downloud_wget_win(link, name_link=name,output=True)
    print(status1)
    status2 = downloud_file_requests(link,name)
    print(status2)
#end main

if __name__ == '__main__':
    main()
    print(check_system())