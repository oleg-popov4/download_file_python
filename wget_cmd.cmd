goto START
------------------------------------
Subprozess hat grosse problem mit Symbolen ^,=,\ -> Brauche ubersetzungsprotokol
set str=Я тебя раскусил, ты оборотень =  то как человек, то как баран
set str=%str:то==%
Parameter
1 - url muss immer eingegeben werden
2 - speicherort vom wget.exe
Optionale Parameter
3 - gehe in Eingegebene verzeichniss 
4 - Datei Name oder ''
5 - log Datei oder ''
------------------------------------
:START
set url=%1
set wget_verz=%2
set cd_verz=%3
set dat_name=%4
set wget_log=%5
if not defined url set url=""
if not defined wget_verz set wget_verz=""
if not defined cd_verz set cd_verz=""
if not defined dat_name set dat_name=""
if not defined wget_log set wget_log=""
echo url %url%
echo wget_verz %wget_verz%
echo cd_verz %cd_verz%
echo par3 %3
echo dat_name %dat_name%
echo wget_log %wget_log%
if %url%=="" echo "url Eingabe fehlt" & goto END 
if %wget_verz%=="" echo "path Eingabe fehlt" & goto END 
path %wget_verz%
if not %cd_verz%=="" cd /d %cd_verz%
dir
if not %dat_name%=="" (if not %wget_log%=="" goto wget_4_par )
if not %dat_name%=="" goto wget_only_3
if not %wget_log%=="" goto wget_only_4
goto wget_only_1

:wget_4_par
    echo "wget_4_par"
    wget -c -nv -a %wget_log% -O %dat_name% %url%
goto END

:wget_only_3
    echo "wget_only_3"
    wget -c -nv -O %dat_name% %url%
goto END

:wget_only_4
    echo "wget_only_4"
    wget -c -nv -a %wget_log% %url%
goto END

:wget_only_1
    echo "wget_only_1"
    wget -c -nv %url%
goto END

:END



