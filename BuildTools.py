#!.venv/bin/python
import subprocess
import sys
from pathlib import Path
sys.tracebacklimit = 0

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

SETTINGSLIST = [
    ["builddir", "tools"],
    ["reconf", False],
    ["wipe", False],
    ["configureSubmodule", True],
    ["configureProject", True],
]

def isEveryOptionFalse():
    SettingsBool = []
    for Setting in SETTINGSLIST:
        if type(Setting[1]) is bool:
            SettingsBool.append(Setting[1])

    if SettingsBool.count(False) == 4:
        return True
    else:
        return False

def CheckForFolder(_path = ""):
    folderPath=Path(_path)
    if not folderPath.is_dir():
        raise FileNotFoundError(f"Directory Does Not Exist; Enable Both Configure Submodule and Configure Project or Reconf")


def run_meson_build(build_dir=SETTINGSLIST[0]):
    # 1. Configure the build (equivalent to 'meson setup build')
    # Note: Replace 'meson' with 'python -m mesonbuild.mesonmain' if meson is not in PATH

    # builddir [0][1]
    # reconf [1][1]
    # wipe [2][1]
    # configureSubmodule [3][1]

    print(
        f"""[]--------Settings--------[]\n
      {SETTINGSLIST[0][0]} : {SETTINGSLIST[0][1]}
      {SETTINGSLIST[1][0]} : {SETTINGSLIST[1][1]}
      {SETTINGSLIST[2][0]} : {SETTINGSLIST[2][1]}
      {SETTINGSLIST[3][0]} : {SETTINGSLIST[3][1]}
      {SETTINGSLIST[4][0]} : {SETTINGSLIST[4][1]}
    """
    )

    submoduleError = False

    if SETTINGSLIST[3][1] is True:
        try:
            setup_cmd = ["git", "submodule", "update", "--init", "--recursive"]
            print(f"\nRunning: {RED}{' '.join(setup_cmd)}{RESET}\n")
            subprocess.run(setup_cmd, check=True)
        except RuntimeError:
            print(f"\n{RED}-- Submodules Not Configured --{RESET}\n")
            submoduleError = True
        finally:
            if submoduleError is False:
                print(f"\n{GREEN}-- Submodules Configured --{RESET}\n")

    if SETTINGSLIST[1][1] is False and SETTINGSLIST[2][1] is False and SETTINGSLIST[4][1] is True:
        try:
            setup_cmd = ["meson", "setup", SETTINGSLIST[0][1]]
            print(f"\nRunning: {RED}{' '.join(setup_cmd)}{RESET}\n")
            subprocess.run(setup_cmd, check=True)
        finally:
            print(f"\n{GREEN}-- Project Configured --{RESET}")
    elif SETTINGSLIST[1][1] is True:
        try:
            setup_cmd = ["meson", "setup", "--reconfigure", SETTINGSLIST[0][1]]
            print(f"\nRunning: {RED}{' '.join(setup_cmd)}{RESET}\n")
            subprocess.run(setup_cmd, check=True)
        finally:
            print(f"\n{GREEN}-- Project Configured --{RESET}")
    elif SETTINGSLIST[2][1] is True:
        try:
            setup_cmd = ["meson", "setup", "--wipe", SETTINGSLIST[0][1]]
            print(f"\nRunning: {GREEN}{' '.join(setup_cmd)}{RESET}\n")
            subprocess.run(setup_cmd, check=True)
        finally:
            print(f"\n{GREEN}-- Project Configured --{RESET}")
    elif isEveryOptionFalse():
        pass
    else:
        raise RuntimeError("-- Uncheck either <reconf> or <wipe> to proceed --")

    CheckForFolder(SETTINGSLIST[0][1])

    # 2. Build the project (equivalent to 'ninja -C build' or 'meson compile -C build')
    try:
        compile_cmd = ["meson", "compile", "-C", SETTINGSLIST[0][1]]
        print(f"\nRunning: {RED}{' '.join(compile_cmd)}{RESET}\n")
        subprocess.run(compile_cmd, check=True)
    except:
        raise RuntimeError(f"\nCould Not Compile\n")


if __name__ == "__main__":
    run_meson_build()
