@echo off 
REM Used in conjunction with psexec to disable psremoting.. remotely 
REM The registry key is what allows or disallows people to create a remote session based on credentials
REM 
powershell "Disable-PSRemoting -Force"
powershell "Set-ItemProperty –Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System –Name LocalAccountTokenFilterPolicy –Value 0 -Type DWord"
