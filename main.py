import subprocess
import time
import os
import importlib.util

def check_dependencies():
    packageNames = [ "scrapy", "scrapyrt", "requests" ]
    unInstalledPackages = []

    for pckg in packageNames:
        package_spec = importlib.util.find_spec(pckg)
        if package_spec is None:
            unInstalledPackages.append(pckg)

    return unInstalledPackages
    

def install_dependencies(unInstalledPackages):
    for pckg in unInstalledPackages:
        subprocess.run(['pip3', 'install', pckg])


def start_scrapyrt():
    scrapyrt_process = subprocess.Popen(['scrapyrt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    return scrapyrt_process


def run_console_script():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    subprocess.run(['python3', 'flight-tracker.py'])


def main():
    unInstalledPackages = check_dependencies()
    if unInstalledPackages:
        install_dependencies(unInstalledPackages)

    scrapyrt_process = start_scrapyrt()
    
    try:
        run_console_script()
    finally:
        scrapyrt_process.terminate()
        scrapyrt_process.wait()


if __name__ == "__main__":
    main()