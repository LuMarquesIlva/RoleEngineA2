# Role Engine A2

## Build Steps

first run:
```bash
    uv sync
```

build executable with:
```bash 
    uv run pyinstaller --onedir --add-data "Assets:Assets" --icon="Assets/Images/Icons/logo.png" RoleEngineA2.py
    cp RoleEngineA2.desktop dist/RoleEngineA2
    ln -s $PWD/dist/RoleEngineA2/RoleEngineA2 $PWD/dist/RoleEngineA2/AppRun
    ./tools/subprojects/AppImageTool/appimagetool dist/RoleEngineA2
```

## Tools Dependencies
```bash
    gpgme-dev
    libgcrypt-dev
    libcurl4-gnutls-dev
    zsync
```