# Role Engine A2


## Tools Dependencies
```bash
    gpgme-dev
    libgcrypt-dev
    libcurl4-gnutls-dev
    zsync
```

## Build Steps

first run:
```bash
    uv sync
```

build executable automatically with:
```bash
    ./BuildTools.py
    ./Build_Linux.py
```

build executable manually with:
```bash
    ./BuildTools.py # Compiles AppImageTool
    cp RoleEngineA2.desktop dist/RoleEngineA2/RoleEngineA2.desktop # Copyt The Desktop File
    cp logo.svg dist/RoleEngineA2/RoleEngineA2.svg # Copy Logo To Be Used By The Desktop File
    cp logo.svg Assets/Images/Icons/logo.svg # Copy The Logo To Be Used By The Engine
    cp logo_small.svg Assets/Images/Icons/logo_small.svg # Copy The Small Logo To Be Used By The Engine
    ln -s $PWD/dist/RoleEngineA2/RoleEngineA2 $PWD/dist/RoleEngineA2/AppRun # Create A Symbolic Link For The AppImage Creation Step
    ./tools/subprojects/AppImageTool/appimagetool dist/RoleEngineA2 # Creates The AppImage
```