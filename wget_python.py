import re
import os
import subprocess #pip install subprocess
import requests #pip install requests

def downloud_file_requests(url,file_name, chunk_size = 8192):
    r = requests.get(url,stream=True)
    Download_erfolg = False
    if(r.status_code == 200):
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
    log_name = os.path.basename(directory)+'.log'
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

def decode_bytes_wget(input, name_link) -> None:
    system = find_system()
    unicode_decode_list = ['ansi']
    win_error_unicode = 'CP866'
    text = ''
    flag_text = False
    if (system == 'win'):
        #Teste verschiedene unicode. Name vom link muss in der ausgabe sein
        for unicode in unicode_decode_list:
            try:
                text = str(input,unicode)
                if ( name_link in text):
                    print(text)
                    flag_text = True
                    break
            except UnicodeDecodeError:
                pass
            #end try
        #end for
        if (not(flag_text)): print(str(input,win_error_unicode))
    elif (system == 'linux'):
        print('linux muss getestet werden')
        print('bytes:',input)
    else:
        print('bytes:',input)
#decode_bytes_wget

def downloud_wget(link :str, name_link = '', wget_log = 'off/on', output = False, terminal_show = False) -> bool:
    downl_befehl = create_wget_command(link, name_link = name_link, wget_log = wget_log, output = output)
    if (terminal_show):
        downl_befehl = create_wget_command(link, name_link = name_link, wget_log = wget_log, output = output, details=True)
        process = subprocess.run(downl_befehl,shell=True)
        return True
    else:
        #downl_befehl = 'path C:\\Program Files (x86)\\WgetGnuWin32\\bin && wget -c -nv -O Магия_вернувшегося_должна_быть_особенной___Gwihwanjaui_mabeob-eun_teugbyeolhaeya_habnida_Глава_№148.zip https://mangabook.org/download/gwihwanjaui-mabeobeun-teugbyeolhaeya-habnida/436169'
        process  = subprocess.run(downl_befehl,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        wget_output = process.stderr #+ process.stdin + process.stdout
        if (output) : decode_bytes_wget(wget_output, name_link)
    return check_downloud_status(str(wget_output))
#end downloud_wget

def create_wget_command(link :str, name_link = '', wget_log = 'off/on', output = False, details = False)-> str:
    system = find_system()
    str_add = ' ' #Leerzeichen am Ende jeden Befehls nicht vergessen
    wget_path = r'path C:\Program Files (x86)\WgetGnuWin32\bin' + str_add if ( system == 'win') else ''
    wget_log_name = 'wget.log' + str_add
    cmd_trenzeichen = '\n' + str_add if ( system == 'win') else ''
    log_command = '-a' + str_add + wget_log_name if (wget_log == 'on' or wget_log == 'On' or wget_log == True) else ''
    name_command = '-O' + str_add + name_link + ' ' if ( name_link != '') else ''
    wget_command = 'wget -c' + str_add if details else 'wget -c -nv' + str_add 
    downl_befehl = wget_path + cmd_trenzeichen + wget_command + log_command + name_command + link
    return downl_befehl
    #process  = subprocess.Popen(downl_befehl,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True )
    #output, errors = process.communicate()
    #process.wait()
#end create_wget_befehl

def find_system() -> str:
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
        print('System wurde nicht erkant', 'wget_python.py','Funktion: find_system')
    #end if
    return system
#end find_system


def main():
    os.chdir(r'E:\Парсинг_на_Python\download_file_python')
    link = 'ipv4.download.thinkbroadband.com/5MB.zip'
    name = 'Магия_вернувшегося_должна_быть_особенной___Gwihwanjaui_mabeob-eun_teugbyeolhaeya_habnida_Глава_№111.zip'
    name = 'test.zip'
    #status1 = downloud_wget(link, name_link=name,output=True)
    #status1 = wget_python.downloud_wget(link, name_link=name,output=True, terminal_show=True)
    #print(status1)
    #status2 = downloud_file_requests(link,name)
    #print(status2)
#end main

if __name__ == '__main__':
    print(__file__)
    print(os.path.realpath(__file__))
    main()