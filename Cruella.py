import urllib2
import re
import platform
import os
import webbrowser
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
global Quti
global No
global B
global GoogleApiKey
GoogleApiKey = " " # You need to imput your own Google API Key to use the Address Print out (not the map link)
Geo = "1"
Latitude = ""
Domains = "2"
Address = "3"
External_IP = "4"
Terminal = "5"
Metasploit = "6"
Quit = "7"
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
        IP = raw_input("IP/WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read()
        print body
        C = body.find("Latitude")
        C += 10
        D = C + 10
        Latitude = body[C:D]
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP).read()
        C = body.find("Longitude")
        C += 10
        D = C + 10
        Longitude = body[C:D]
        print("")
        print("")

    def domains():

        print("Enter website with out www. to get full out put")
        print("Warnning may have massive output")

        site = raw_input("WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/dnslookup/?q="+ site)

        write = raw_input("Do you want the ouput sent to a file?(Y/N): ")
        if(write==Yes or write == yes):
            f = open("OwnedHosts.txt", "w+")
            f.write(body)
            f.close()
        else:
            print body
            print(" ")
            print(" ")


    def address():
        global Latitude
        if(Latitude==""):
            print("")
            print("")
            print("Please run Tool 1 first")
            print("")
            print("")
            main()
        else:
            pass
        #print(Latitude)
        #print(Longitude)
        #print("Enter the Latitude and Longitude to recive the address(s)")
        #Latitude = raw_input("Latitude: " )
        #Longitude = raw_input("Longitude: " )

        link = raw_input("Would you like to open Google Maps?(Y/N): ")
        if(link==Yes or link == yes):
            url = ("https://www.google.com/maps/search/?api=1&query=" + Latitude +","+ Longitude)
            webbrowser.open_new_tab(url)
            print(" ")
            print(url)
        else:
            B = Latitude+","+Longitude +"&key="+ GoogleApiKey
            body = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+B)
            print body.read()
            B = ""
    def external_ip():
        print("")
        print("External IP:")
        print("------------")
        if(OS == Windows):
            os.system("nslookup myip.opendns.com. resolver1.opendns.com") # External IP check for Windows
        else:
            os.system("dig +short myip.opendns.com @resolver1.opendns.com") # External IP check of every OS except for Windows
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
        B = raw_input("Would you like to update metasploit befor running (Y/N)")
        if(B == Yes or B == yes):
            print("Switching to root to update")
            os.system("sudo msfupdate")
            os.system("msfconsole")
        else:
            print("Launching Metasploit")
            os.system("msfconsole")
    def quit():
        B = raw_input("Do you want to quit Cruella? (Y/N)")
        if(B == Yes or B == yes):
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

        print("[1] IP Geolocator ")
        print("[2] Owned Domains and IPs")
        print("[3] Resolve Cordinets to Address(use with option [1])")
        print("[4] Display External IP")
        print("[5] Terminal")
        print("[6] Metasploit")
        print("[7] Quit Cruella")
        tool = raw_input("Select a tool: " )

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
