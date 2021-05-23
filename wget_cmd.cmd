goto START
------------------------------------
Subprozess hat grosse problem mit Symbolen ^,=,\ -> Brauche ubersetzungsprotokol
Parameter
1 - url muss immer eingegeben werden
2 - speicherort vom wget.exe
Optionale Parameter
3 - gehe in Eingegebene verzeichniss 
4 - Datei Name oder ''
5 - log Datei oder ''
------------------------------------
:START
call :convert_int_to_char %1
set "url=%temp_str%"

call :convert_int_to_char %2
set "wget_verz=%temp_str%"

call :convert_int_to_char %3
set "cd_verz=%temp_str%"

call :convert_int_to_char %4
set "dat_name=%temp_str%"

call :convert_int_to_char %5
set "wget_log=%temp_str%"

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


:convert_int_to_char
rem ['=','^', '"', '<', '>', '|', ',', '&'] 
rem   61  94  34   60   62   124   44   38
set temp_str=%1
if not defined temp_str set temp_str=""
set "temp_str=%temp_str:ord61=^=%"
set "temp_str=%temp_str:ord94=^^%"
set "temp_str=%temp_str:ord34=^"%"
set "temp_str=%temp_str:ord60=^<%"
set "temp_str=%temp_str:ord62=^>%"
set "temp_str=%temp_str:ord124=^|%"
set "temp_str=%temp_str:ord44=^,%"
set "temp_str=%temp_str:ord38=^&%"
exit /b

:END



