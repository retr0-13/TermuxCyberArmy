# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

try:
	import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
        
def entertools():
	os.system('cd Avoid ; bash babi_buat_yang_ngerecode_thanks.sh')

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def wa():
    os.system('xdg-open https://www.instagram.com/termux_hacking/?hl=it')

def menutools():
	os.system ('clear')
	print ' ┏━╮╭━┓            \033[1;37m[\033[1;33m+\033[1;37m] TOOLS HACK ALL IN ONE\n \033[1;31m┃┏┗┛┓┃        \033[1;35m* \033[1;37mAuthor \033[1;31m: \033[1;36mERR0R\n \033[1;31m╰┓▋▋┏╯          \033[1;37mInstagram  \033[1;31m: \033[1;32m@termux_hacking\n\033[1;31m╭━┻╮╲┗━━━━╮╭╮    \033[1;37mDeveloper\033[1;31m: \033[1;32m*ERR0R*\n\033[1;31m┃▎▎┃╲╲╲╲╲╲┣━╯  \033[1;35m* \033[1;33mTool Contains 20 Hacking Tools.\n\033[1;31m╰━┳┻▅╯╲╲╲╲┃      \033[1;33mStay away from existing prohibitions  \033[1;37m^_^\n \033[1;31m ╰━┳┓┏┳┓┏╯    \033[1;35m+ \033[1;33mAppreciate The Author\n    \033[1;31m┗┻┛┗┻┛    \033[1;33m   Not so Difficult to Create \033[1;37m:-D'
	loding2()
	print '\033[1;35m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;35m║ \033[1;37m NO\033[1;37m  \033[1;35m║║ \033[1;37m{\033[1;32mLIST TOOLS HACK COMPLETE \033[1;37m} \033[1;35m║║\033[0mSTATUS\033[1;35m║\n\033[1;35m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m01\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mDARK FACEBOOK\033[1;37m}       \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m02\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mMULTI BRUTEFORCE FACEBOOK\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m03\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mHACK INSTAGRAM  \033[1;37m(\033[1;36mNO ROOT\033[1;37m)} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m04\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mHACK MAIL MULTIBRUTEFORCE\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m05\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mVIRTEX WHATSAPP\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m06\033[1;37m} \033[1;31m║║    \033[1;37m{\033[1;32mLIST VULN WEBSITES\033[1;37m}    \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m07\033[1;37m} \033[1;31m║║         \033[1;37m{\033[1;32mSPAM  SMS\033[1;37m}         \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m08\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mCHAT  ADMIN\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m09\033[1;37m} \033[1;31m║║     \033[1;37m{\033[1;32mJOIN ITALIA CYBER ARMY\033[1;37m}     \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m10\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mHACK WIFI \033[1;37m(\033[1;36mROOT\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m11\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mHACK INSTAGRAM \033[1;37m(\033[1;36mROOT\033[1;37m)\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m12\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mHACK  PULSE\033[1;37m}        \033[1;31m║║\033[1;37m{\033[1;31mCOID\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m13\033[1;37m} \033[1;31m║║  \033[1;37m{\033[1;32mHACK DIAMOND  FREE FIRE\033[1;37m}  \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m14\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mHACK  UC PUBG\033[1;37m}       \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m15\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mHACK  CP CODM\033[1;37m}       \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m16\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mBUG HUNTERS\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m17\033[1;37m} \033[1;31m║║           \033[1;37m{\033[1;32mK-DORK\033[1;37m}          \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m18\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mSEND  VIRUS\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m19\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mSHORTNER  LINKS\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m20\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mNUYUL APLIKASI CAPING\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m21\033[1;37m} \033[1;31m║║  \033[1;37m{\033[1;32mNUYUL APLIKASI  FLASHGO\033[1;37m}  \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m22\033[1;37m} \033[1;31m║║     \033[1;37m{\033[1;32mHACK DIAMOND MLBB\033[1;37m}     \033[1;31m║║\033[1;37m{\033[1;31mCOID\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m22\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mHACK FACEBOOK  TARGET\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m00\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;34mKELUAR  PROGRAM\033[1;37m}      \033[1;31m║║ \033[1;31mEXIT \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m++\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;34mSUBCRIBE PAJAOQ\033[1;37m}      \033[1;31m║║ \033[1;37mSUBS \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝'


def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Already Have an ID And Password? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN FOR CONTINUE║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'ItaliaCyberArmy' and user == 'ERR0R':
      print '║LOGIN SUCCSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login FAILED, Please contact ADMIN'
      wa()
      ressture()
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        
def lodhirt():
    lodhirt = [
     '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*', '      ', '*ERR0R*\n']
    for o in lodhirt:
        print '\r\x1b[1;97m╔[\x1b[1;32m+\x1b[1;97m] \x1b[1;92mSUBSCRIBE CHANNEL \x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.15)

os.system('clear')
logoname = '\033[1;32m  ____________\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\033[1;33m  ╔╗╔╔═╗╔╦╗╔═╗\n\033[1;32m ╔════════════╗\033[1;33m ║║║╠═╣║║║╠═╣\n\033[1;32m ╚════════════╝\033[1;33m ╝╚╝╩ ╩╩ ╩╩ ╩\n\033[1;31m  ║\033[1;36m██████████\033[1;31m╚╗\033[1;33m ╦╔═╔═╗╔╦╗╦ ╦\n\033[1;31m  ║\033[1;36m██\033[1;31m╔══╗\033[1;36m█\033[1;31m╔═╗\033[1;36m█\033[1;31m║\033[1;33m ╠╩╗╠═╣║║║║ ║\n\033[1;31m  ║\033[1;36m██\033[1;31m║\033[1;33m╬\033[1;31m╔╝\033[1;36m█\033[1;31m╚╗║\033[1;36m█\033[1;31m║\033[1;33m ╩ ╩╩ ╩╩ ╩╚═╝\n\033[1;31m  ║\033[1;36m██\033[1;31m╚═╝\033[1;36m█\033[1;31m║\033[1;36m█\033[1;31m╚╝\033[1;36m█\033[1;31m║\033[0m Subscribe\n\033[1;31m  ╚╗\033[1;36m█████████\033[1;31m═╝ \033[0mChannel\n\033[1;31m   ╚╗║╠╩╩╩╩╩╝   \033[0m\033[1;95m*ERR0R*\n\033[1;31m    ║║╚╗\033[1;33m┈\033[1;34m█▐█████\033[1;31m▒\033[0m.｡oO\n\033[1;31m    ║\033[1;36m██\033[1;31m╠╦╦╦╗\n\033[1;31m    ╚╗\033[1;36m██████ \033[0mAuthor \033[1;31m: \033[48;5;0;38;5;197m*ERR0R*\n\033[1;31m     ╚════╝    \033[0mTeam \033[1;31m: \033[1;92mITALIA \033[1;97mCYBER \033[1;91mARMY\n \033[1;33m<══════════════════════════════════>\n\033[1;31m'
print logoname
enternamek = raw_input("\033[1;31m[*] \033[1;32mSELECT YOUR NAME: \033[1;36m")
os.system('clear')

print 32 * '\x1b[1;97m\xe2\x95\x90'
print '\033[1;33m █░░░█ █▀▀ █░░ ▄▀ ▄▀▄ █▄░▄█ █▀▀\n █░█░█ █▀▀ █░▄ █░ █░█ █░█░█ █▀▀\n ░▀░▀░ ▀▀▀ ▀▀▀ ░▀ ░▀░ ▀░░░▀ ▀▀▀'
print '                 \033[1;31m[*] \033[1;37mHi \033[1;36m' + enternamek
print 32 * '\x1b[1;97m\xe2\x95\x90'
lodhirt()
print '\033[1;37m║'
print '\033[1;37m╠\033[1;37m[\033[1;31m*\033[1;37m] \033[1;32mSELECT IT \033[1;37m[\033[1;31m*\033[1;37m]'
print '║\033[1;37m{\033[1;33m1\033[1;37m} \033[1;34mLogin Tool\033[1;37m'
print '║\033[1;37m{\033[1;33m2\033[1;37m} \033[1;34mContact Author \033[0m(\033[1;32mInstagram\033[1;37m)'
print '║\033[1;37m{\033[1;33m3\033[1;37m} \033[1;34mInstall Requirements\033[1;37m'
print '║\033[1;37m{\033[1;33m4\033[1;37m} \033[1;34mDownload User & Pass\033[1;37m'
print '║\033[1;37m{\033[1;31m0\033[1;37m} \033[1;31mEXIT.'
num = input("\033[1;37m╚═\x1b[1;91m▶\x1b[1;97m ")
if num == 1:
	tik()
	entertools()
elif num == 2:
	tik()
	wa()
	print '\n\033[1;37mThank You For Using This Tools ^_^'
elif num == 3:
	tik()
	os.system ('bash babi_lu.sh')
elif num == 4:
	os.system('xdg-open https://www.instagram.com/termux_hacking/?hl=it')
elif num == 0:
	os.system('clear')
	print '\033[1;37mThank You For Using This Tools ^_^'
	os.system('exit')
	