import wget_python
import os

if __name__ == '__main__':
    os.chdir(r'E:\Парсинг_на_Python\download_file_python')
    link = 'https://mangabook.org/download/gwihwanjaui-mabeobeun-teugbyeolhaeya-habnida/436169'
    name = 'Магия_вернувшегося_должна_быть_особенной___Gwihwanjaui_mabeob-eun_teugbyeolhaeya_habnida_Глава_№148.zip'
    link = 'ipv4.download.thinkbroadband.com/5MB.zip'
    name = 'Магия_вернувшегося_должна_быть_особенной___Gwihwanjaui_mabeob-eun_teugbyeolhaeya_habnida_Глава_№111.zip'
    #name = 'test.zip'
    status1 = wget_python.downloud_wget_win(link, name_link=name,output=True)
    print(status1)