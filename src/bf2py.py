#!/usr/bin/python3
import sys,os
incr=0

def display(s = ""):
    global incr
    print(incr*'  '+s)

def increment():
    global incr
    incr+=1

def decrement():
    global incr
    incr-=1

def bf_move_right():
    display("i+=1")

def bf_move_left():
    display("i-=1")

def bf_incr():
    display("mem[i]+=1")

def bf_decr():
    display("mem[i]-=1")

def bf_begin():
    display("while mem[i] != 0:")
    increment()

def bf_end():
    display()
    decrement()

def bf_read():
    display("mem[i]=args[c]")
    display("c+=1")

def bf_print():
    display("print(chr(mem[i]),end='')")

translator = {
        '>':bf_move_right,
        '<':bf_move_left,
        '+':bf_incr,
        '-':bf_decr,
        '[':bf_begin,
        ']':bf_end,
        ',':bf_read,
        '.':bf_print,
        }

def treat(c):
    try:
        translator[c]()
    finally:
        return 0

def init(ms=0):
    display("#!/usr/bin/python3\nms="+str(ms)+"\nmem=[0 for i in range(ms)]\ni=0")

if __name__=='__main__':
    filename=sys.argv[1]
    memsize=sys.argv[2]
    with open(filename) as f:
        init(memsize)
        c=f.read(1)
        while c:
            treat(c)
            c=f.read(1)
