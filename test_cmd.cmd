call :convert_int_to_char %1
set "url=%temp_str%"
echo url %url%



call :convert_int_to_char %2
set "wget_verz=%temp_str%"
echo wget_verz %wget_verz%

call :convert_int_to_char %3
set "cd_verz=%temp_str%"
echo cd_verz %temp_str%
goto :EXIT

call :convert_int_to_char %4
set "dat_name=%temp_str%"
echo dat_name %temp_str%
goto :EXIT





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

:EXIT