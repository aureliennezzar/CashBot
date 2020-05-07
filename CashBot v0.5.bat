@echo off
Title [Display] Cash Bot
set version=0.5
set dirname=user
set botname=cashbot.py
set chatname=chat\cashbot_chat.py
set chatnameBat=chat\cashbot_chat.bat
set iconebot=iconelauncher.ico
set ldat=load.dat
set sldat=slack.dat
set scrdat=screen.dat
set scrdatHL=screenHL.dat
set /a delay=3000
if not exist %dirname% (
	set errmsg= "%dirname%"
	set errnb=01
	goto :errF)
cd user
if not exist bin md bin
if not exist chat md chat
:restart
cd bin
if not exist batbox.exe call :make_bb
if not exist %scrdat% echo Airserver >%scrdat%
if not exist %scrdatHL% echo Windows >%scrdatHL%
if not exist %ldat% (goto :errF)
if not exist %sldat% (goto :errF)
if not exist %iconebot% (
	set errmsg="%dirname%\%iconebot%"
	set errnb=05
	goto :errF)

if not exist %botname% (
	set errmsg="%dirname%\%botname%"
	set errnb=04
	goto :errF)
cd ..
if not exist %chatnameBat% (
	set errmsg=%dirname%\chat\%chatnameBat%"
	set errnb=02
	goto :errF)

if not exist %chatname% (
	set errmsg="%dirname%\chat\%chatname%"
	set errnb=03
	goto :errF)

cd bin

for /f "tokens=* delims=" %%c in ('type %sldat%') do set slackmod=%%c
if /I "%slackmod%"=="Hors-ligne" (goto :testHL) else (goto :test)
:testHL
set colortt=0x0C
echo offline\cashbotHL.py>%ldat%
for /f "tokens=* delims=" %%a in ('type %scrdatHL%') do (set scrmod=%%a)
goto :start
:test
set colortt=0x0A
echo cashbot.py>%ldat%
for /f "tokens=* delims=" %%a in ('type %scrdat%') do (set scrmod=%%a)
goto :start

:start
if "%scrmod%"=="Windows" (set colortt1=0x09) else (set colortt1=0x05)
for /f "tokens=* delims=" %%b in ('type %ldat%') do (set exec_bot=%%b)
if exist sauv.txt del sauv.txt >nul
if exist r*.png del r*.png >nul
if exist q.png del q.png >nul
mode 40,12
color 0B
cls
echo ษอออออออออออออออออออออออออออออออออออออป
echo บ                                     บ
echo บ                                     บ
echo บ ษออออออออป                          บ
echo บ บ        บ                          บ
echo บ ศออออออออผ                          บ
echo บ                                     บ
echo บ ษอออออออออป                         บ
echo บ บ         บ                         บ
echo บ ศอออออออออผ                         บ
echo ศอออออออออออออออออออออออออออออออออออออผ
batbox /g 16 4 /d "Slack : " /C %colortt% /D "%slackmod%" /C 0x0B
batbox /g 16 6 /d "Mode : " /C %colortt1% /D "%scrmod%" /C 0x0B
batbox /g 2 1 /c 0x0f /d "CashBot " /c 0x0E /d "V%version%" /g 4 4 /c 0x0f /d "LANCER" /g 4 8 /c 0x0f /d "OPTIONS" /g 37 1 /c 0x0C /d "X" /g 0 11 /c 0x0B
:loop
for /f "tokens=1,2,3 delims=:" %%a in ('batbox /m') do (
set c=%%c
set Y=%%b
set X=%%a
)
if %x% GEQ 2 if %x% LEQ 11 if %y% GEQ 2 if %y% LEQ 4 if %c%==1 goto :python
if %x% GEQ 2 if %x% LEQ 12 if %y% GEQ 6 if %y% LEQ 8 if %c%==1 goto :sett
if %x%==37 if %y%==1 if %c%==1 goto :exit
goto :loop

:python
mode 55,40
color 0f
cls
start taskmgr
start /REALTIME %exec_bot%
if exist sauv.txt del sauv.txt >nul
if exist r*.png del r*.png >nul
if exist q.png del q.png >nul
goto :restart

:sett
mode 40,12
cls
echo.
echo  1. Installation modules Python
echo.
echo  2. FreeShow
echo.
batbox /g 30 9 /C 0x0C /D "(R)etour" /C 0x0B
batbox /k
if %errorlevel%==49 goto :ins_modules
if %errorlevel%==50 goto :slackchat
if %errorlevel%==114 goto :start
goto :sett

:slackchat
cls
for /f "tokens=* delims=" %%a in ('type %sldat%') do set slackmod=%%a
if "%slackmod%"=="Hors-ligne" (set colortt=0x0C) else (set colortt=0x0A)
batbox /g 1 1 /C 0x0B /D "Chat Slack : " /C 0x05 /D "Free.show" /C 0x0B
batbox /g 1 3 /C 0x0B /D "Status : " /C %colortt% /D "%slackmod%" /C 0x0B
batbox /g 1 5 /D "(H)ors-ligne (L)igne (R)etour" /k
if %errorlevel%==104 goto :slack_off
if %errorlevel%==108 goto :slack_on
if %errorlevel%==114 goto :sett
goto :slackchat

:slack_off
echo Hors-ligne>%sldat%
echo offline\cashbotHL.py>%ldat%
echo Done.
goto :slackchat
:slack_on
echo En ligne>%sldat%
echo cashbot.py>%ldat%
echo Done.
goto :slackchat

:ins_modules
mode 75,12
cls
echo Voulez-vous installer les modules Python pour Cash Bot ? (o/n)
echo Cela va prendre quelques minutes...
batbox /k
if %errorlevel%==111 (goto :ins_modules2)
if %errorlevel%==110 (goto :sett)
goto :ins_modules
:ins_modules2
cls
echo Installation. (requests) 10 %%%
echo.
pip install requests
cls
echo Installation.. (PyQt5) 20 %%%
echo.
pip install PyQt5
cls
echo Installation... (Pillow) 40 %%%
echo.
pip install Pillow
cls
echo Installation. (numpy) 50 %%%
echo.
pip install numpy
cls
echo Installation.. (beautifulsoup4) 60 %%%
echo.
pip install beautifulsoup4
cls
echo Installation... (opencv-python) 80 %%%
echo.
pip install opencv-python
cls
echo Installation. (regex) 90 %%%
echo.
pip install regex
cls
echo Installation.. (pytesseract) 100 %%%
echo.
pip install pytesseract
:ins_m_fin
cls
echo Il ne manque plus que le module Tkinter qui se t้l้charge sur le site Activestate.com
echo ActiveTcl 8.5 instellera toute les fonctionnalit้s requises pour CashBot (sous windows)
echo.
echo Lancer le telechargement sur Google Chrome ? (o/n)
batbox /k
if %errorlevel%==111 (goto :ins_m_fin2)
if %errorlevel%==110 (goto :exit)
goto :ins_m_fin
:ins_m_fin2
start chrome.exe https://www.activestate.com/activetcl/downloads/thank-you?dl=http://downloads.activestate.com/ActiveTcl/releases/8.5.18.0/ActiveTcl8.5.18.0.298892-win32-x86_64-threaded.exe
cls
echo A vous de finir l'installation Ciao !
batbox /w 500
goto :start

:errF
cls
batbox /g 1 1 /C 0x0C /D "Erreur Fatale %errnb% " /C 0x0B /D "Fichier/Dossier %errmsg% manquant !"
batbox /w %delay%
exit

:exit
echo.
echo.
echo arret...
batbox /w500
exit

:make_bb
for %%b in (
4D534346000000005A040000000000002C000000000000000301010001000000
000000004700000001000100000800000000000000006546F2B1200062617462
6F782E65786500D7E54E4C0B040008434BB5555F685B55183F499BA06D4DB235
295311EFA4151C23E04A7C2854B2759D8EA51A92B88A14BAFCB9C9BD697A6FB8
B9B19DF32123093223F8361FF6B212F0C597227B98A26C359382B46FC38789FB
F7306E9C6011FF14D15E7FDFB9376D26854DD093FCCE39DFEFFBCE777EE7BBE7
26536F55988331D6CB7CCC34190B938116660F6F15C0F3ECE71E76E9F1F5FD97
1D91F5FD09492E09454DCD69C979219D5414551752A2A09515415684A3AFC785
793523069FE81BEEE4884E32167138D8DBAB9B890E779B791DFD0EC731E686E1
B6495F17481D8D4EC66CB9D06F37C1E2477E66ACA77BDD76A46DDAEDC341C6E6
9C8F70D8FFB805B385A48EF190DB16E4B67477B753548AFFB9497D436196B706
692B80EE0F74662083BE7ACD9FFFD50C44FC61D67453D86FB6E1A4E00A0A2A39
CFA27B6F9056E87CC54075D3F4D6AEE224CD202DF1492F913744861978D78A31
62F04FBC3F58F94678D1CC7E36C0C63E3A83286F6D14FC2BB9BB1BED1BA6691A
7B6045CD909B2F4D60E3760B74E58C63D65BF740BB1928205FFDAAB7F6097833
700AD63855CC5BEFE76E225CB8D4ACD940FAF62F506C7C81AEC745A29A2FA3CB
363D486F7CCCD931628F70D6479B863CBCB704BC49028E90AED3085E751D1BB4
DE91264D24DEBDC00B31835DDB4F52E01C02E35D6CF5DA636D468E35ACFBDDF5
1CF2FE05D35BBF8F7EE9A921EB303729E24744B4AF6F61761133E37B32BF26F3
4F7A69703452738988FBA481CE63DCA1199DA17D010EE9F92EF112C28D15F21F
A067D7EDCA50A63C655A82FFDC2AAA0A661A7B0C90270A8FE9A2A22CEDD46B69
A748ED6F1190DF67869C3C5B146BAC3BE590F6F25D2C7E067C759C1C78CCEB48
99AD8E93DFE9AD5F81D56A8C0FC13AB7B5F293EFEC3DFA21EAE1E5894E9F940E
76D5CFD73286A0328F4FDC0C14ADEBD43287BF3C81A0AA8B2E706FE3191A1A4F
D7BFF3D6E8A56FE5B7EF5FCD7A08FFB8958B569A8E59E166AF196AF08D25CB1C
29B191CC18FFF6EDFE2A7DEA0BB30D60744F985DC03883B10CAC00CBC00DA07F
2F8A877104E35C2E99CECCAB0B52F1B4124CA5788E83819D7CB7F0D334037BD8
BFC3FD002E02BBB78BDB0437E0DF5DD354FCE4442C113C1A89B01393B1D72623
A387B8C1DE884FC63A73BFBDD8BF9D242EA90BD3B2925117C8D2C1D780F3C032
B006DC060C8A87C07DB6E8478DC33B2EEA713DF36A52C91444BE9FA84FA84A49
2D8853F87F789049888BFA615DD7E45459171FF04C94B592AA45D592ACCBAA42
AB626232633B8F2BC5B27E98E20BA258DC65DD7125ABDA5A1EC2772AF101F49F
072E02CBC065E02B600DB80EDC04EE011BF639FF6D3C63454D56F42CCD6673A2
9E96F88CA6F34959496AB9126C7151D6393F9792AC5949D774B5C039B5285221
66173499178BCD6A28098DE9825AB298B45492DF11EDBFBCBF01            
) Do >>t.dat (Echo.For b=1 To len^("%%b"^) Step 2
ECHO WScript.StdOut.Write Chr^(Clng^("&H"^&Mid^("%%b",b,2^)^)^) : Next)
Cscript /b /e:vbs t.dat>batbox.ex_
Del /f /q /a t.dat >nul 2>&1
Expand -r batbox.ex_ >nul 2>&1
Del /f /q /a batbox.ex_ >nul 2>&1