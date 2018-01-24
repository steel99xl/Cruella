import urllib2
import platform
import os
import webbrowser
global OS
global Windows
global Latitude
global Longitude
global Yes
global Geo
global Domains
global External_IP
global Terminal
global Address
global No
global B
global GoogleApiKey
GoogleApiKey = "" # You need to imput your own Google API Key to use the Address Print out (not the map link)
Geo = "1"
Latitude = ""
Domains = "2"
Address = "3"
External_IP = "4"
Terminal = "5"
Yes = "Y"
No = "N"
OS = platform.system()
Windows = "Windows" # Its esayer just check windows and if its not have its default to a Unix OS
B = "" #This is just used as a blank variable to temporary store variables

print("")
print(" $$$$$$\                                $$\ $$\           ")
print("$$  __$$\                               $$ |$$ |          ")
print("$$ /  \__| $$$$$$\  $$\   $$\  $$$$$$\  $$ |$$ | $$$$$$\  ")
print("$$ |      $$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$ | \____$$\ ")
print("$$ |      $$ |  \__|$$ |  $$ |$$$$$$$$ |$$ |$$ | $$$$$$$ |")
print("$$ |  $$\ $$ |      $$ |  $$ |$$   ____|$$ |$$ |$$  __$$ |")
print("\$$$$$$  |$$ |      \$$$$$$  |\$$$$$$$\ $$ |$$ |\$$$$$$$ |")
print(" \______/ \__|       \______/  \_______|\__|\__| \_______|") # ascii art comming soon
print(" ")
print(" WARRNING THE ANSWERS OF (Y/N) ARE CASE SENSITIVE FOR (Y)")

while True:
    def geo():
        global Latitude
        global Longitude
        print("Enter a website or IP")
        IP = raw_input("IP/WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP)
        print body.read()
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP)
        Latitude = body.read()[77:86]
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP)
        Longitude = body.read()[98:108]
        print(" ")

    def domains():

        print("Enter website with out www. to get full out put")
        print("Warnning may have massive output")

        site = raw_input("WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/dnslookup/?q="+ site)

        write = raw_input("Do you want the ouput sent to a file?(Y/N): ")
        if(write==Yes):
            f = open("OwnedHosts.txt", "w+")
            f.write(body.read())
            f.close()
        else:
            print body.read()
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
        if(link==Yes):
            url = ("https://www.google.com/maps/place/0%C2%B000'00.0%22N+0%C2%B000'00.0%22E/@" + Latitude +","+ Longitude +",3647m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d" + Latitude +"!4d"+ Longitude)
            webbrowser.open_new_tab(url)
            print(" ")
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

    def main():

        print("[1] IP Geolocator ")
        print("[2] Owned Domains and IPs")
        print("[3] Resolve Cordinets to Address(use with option [1])")
        print("[4] Display External IP")
        print("[5] Terminal")
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
        print("Select a tool")
    main()
