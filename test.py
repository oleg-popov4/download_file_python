import wget_python
import os

if __name__ == '__main__':
    os.chdir(r'E:\Парсинг_на_Python\download_file_python')
    link = 'https://mangabook.org/download/gwihwanjaui-mabeobeun-teugbyeolhaeya-habnida/436169'
    name = 'Магия_вернувшегося_должна_быть_особенной___Gwihwanjaui_mabeob-eun_teugbyeolhaeya_habnida_Глава_№148.zip'
    link = 'ipv4.download.thinkbroadband.com/5MB.zip'
    name = 'Магия.zip'
    name = 'test123.zip'
    #status1 = wget_python.downloud_wget(link, name_link=name,output=True, terminal_show=True)
    status1 = wget_python.downloud_wget(link, name_link=name,output=True)
    print(status1)