import dns.resolver
import colorama
from colorama import Fore, Style
import requests

colorama.init()

apple = [
    'www', 'mail', 'ftp', 'webmail', 'localhost', 'blog', 'cpanel', 'shop', 'dev', 'staging', 'test', 'api', 'app', 
    'beta', 'admin', 'assets', 'cdn', 'cloud', 'dashboard', 'data', 'docs', 'files', 'forum', 'help', 'images', 
    'intranet', 'jira', 'live', 'media', 'mobile', 'news', 'node', 'office', 'old', 'panel', 'portal', 'prod', 'proxy', 
    'secure', 'server', 'static', 'status', 'support', 'svn', 'vpn', 'web', 'webmail', 'wiki', 'beta', 'ci', 'git', 
    'download', 'payments', 'tracker', 'log', 'reports', 'account', 'ads', 'alerts', 'analytics', 'app', 'auth', 
    'billing', 'books', 'calendar', 'chat', 'client', 'connect', 'contact', 'directory', 'email', 'events', 'forum', 
    'gateway', 'hr', 'inventory', 'jobs', 'knowledge', 'legacy', 'login', 'marketing', 'members', 'news', 'partners', 
    'pay', 'projects', 'qa', 'search', 'signin', 'signup', 'storage', 'survey', 'testing', 'tools', 'user', 'users', 
    'vault'
]

def print_ascii_art():
    print(Fore.RED + """
 /$$$$$$$$ /$$$$$$  /$$   /$$ /$$   /$$ /$$      /$$ /$$$$$$$$ /$$$$$$  /$$   /$$
| $$_____//$$__  $$| $$$ | $$| $$  | $$| $$$    /$$$|__  $$__//$$__  $$| $$  / $$
| $$     | $$  \ $$| $$$$| $$| $$  | $$| $$$$  /$$$$   | $$  | $$  \ $$|  $$/ $$/
| $$$$$  | $$$$$$$$| $$ $$ $$| $$  | $$| $$ $$/$$ $$   | $$  | $$$$$$$$ \  $$$$/ 
| $$__/  | $$__  $$| $$  $$$$| $$  | $$| $$  $$$| $$   | $$  | $$__  $$  >$$  $$ 
| $$     | $$  | $$| $$\  $$$| $$  | $$| $$\  $ | $$   | $$  | $$  | $$ /$$/\  $$
| $$     | $$  | $$| $$ \  $$|  $$$$$$/| $$ \/  | $$   | $$  | $$  | $$| $$  \ $$
|__/     |__/  |__/|__/  \__/ \______/ |__/     |__/   |__/  |__/  |__/|__/  |__/                                                                      
""" + Style.RESET_ALL)

def cheese(domain):
    yaaa = []
    sauce = dns.resolver.Resolver()
    
    print(Fore.YELLOW + f"Starting DNS-based seggsing for {domain}..." + Style.RESET_ALL)
    
    for seggsing in apple:
        pickle = f"{seggsing}.{domain}"
        try:
            fizzy = sauce.resolve(pickle, 'A')
            if fizzy:
                yaaa.append(pickle)
                print(Fore.GREEN + f"Found: {pickle}" + Style.RESET_ALL)
        except dns.resolver.NXDOMAIN:
            continue
        except dns.exception.DNSException as e:
            print(Fore.RED + f"Yeah this errored: {pickle}" + Style.RESET_ALL)
    
    if not yaaa:
        print(Fore.RED + "No seggsing found." + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"Enumeration Complete. {len(yaaa)} seggsing found." + Style.RESET_ALL)

def sauce(url):
    print(Fore.YELLOW + f"Starting seggsing scan for {url}..." + Style.RESET_ALL)
    pickle = ['<script>alert(1)</script>', '"><img src=x onerror=alert(1)>', '"><svg onload=alert(1)>']
    for yaaa in pickle:
        cheese = False
        try:
            fizzy = requests.get(f"{url}?q={yaaa}")
            if yaaa in fizzy.text:
                cheese = True
                print(Fore.RED + f"[+] seggsing sauce found: {yaaa}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Yeah this errored: {e}" + Style.RESET_ALL)
        if not cheese:
            print(Fore.GREEN + "No seggsing found." + Style.RESET_ALL)

def pickle(url):
    print(Fore.YELLOW + f"Starting cheese seggsing for {url}..." + Style.RESET_ALL)
    seggsing = ["'", '"', "1' OR '1'='1", "1 OR 1=1", "1'--", "1/*"]
    for yaaa in seggsing:
        cheese = False
        try:
            fizzy = requests.get(f"{url}?id={yaaa}")
            if "sql" in fizzy.text.lower() or "error" in fizzy.text.lower():
                cheese = True
                print(Fore.RED + f"[+] cheese sauce found with: {yaaa}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Yeah this errored: {e}" + Style.RESET_ALL)
        if not cheese:
            print(Fore.GREEN + "No seggsing found." + Style.RESET_ALL)

def seggsing(url):
    print(Fore.YELLOW + f"Starting seggsing for {url}..." + Style.RESET_ALL)
    yaaa = ['admin', 'login', 'dashboard', 'config', 'uploads', 'images', 'css', 'js', 'backup', 'private']
    for cheese in yaaa:
        try:
            fizzy = requests.get(f"{url}/{cheese}")
            if fizzy.status_code == 200:
                print(Fore.GREEN + f"Found seggsing: {url}/{cheese}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"No seggsing found: {url}/{cheese}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Yeah this errored: {e}" + Style.RESET_ALL)

def main_menu():
    print_ascii_art()
    while True:
        print(Fore.MAGENTA + "--- MENU ---" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] Subdomain Enumeration" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] XSS Vulnerability Scan" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] SQL Injection Scan" + Style.RESET_ALL)
        print(Fore.CYAN + "[4] Directory Brute Force" + Style.RESET_ALL)
        print(Fore.CYAN + "[5] Exit" + Style.RESET_ALL)

        potion = input(Fore.YELLOW + "Enter your potion: " + Style.RESET_ALL)
        
        if potion == "1":
            fizzy = input(Fore.YELLOW + "Enter the sauce domain: " + Style.RESET_ALL)
            cheese(fizzy)
        elif potion == "2":
            sauce = input(Fore.YELLOW + "Enter the sauce URL: " + Style.RESET_ALL)
            sauce(sauce)
        elif potion == "3":
            sauce = input(Fore.YELLOW + "Enter the URL: " + Style.RESET_ALL)
            pickle(sauce)
        elif potion == "4":
            sauce = input(Fore.YELLOW + "Enter the seggsing URL: " + Style.RESET_ALL)
            seggsing(sauce)
        elif potion == "5":
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
