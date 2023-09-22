@echo off
title REEEE

:main
cls
echo Start Loop?
pause >nul

:oop
set /a rand1=%random% %% 16
set /a rand2=%random% %% 16
set HEX=0123456789ABCDEF
call set hexcolors=%%HEX:~%rand2%,1%%
color %hexcolors%
echo Loading Variable at Memory Location:%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
ping 127.0.0.1 -n 1 -w 750> nul
goto oop