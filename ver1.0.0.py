#######MUGbot VER 2.0.0######
##########BY  SAIKA##########
#———————————————————————————#
#MODIIFYING OF THIS FILE IS##
#NOT ADVICED UNLESS YOU KNOW#
######WHAT YOU ARE DOING#####

from wxpy import *
from random import *
from math import *
from time import *
from re import *

import MUGStr_2 as MUGStr

bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
group = bot.groups().search(MUGStr.GroupName)[0]

dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')

pu = []
nm = []
rp = []
rptnxt = False
rpu = ''

@bot.register(group)       
def returner(msg):
    global pu,nm,rp,dt,rptnxt,rpu
    s = '[MUGBot]'
    f = ''
    if msg.member.puid not in pu:#第一次在群中出现的人的初始化
        pu.append(msg.member.puid)
        nm.append(msg.member.name)
        k = 0
        while (k // 100 == k % 100 // 10):
            k = randint(0,6)+randint(0,len(MUGStr.obj)-1)*10+randint(0,len(MUGStr.obj)-1)*100
        rp.append(k)
    for i in range(0,len(pu)):#群成员指针
        if msg.member.puid == pu[i]:
            tn = nm[i]
            si = i
    if (dt != (strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日'))):#jrrp更新
        for i in range(0,len(pu)):
            k = 0
            while (k // 100 == k % 100 // 10):
                k = randint(0,6)+randint(0,len(MUGStr.obj)-1)*10+randint(0,len(MUGStr.obj)-1)*100
            rp[i] = k
        dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')
    if (rptnxt == True) & (pu[si] == rpu):
        if msg.type == 'Picture':
            msg.forward(group)
        else:
            msg.forward(group,suffix = '——'+tn)
        rptnxt = False
        rpu = -1
    if msg.type == 'Picture':
        if randint(1,15) == 1:
            s += MUGStr.nnn[randint(0,len(MUGStr.nnn)-1)]
            group.send(s)
    elif msg.type == 'Text':
        if randint(1,10) == 1:
            if randint(1,3) == 1:
                s += MUGStr.atr[randint(0,len(MUGStr.atr)-1)]
                group.send(s)
            elif len(msg.text) <= 50:
                group.send(MUGStr.rpt.format(msg.text,tn))
        if (msg.text == '.jrrp') | (msg.text == '。jrrp'):
            obj1 = rp[si] % 100 // 10
            a1 = MUGStr.obj[obj1]
            a2 = MUGStr.pro[obj1]
            obj2 = rp[si] // 100
            b1 = MUGStr.obj[obj2]
            b2 = MUGStr.con[obj2]
            if rp[si]%10 == 0:
                a1 = '诸事不宜'
                a2 = ''
            elif rp[si]%10 == 6:
                b1 = '诸事皆宜'
                b2 = ''
            group.send(MUGStr.jrrp.format(tn,dt,MUGStr.luk[rp[si]%10],a1,a2,b1,b2))
    if ('.复读' in msg.text) | ('。复读' in msg.text):#手动复读
        if ' ' in msg.text:
            if len(msg.text[4:]) > 50:
                group.send(s+'爬')
            else:
                group.send(MUGStr.rpt.format(msg.text[4:],tn))
        else:
            
            rptnxt = True
            rpu = pu[si]
            group.send(MUGStr.rptn)
    if ('.rd' in msg.text) | ('。rd' in msg.text):#将rd转化为。r1d
        if (len(msg.text) == 3) | (msg.text[3:4] == ' '):
            f = '.r1d100'+msg.text[3:]
        else:
            f = '.r1d'+msg.text[3:]
    if (msg.text[0:2] == '.r') | (msg.text[0:2] == "。r"):#普通骰子
        s = ''
        t = ''
        if f == '':
            f = msg.text
        if ' ' in f:
            xx = f.split(' ')[0][2:]
            z = f[len(xx)+3:]
            x,y = xx.split('d')
            if len(y) > 1:
                y,t = findall('(\d+)(.+)',y)[0]
                if len(t) <= 1:
                    y = y+t
                    t = ''
        else:
            x = f.split('d')[0][2:]
            y = f.split('d')[1]
            z = ''
            if len(y) > 1:
                y,t = findall('(\d+)(.+)',y)[0]
                if len(t) <= 1:
                    y = y+t
                    t = ''
        dc = 0
        if (int(x) > 100) | (int(y) > 100000):
            group.send(s+'爬')
        else:
            for i in range(1,int(x)+1):
                k = randint(1,int(y))
                s += str(k)
                if i != int(x):
                    s += '+'
                elif int(x) > 1:
                    if t != '':
                        s += ')' + t
                    s += '='
                else:
                    s = ''
                    if t != '':
                        s += str(k) + ')' + t + '='
                dc += k
            if (t != '') :
                y += t
                s = '(' + s
            if (z == ''):
                group.send(MUGStr.ROLL.format(tn,x,y,s,eval('floor('+str(dc)+t+')')))
            else:
                group.send(MUGStr.ROLLn.format(z,tn,x,y,s,eval('floor('+str(dc)+t+')')))
        f = ''
    if ('.choose ' in msg.text) | ('。choose ' in msg.text):
        if ' ' in msg.text[8:]:
            x = msg.text[8:].split(' ')
        else:
            x = msg.text[8:].split('/')
        if len(x) >= 2:
            group.send(MUGStr.choice.format(x[randint(0,len(x)-1)]))
embed()
