import urllib2
import webbrowser
global Yes
global Geo
global Domains
global Address
global No
global B
global GoogleApiKey
GoogleApiKey = "" # You need to imput your own Google API Key to use the Address Print out (not the map link)
Geo = "1"
Domains = "2"
Address = "3"
Yes = "Y"
No = "N"
B = "" #This is just used as a blank variable to temporary store variables
print("Cruella") # ascii art comming soon
print(" WARRNING THE ANSWERS OF (Y/N) ARE CASE SENSITIVE FOR (Y)")

while True:
    def geo():
        print("Enter a website or IP")
        IP = raw_input("IP/WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/geoip/?q="+ IP)
        print body.read()
        print(" ")
        print(" ")

    def domains():

        print("Enter website with out www. to get full out put")
        print("Warnning may have massive output")

        site = raw_input("WEBSITE: " )
        body = urllib2.urlopen("http://api.hackertarget.com/hostsearch/?q="+ site)

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

        print("Enter the Latitude and Longitude to recive the address(s)")
        Latitude = raw_input("Latitude: " )
        Longitude = raw_input("Longitude: " )

        link = raw_input("Would you like a Google Maps Link?(Y/N): ")
        if(link==Yes):
            url = ("https://www.google.com/maps/place/0%C2%B000'00.0%22N+0%C2%B000'00.0%22E/@" + Latitude +","+ Longitude +",3647m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d" + Latitude +"!4d"+ Longitude)
            webbrowser.open_new_tab(url)
            print(" ")
        else:
            B = Latitude+","+Longitude +"&key="+ GoogleApiKey
            body = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+B)
            print body.read()

    def main():

        print("[1] IP Geolocator ")
        print("[2] Owned Domains and IPs")
        print("[3] Resolve Cordinets to Address(use with option [1])")

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
            print("Select a tool")
    main()
