import re
import os
import subprocess #pip install subprocess
import requests #pip install requests

class DownloadFile():
    #--------------------------------
    #------------Funktionen----------
    def find_system(win_sys = 'win', linux_sys = 'linux') -> str:
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

    #--------------------------------
    #--------------------------------
    verzeichniss = os.path.dirname(os.path.abspath(__file__))
    system = find_system()

    def __init__(self, url :str, file_name = '', chunk_size = 8192):
        """Constructor"""
        self.url = url
        self.file_name = file_name
        self.chunk_size = chunk_size
    #end __init__

    def test_wget(self, cd_param :str):
        '''
        Parameter
        1 - url muss immer eingegeben werden
        Optionale Parameter
        2 - gehe in Eingegebene verzeichniss 
        3 - Datei Name oder ''
        4 - log Datei oder ''
        '''
        subprocess.run(['wget_cmd.cmd',self.url,cd_param,self.file_name],shell=True)#, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pass
    #end test_wget

    def ausgabe(self) -> None:
        print('verzeichniss:',DownloadFile.verzeichniss)
        print('system:',DownloadFile.system)
        print('url:',self.url)
        print('name:',self.file_name)
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
    print('-----------------------')
    url = 'ipv4.download.thinkbroadband.com/5MB.zip'
    name = 'test.zip'
    cd = r'C:\Users\Super PC\Downloads'
    test = DownloadFile(url,name)
    test.ausgabe()
    test.test_wget(cd)
    
