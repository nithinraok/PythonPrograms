from datetime import datetime as dt
import time
hostFile='C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites=['www.facebook.com','www.cricbuzz.com']
#file.seek(-1);
while True:
    if 18 < dt.now().hour < 23 :
        print "Working Hours"
        with open(hostFile,'r+') as file:            
            content = file.read()
            for website in websites:
                line = redirect + '   ' + website + '\n';
                if website in content:
                    pass
                else:   
                    file.seek(0,1);
                    file.write(line)
        
    else:
        print "Fun Hours" 
        newfile=''
        with open(hostFile,'r') as file:
            content = file.readlines();
            for newcontent in content:
                if not any(website in newcontent for website in websites):
                    newfile=newfile+newcontent
        with open(hostFile,'w') as file:
            file.write(newfile)
    time.sleep(10);
