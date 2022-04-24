#!/usr/bin/env python3

import psutil

def get_freecell_pid():

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])

            if 'freecell.exe' in pinfo['name'].lower():
                return pinfo['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return -1


if __name__ == '__main__':
    print(get_freecell_pid())
