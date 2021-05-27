goto START
------------------------------------
Parameter
1 url       - url muss immer eingegeben werden
2 wget_dir  - speicherort vom wget.exe
        Optionale Parameter
3 cd_dir    - gehe in Eingegebene verzeichniss 
4 file_name  - Datei Name oder ''
5 wget_log  - log Datei oder ''
------------------------------------
:START

set url=%1
if not defined url set url=""
if %url%=="" echo "url Eingabe fehlt" & goto END
echo url %url%

set wget_dir=%2
if not defined wget_dir set wget_dir=""
if %wget_dir%=="" echo "path Eingabe fehlt" & goto END 
path %wget_dir%
echo wget_dir %wget_dir%

set cd_dir=%3
if not defined cd_dir set cd_dir=""
if not %cd_dir%=="" cd /d %cd_dir%
echo cd_dir %cd_dir%

set file_name=%4
if not defined file_name set file_name=""
echo file_name %file_name%

set wget_log=%5
if not defined wget_log set wget_log=""
echo wget_log %wget_log%

if not %file_name%=="" (if not %wget_log%=="" goto wget_4_par )
if not %file_name%=="" goto wget_only_3
if not %wget_log%=="" goto wget_only_4
goto wget_only_1

:wget_4_par
    echo "wget_4_par"
    wget -c -nv -a %wget_log% -O %file_name% %url%
goto EXIT

:wget_only_3
    echo "wget_only_3"
    wget -c -nv -O %file_name% %url%
goto EXIT

:wget_only_4
    echo "wget_only_4"
    wget -c -nv -a %wget_log% %url%
goto EXIT

:wget_only_1
    echo "wget_only_1"
    wget -c -nv %url%
goto EXIT

:EXIT