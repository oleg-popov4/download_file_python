import os
import subprocess

def special_character_to_int(string :str) ->str:
    char_list = ['=', '^','"','<','>','|', ',', '&'] 
                # 61  94  34  60  62  124  44   38
    output = string[:]
    add_str = 'ord'
    for el in char_list:
        output = output.replace(el, add_str+str(ord(el)) )
    return output
#end special_character_to_int
os.chdir(r'E:\Парсинг_на_Python\download_file_python')
par1 = '1'
par2 = special_character_to_int('1=&|1^')
par3 = '3'
par4 = '4'
prozess = subprocess.run(['test_cmd.cmd',par1,par2,par3,par4],shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(str(prozess.stdout,'CP866'))
