#!/usr/bin/env bash

SCRIPT_VERSION="1.0"

LOG_FILE="BuildLinux.log"
LOG_TO_FILE=false
COMMAND=""

# Log function to output to console and optionally to a log file
log() {
    if $LOG_TO_FILE; then
        echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
    else
        echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
    fi
}

# Log the start of the script and version
log "Starting Build_Linux.sh - Version $SCRIPT_VERSION"

# Command function for 'command1'
execute_command1() {
    log "Executing executable step..."

    log "Executing PyInstaller"

    uv run pyinstaller --onedir --name RoleEngineA2 --noconfirm --add-data "Assets:Assets" --icon="Assets/Images/Icons/logo.png" RoleEngineA2.py

    log "Finished PyInstaller"

    log "Creating .desktop"

    printf "[Desktop Entry]\nType=Application\nName=RoleEngineA2\nComment=A Game Engine Made On Top Of Pygame\nExec=./RoleEngineA2-x86_64.AppImage\nIcon=RoleEngineA2\nTerminal=false\nCategories=Development;\n" > RoleEngineA2.desktop

    log "Created .desktop"

    log "Completed executable step."
}

# Command function for 'command2'
execute_command2() {
    log "Executing appimage creation step..."
    
    #Copy the files
    cp RoleEngineA2.desktop dist/RoleEngineA2/RoleEngineA2.desktop && cp logo.svg dist/RoleEngineA2/RoleEngineA2.svg && cp logo.svg Assets/Images/Icons/logo.svg && cp logo_small.svg Assets/Images/Icons/logo_small.svg && ln -s $PWD/dist/RoleEngineA2/RoleEngineA2 $PWD/dist/RoleEngineA2/AppRun && ./tools/subprojects/AppImageTool/appimagetool dist/RoleEngineA2

    log "Completed appimage creation step."
}

execute_command1
execute_command2

# Log the end of the script execution
log "Completed Build_Linux.sh - Version $SCRIPT_VERSION"