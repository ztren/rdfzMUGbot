#######MUGbot VER 4.0.0######
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
from copy import *
from arcaea_crawler import *

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw , ImageFont
import MUGStr

bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
group = bot.groups().search(MUGStr.GroupName)[0]

dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')

pu = []
nm = []
rp = []
rpu = ''
gru = ''

@bot.register(group)       
def returner(msg):
    global pu,nm,rp,dt,gru,rpu
    s = '[MUGBot]'
    f = ''
    if msg.member.puid not in pu:#第一次在群中出现的人的初始化
        pu.append(msg.member.puid)
        nm.append(msg.member.name)
        k = 0
        while (k // 1000 == k % 1000 // 10):
            k = randint(0,6)+randint(0,len(MUGStr.obj)-1)*10+randint(0,len(MUGStr.obj)-1)*1000
        rp.append(k)
    for i in range(0,len(pu)):#群成员指针
        if msg.member.puid == pu[i]:
            tn = nm[i]
            si = i
    if (dt != (strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日'))):#jrrp更新
        for i in range(0,len(pu)):
            k = 0
            while (k // 1000 == k % 1000 // 10):
                k = randint(0,6)+randint(0,len(MUGStr.obj)-1)*10+randint(0,len(MUGStr.obj)-1)*1000
            rp[i] = k
        dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')
    if (pu[si] == rpu):
        if msg.type == 'Picture':
            msg.forward(group)
        else:
            msg.forward(group,suffix = '——'+tn)
        rpu = ''
    if msg.type == 'Picture':
        if randint(1,15) == 1:
            s += MUGStr.nnn[randint(0,len(MUGStr.nnn)-1)]
            group.send(s)
    elif msg.type == 'Text':
        if randint(1,15) == 1:
            if randint(1,3) == 1:
                s += MUGStr.atr[randint(0,len(MUGStr.atr)-1)]
                group.send(s)
            elif len(msg.text) <= 50:
                group.send(MUGStr.rpt.format(msg.text,tn))
    if (msg.text == '.jrrp') | (msg.text == '。jrrp'):
        obj1 = rp[si] % 1000 // 10
        a1 = MUGStr.obj[obj1]
        a2 = MUGStr.pro[obj1]
        obj2 = rp[si] // 1000
        b1 = MUGStr.obj[obj2]
        b2 = MUGStr.con[obj2]
        if rp[si]%10 == 0:
            a1 = '诸事不宜'
            a2 = ''
        elif rp[si]%10 == 6:
            b1 = '诸事皆宜'
            b2 = ''
        group.send(MUGStr.jrrp.format(tn,dt,MUGStr.luk[rp[si]%10],a1,a2,b1,b2))
    elif (msg.text == '.4k') | (msg.text == '。4k'):
        group.send(MUGStr.File4K)
    elif (msg.text[0:4] == '.arc') | (msg.text[0:4] == '。arc'):
        s = msg.text[5:] if msg.text[4] == ' ' else msg.text[4:]
        group.send(MUGStr.Crawling.format(s))
        try:
            group.send(query(s))
        except Exception as e:
            group.send(MUGStr.CrawlErr.format(repr(e)))
    elif (msg.text[0:3] == '.复读') | (msg.text[0:3] == '。复读'):#手动复读
        if ' ' in msg.text:
            if len(msg.text[4:]) > 50:
                group.send(s+'爬')
            else:
                group.send(MUGStr.rpt.format(msg.text[4:],tn))
        else:
            rpu = pu[si]
            group.send(MUGStr.rptn)
    elif (msg.text[0:8] == '.choose ') | (msg.text[0:8] == '。choose '):
        if ' ' in msg.text[8:]:
            x = msg.text[8:].split(' ')
        else:
            x = msg.text[8:].split('/')
        if len(x) >= 2:
            group.send(MUGStr.choice.format(x[randint(0,len(x)-1)]))
    elif (msg.text[0:3] == '.nn') | (msg.text[0:3] == '。nn'):#更改昵称
        if ' ' in msg.text:
            if len(msg.text[4:]) > 30:
                group.send(s+'爬')
            else:
                nm[si] = msg.text[4:]
                group.send(MUGStr.NN.format(nm[si]))
        else:
            nm[si] = msg.member.name
            group.send(MUGStr.NNForget.format(tn))
    elif (msg.text[0:6] == '.grade') | (msg.text[0:6] == '。grade'):
        gru = pu[si]
        group.send(MUGStr.InputGradeData)
    elif (pu[si] == gru):
        try:
            if ' ' in msg.text:
                ac,usr,P,gr,gd,ms,acc = msg.text.split(' ')
            else:
                ac,usr,P,gr,gd,ms,acc = msg.text.split('\n')
            pic = Image.open('resources/'+ac+'.jpg')
            ac = ('Stamina '+ac[1:]) if ac[0] == 'S' else ac
            ac = ('Raber '+ac[1:]) if ac[0] == 'R' else ac
            usr = ac +' [Cleared by '+usr+']'
            dr = ImageDraw.Draw(pic)
            fnt1 = ImageFont.truetype('resources/fonts/Cytus2.ttf',70)
            fnt2 = ImageFont.truetype('resources/fonts/mvboli.ttf',60)
            fnt3 = ImageFont.truetype('resources/fonts/ALGER.ttf',65)
            dr.text((30,10),usr,fill='yellow',font=fnt1)
            dr.text((1000,145),P,fill='white',font=fnt2)
            dr.text((1000,220),gr,fill='white',font=fnt2)
            dr.text((1000,295),gd,fill='white',font=fnt2)
            dr.text((1000,370),ms,fill='white',font=fnt2)
            dr.text((1000,455),acc,fill='white',font=fnt3)
            pic.save('resources/timg.jpg')
            group.send_image('resources/timg.jpg')
        except FileNotFoundError:
            group.send(MUGStr.File404)
        except:
            group.send(MUGStr.Err)
        gru = ''
    elif (msg.text[0:3] == '.rb') | (msg.text[0:3] == '。rb') | (msg.text[0:3] == '.rp') | (msg.text[0:3] == '。rp'):#奖励骰/惩罚骰
        x1 = randint(1,100)
        x2 = []
        y  = ''
        t  = 1
        if len(msg.text) > 3:
            if ' ' in msg.text:
                t = msg.text[3:].split(' ')[0]
                t = 1 if t == '' else int(t)
                if t > 100:
                    group.send(s+'爬')
                    t = -1
                y = msg.text[3:].split(' ')[1]
            else:
                t = int(msg.text[3:])
        for i in range(0,t):
            x2.append(randint(0,10))
        x3 = deepcopy(x2)
        x3.append(x1 // 10)
        if msg.text[2] == 'b':
            if x1 % 10 == 0:
                while min(x3) == 0:
                    for i in range(0,len(x3)):
                        x3[i] = 10 if x3[i] == 0 else x3[i]
            x = min(x3) * 10 + x1 % 10
            k = '奖励'
        elif msg.text[2] == 'p':
            if x1 % 10 != 0:
                while max(x3) == 10:
                    for i in range(0,len(x3)):
                        x3[i] = -1 if x3[i] == 10 else x3[i]
            elif min(x3) == 0:
                x3.append(10)
            x = max(x3) * 10 + x1 % 10
            k = '惩罚'
        if y == '':
            group.send(MUGStr.RBP.format(tn,msg.text[2].upper(),x1,k,x2,x))
        else:
            group.send(MUGStr.RBPn.format(y,tn,msg.text[2].upper(),x1,k,x2,x))
    elif (msg.text[0:3] == '.rc') | (msg.text[0:3] == '。rc') | (msg.text[0:3] == '.ra') | (msg.text[0:3] == '。ra'):#检定
        d = randint(1,100)
        k = msg.text[3:] if msg.text[3] != ' ' else msg.text[4:]
        if ' ' in k:
            x,y = k.split(' ')
        else:
            x = k
            y = ''
        try:
            x = int(x)
            if d > max(95,x):
                t = MUGStr.LFail
            elif d > x:
                t = MUGStr.Fail
            elif d > x // 2:
                t = MUGStr.Suc
            elif d > x // 5:
                t = MUGStr.HardSuc
            else:
                t = MUGStr.ExtremeSuc
            group.send(MUGStr.RC.format(tn,y,d,t))    
        except:
            group.send(MUGStr.Err)
    elif (msg.text[0:3] == '.rd') | (msg.text[0:3] == '。rd'):#将rd转化为。r1d
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
embed()
