import re
import os
import subprocess #pip install subprocess
import requests #pip install requests
'''
ToDo
1 Linux implementation
2 Ubeprufefile existens vor dem download, dann wget only
3 wget log file
'''

#--------------------------------
#------------Funktionen----------
def find_system(win_sys , linux_sys ) -> str:
    system = ''
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

def get_wget_cmd_dir() ->str:
    wget_cmd_name = 'wget_cmd.cmd'
    temp_cd = os.path.dirname(os.path.abspath(__file__))
    flag_wget_cmd = os.path.isfile( os.path.join(temp_cd,wget_cmd_name) )
    if (flag_wget_cmd): 
        return temp_cd
    else:
        print(wget_cmd_name,'wurde nicht gefunden und muss erzeugt werden')
        input('Program abbrechen?')
#end get_wget_cmd_dir

def create_wget_log() -> str:
    directory = os.getcwd()
    log_name = os.path.basename(directory)+'.log'
    return log_name
#end create_wget_log_link

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

#--------------------------------
#--------------------------------

class DownloadFile():
    dir_cmd = get_wget_cmd_dir()
    win_sys = 'win'
    linux_sys = 'linux'
    system = find_system(win_sys,linux_sys)

    def __init__(self, url :str, file_name = '', only_wget = False, chunk_size = 8192):
        """Constructor"""
        self.url = url
        self.dowload_status = False
        self.only_wget = only_wget
        self.stdin = ''
        self.stdout = ''
        self.stderr = ''
        #file_name kann auch mit verzeichniss angegeben werden
        temp_save_dir = os.path.dirname(file_name)
        self.aktuelle_dir = os.getcwd()
        self.save_dir = temp_save_dir if temp_save_dir !='' else self.aktuelle_dir
        self.file_name =  os.path.basename(file_name) 
        self.chunk_size = chunk_size
        self.system  = DownloadFile.system
        self.start_download()
    #end __init__

    def check_wget_downloud_status(self) ->bool:
        wget_output = self.stderr
        successful_status = '\[1\]' #[1] wird fuer re modul angepasst
        search_patern = 'URL:http.+->.+' +successful_status
        match = re.search(search_patern,wget_output)
        wget_status = str(match.group()) if (match != None) else ''
        downl_status = False if ( wget_status == '') else True
        if downl_status: print(wget_output)
        return downl_status
    #end check_downloud_status

    def start_download(self):
        if ( self.system == DownloadFile.win_sys ):
            self.wget_win()
        #end if
        self.dowload_status = self.check_wget_downloud_status()
        #wget kann versuchen download fortsetzen, deswegen gibt es only_wget
        if (not(self.dowload_status) and not(self.only_wget)):
            self.dowload_status = self.requests_bar()
    #end start_download

    def wget_win(self):
        '''
        ------------------------------------
        Parameter
        1 - url muss immer eingegeben werden
        2 - speicherort vom wget.exe
        Optionale Parameter
        3 - gehe in Eingegebene verzeichniss 
        4 - Datei Name oder ''
        5 - log Datei oder ''
        ------------------------------------
        '''
        #gehe in Verzeichniss mit 'wget_cmd.cmd
        os.chdir(self.dir_cmd)
        prozess = subprocess.run(['wget_cmd.cmd',self.url,DownloadFile.dir_cmd,self.save_dir,self.file_name],
                        shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(self.aktuelle_dir)
        if hasattr(prozess, 'stdin'):
            temp = prozess.stdin
            self.stdin = str(temp)
            self.stdin_byte = temp
        if hasattr(prozess, 'stdout'):
            temp = prozess.stdout
            self.stdout = str(temp)#'CP866'
            self.stdout_byte = temp
        if hasattr(prozess, 'stderr'):
            temp = prozess.stderr
            self.stderr = str(temp)
            self.stderr_byte = temp
    #end test_wget

    def info(self) -> None:
        print('dir_cmd:',DownloadFile.dir_cmd)
        print('system:',DownloadFile.system)
        print('aktuelle_dir:',self.aktuelle_dir)
        print('url:',self.url)
        print('name:',self.file_name)
        print('save_dir',self.save_dir)
        print('stdin:',self.stdin)
        print('stdout:',self.stdout)
        print('stderr:',self.stderr)
        print('dowload_status:',self.dowload_status)
    #end ausgabe
        

    def requests_bar(self,prozent_schritt = 5):
        url = self.url
        file_name = self.file_name
        chunk_size = self.chunk_size
        r = requests.get(url,stream=True)
        Download_erfolg = False
        if(r.status_code == 200):
            file_len = r.headers.get('Content-Length')
            try:
                file_len = int(file_len)
            except ValueError:
                return Download_erfolg
            #end try
            prozent_anzeigen = list(range(100 + prozent_schritt,0,-prozent_schritt))#in prozent_schritt
            save_len = 0
            prozent = 100/file_len
            aktuelle_prozent = 0
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size):
                    save_len = save_len + len(chunk)
                    f.write(chunk)
                    save_prozent = round(prozent * save_len,1)
                    if (save_prozent >= aktuelle_prozent):
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
    #end requests_bar


#end DownloadFile

if __name__ == '__main__':
    url = 'ipv4.download.thinkbroadband.com/5MB.zip'
    name = 'test.zip'
    cd = r'E:\Парсинг_на_Python\download_file_python\__pycache__'
    test = DownloadFile(url,os.path.join(cd,name))
    test.info()
    
