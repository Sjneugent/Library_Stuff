@echo off
powershell "Enable-PSRemoting -Force"
powershell "Set-Item wsman:\localhost\client\trustedhosts 10.3.0.110"
powershell "Restart-Service WinRM"