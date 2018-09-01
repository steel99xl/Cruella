#by steel99xl
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
Quit = "9"
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
        body = urllib2.urlopen("http://api.hackertarget.com/dnslookup/?q="+ site)

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
        os.system("sudo openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'| xargs sudo ifconfig " + C + " ether")
        os.system("sudo ifconfig " + C + " down")
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
    def quit():
        B = input("Do you want to quit Cruella? (Y/N)")
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
        print("[9] Quit Cruella")
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
