; The name of the installer
Name "Number Jumbler Installer"

; The file to write
OutFile "Number Jumbler Installer.exe"

; The default installation directory
InstallDir C:\Number_Jumbler

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

;--------------------------------

; The stuff to install
Section "Files (required)"

SectionIn RO

; Set output path to the installation directory.
SetOutPath $INSTDIR

; Put file there
File "NJ.exe"
File "Choose.txt"
File "Intro_and_Rules.txt"
File "Menu.txt"
File "Save.json"
File "Splash.txt"

SectionEnd

; Optional section (can be disabled by the user)

Section "Desktop Shortcut" SHORTCUT
    SetOutPath "$INSTDIR"
    CreateShortcut "$DESKTOP\Number Jumbler.lnk" "$INSTDIR\NJ.exe" "" 
SectionEnd
