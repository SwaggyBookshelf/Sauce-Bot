$PSScriptRoot = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Set-Location $PSScriptRoot
pyinstaller --onefile --icon=n.ico --splash=n-1.3.png --window "Sauce Bot 1.0.3.py"
copy "n.ico" "dist"
copy "changelog.md" "dist"
copy "preferences.config" "dist"
copy "README.md" "dist"
cd "dist"
mkdir "Sauces"
