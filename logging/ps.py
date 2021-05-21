import subprocess
from contextlib import redirect_stdout
import re

p = subprocess.check_output("PowerShell.exe -Executionpolicy byPass -File C:\\Users\\srijitha.s\\Downloads\\logging\\sample.ps1")
#print(p.decode())

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        print(p.decode())
#print("******************************************************************************")

regex = r'ProcessID\s+:\s+(\d+)\n+Name\s+:\s+(\w.+)\n+WS\s+:\s+(\d+)\n+CommandLine\s+:\s(.+)?'
#regex = r'ProcessID\s+:\s+(\d+)\n+Name\s+:\s+(\w.+)\n+WS\s+:\s+(\d+)\n+CommandLine\s+:\s(.?|.+/.exe)?'
#regex1 = r'(Name\s*:\s*(\w+))'
#ProcessID   : 18672
#Name        : pycharm64.exe
#WS          : 609677312
#CommandLine : "C:\Users\srijitha.s\AppData\Local\JetBrains\PyCharm Community Edition 2020.2.1\bin\pycharm64.exe"
dic={}
with open ('out.txt', 'r') as infile:
    content = infile.read()
    print(content)
    results = re.findall(regex,content)
    #print(results)

#print(results[0][0])
s=0
for i in results:
    #print(i)
    if i[3]!='':
        match='.+'+i[1]
        #print("=================================",i)

        #print(re.search(match,i[3],re.IGNORECASE).group(0))
        s=re.search(match,i[3],re.IGNORECASE).group(0)
    dic[i[0]]=list(i[1:3])
    #dic[i[0]][]
    #print(dic[i[0]][0][0])
    #print(type(dic[i[0]]))
    dic[i[0]].append(s)

#print("***************************************************************" )
#print(dic)




