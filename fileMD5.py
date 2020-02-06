#_*_ coding:utf-8 _*-
# Python 3.7
#
# fileMD5 v1.0
# Author:ThestaRY
# github:


import hashlib
import sys



banner = '''

_________          _______  _______ _________ _______  _______          
\__   __/|\     /|(  ____ \(  ____ \\__   __/(  ___  )(  ____ )|\     /|
   ) (   | )   ( || (    \/| (    \/   ) (   | (   ) || (    )|( \   / )
   | |   | (___) || (__    | (_____    | |   | (___) || (____)| \ (_) / 
   | |   |  ___  ||  __)   (_____  )   | |   |  ___  ||     __)  \   /  
   | |   | (   ) || (            ) |   | |   | (   ) || (\ (      ) (   
   | |   | )   ( || (____/\/\____) |   | |   | )   ( || ) \ \__   | |   
   )_(   |/     \|(_______/\_______)   )_(   |/     \||/   \__/   \_/   


'''

print(banner)

if len(sys.argv) == 2:
    try:
        print(hashlib.md5(open(sys.argv[1],'rb').read()).hexdigest())#以二进制格式打开一个文件用于只读,并获取md5值,返回摘要,十六进制数据字符串值
    except:
        print('[-]请输入正确的文件名。\nPlease input a correct filename')
else:
    print('[*]Usage: python3 fileMD5.py [Filename]')