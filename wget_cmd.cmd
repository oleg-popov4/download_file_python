goto START
------------------------------------
Parameter
1 - url muss immer eingegeben werden
Optionale Parameter
2 - gehe in Eingegebene verzeichniss 
3 - Datei Name oder ''
4 - log Datei oder ''
------------------------------------
:START
set par1=%1
set par2=%2
set par3=%3
set par4=%4
if not defined par1 set par1=""
if not defined par2 set par2=""
if not defined par3 set par3=""
if not defined par4 set par4=""
if %par1%=="" echo "url Eingabe fehlt" & goto END 
if not %par2%=="" cd /d %par2%
if not %par3%=="" (if not %par4%=="" goto wget_4_par )
if not %par3%=="" goto wget_only_3
if not %par4%=="" goto wget_only_4
goto wget_only_1

:wget_4_par
    echo "wget_4_par"
    wget -c -nv -a %par4% -O %par3% %par1%
goto END

:wget_only_3
    echo "wget_only_3"
    wget -c -nv -O %par3% %par1%
goto END

:wget_only_4
    echo "wget_only_4"
    wget -c -nv -a %par4% %par1%
goto END

:wget_only_1
    echo "wget_only_1"
    wget -c -nv %par1%
goto END

:END



