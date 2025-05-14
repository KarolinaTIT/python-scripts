print("Привет! Добро пожаловать! 👋")
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Autoreset tähendab, et pärast iga väljundit värv taastatakse.

print(Fore.RED + "See tekst on punane!")
print(Back.GREEN + "See tekst on rohelise taustaga!")
print(Style.BRIGHT + "See tekst on heledam!")
print(Fore.YELLOW + Style.BRIGHT + "Kollane ja ere!")