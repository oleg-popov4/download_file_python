import os
import subprocess


def special_character_to_int(string: str) -> str:
    char_list = ['=', '^', '"', '<', '>', '|', ',', '&', ' ', '%']
    #             61  94   34    60  62   124   44  38    32   37
    output = string[:]
    add_str = 'ord'
    for el in char_list:
        output = output.replace(el, add_str + str(ord(el)))
    return output


# end special_character_to_int
os.chdir(r'E:\Парсинг_на_Python\download_file_python')
# prozess = subprocess.run(['test_cmd.cmd', par1, par2, par3, par4], shell=True, stdin=subprocess.PIPE,
#                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(str(prozess.stdout, 'CP866'))
#subprocess.run('test_cmd.cmd {0}'.format(par2), shell=True)
url = 'http://b.aaa200.rocks/auto/03/71/82/001.htm?t=1622005187&u=0&h=fPZ93hQxWKAqd65AuJwC6g'
dat_name = 'page_num_1.png'
wget_dir = r'E:\Парсинг_на_Python\download_file_python'
cd_dir =r'C:\Users\Super PC\Desktop'
subprocess.run('test_cmd.cmd "{0}" "{1}" "{2}" "{3}"'.format(url,wget_dir,cd_dir,dat_name), shell=True)


#char_list = ['1=2', '1|2', '1,2', '1&2', '1 2', '1%2']
#for el in char_list:
    #subprocess.run('test_cmd.cmd "{0}"'.format(el), shell=True)
    #subprocess.run('test_cmd.cmd "{0}" "{1}"'.format(el,'--------'), shell=True)

