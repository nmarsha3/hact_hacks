#!/usr/bin/env python3
from ctypes import *
from ctypes.wintypes import *
import sys
import json

# Program to read the memory of the freecell process and extract information about card placement

CARD_CODE_FILE = 'card_codes.json'
EXE_FILE = 'freecell.exe'

def steal_cards(pid=None):
    '''Reads card info from the memory of the specified pid.
        If no pid is specified, attempts to find one for 'freecell.exe'
    '''

    if pid is None:
        pid = get_freecell_pid()

    # get card codes
    with open(CARD_CODE_FILE, 'r') as inFile:
        card_codes = json.load(inFile)

    # process reading code
    OpenProcess = windll.kernel32.OpenProcess
    ReadProcessMemory = windll.kernel32.ReadProcessMemory
    CloseHandle = windll.kernel32.CloseHandle

    PROCESS_ALL_ACCESS = 0x1F0FFF

    start_address = 0x01008B04 # where freecell executable stores the cards

    # create buffer to read code
    buffer = c_char_p("X".encode('utf-8'))
    bufferSize = len(buffer.value)
    bytesRead = c_ulong(0)

    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

    # initialize list
    cards = [[0]*7 for x in range(4)] + [[0]*6 for x in range(4)]


    for i in range(8):
        address = start_address + i*84 # memory offset for each row
        num_cards = 7 if i < 4 else 6

        for j in range(num_cards):
            #print("Reading row {} position {} at address {}".format(i,j,hex(address + j*4)))
            result = ReadProcessMemory(processHandle, address + j*4, buffer, bufferSize, byref(bytesRead))

            cardval = int.from_bytes(buffer.value, byteorder='big')
            cards[i][j] = tuple(card_codes[str(cardval)])


    CloseHandle(processHandle)

    return cards

def get_freecell_pid():
    '''Finds the PID corresponding to freecell.exe, if such a process is running. Returns -1 if the process was not found.
        Returns the PID of the first process it finds that matches the name, so if multiple processes with the same name are
        running, only one will be returned.
    '''
    import psutil

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])

            if EXE_FILE.lower() in pinfo['name'].lower():
                return pinfo['pid']

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return -1

if __name__ == '__main__':

    # read pid from command line or find the pid for "freecell.exe"
    if len(sys.argv) > 1:
        try:
            pid = int(sys.argv[1])
        except ValueError:
            print("ERROR: freecell.exe PID must be a valid integer")
            sys.exit(1)

    else:
        pid = get_freecell_pid()

    # steal cards from the given pid
    cards = steal_cards(pid)

    # pretty printing
    for c in cards:
        print(c)

