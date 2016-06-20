#!/usr/bin/python3
import sys

ofst=0
def disp(s=''):
    global ofst
    print(ofst*'  '+s)

def incr(n=1):
    global ofst
    ofst+=n

def decr(n=1):
    global ofst
    ofst-=n

def bf_move_right(n):
    disp("i+="+str(n))

def bf_move_left(n):
    disp("i-="+str(n))

def bf_incr(n):
    disp("m[i]+="+str(n))

def bf_decr(n):
    disp("m[i]-="+str(n))

def bf_begin(n):
    for i in range(n):
        disp("while m[i]:")
        incr()

def bf_end(n):
    disp()
    decr(n)

def bf_read(n):
    disp("c+="+str(n))
    disp("m[i]=ord(a[c-1]) if c>0 and len(a)>=c else 0")

def bf_print(n):
    disp("print(chr(m[i])"+(("*"+str(n)) if n>1 else "")+",end='')")

def bf_debug(n):
    return 0

translator = {
        '>':bf_move_right,
        '<':bf_move_left,
        '+':bf_incr,
        '-':bf_decr,
        '[':bf_begin,
        ']':bf_end,
        ',':bf_read,
        '.':bf_print,
        '#':bf_debug,
        }

def init(ms=0):
    header="""
#!/usr/bin/python3
import sys
s="""+str(ms)+"""
m=[0 for i in range(s)]
i=0
c=0
d=1
a=sys.argv[1] if len(sys.argv)>1 else ''
"""
    disp(header)

def treat(c,n):
    try:
        translator[c](n)
    except:
        return 0

if __name__=='__main__':
    filename=sys.argv[1]
    memsize=sys.argv[2]
    with open(filename) as f:
        init(memsize)
        p=f.read(1)
        c=f.read(1)
        while p:
            n=1
            while c == p:
                n+=1
                c=f.read(1)
            treat(p,n)
            p=c
            c=f.read(1)
