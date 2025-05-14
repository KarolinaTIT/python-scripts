print("Привет! Добро пожаловать! 👋")
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Autoreset tähendab, et pärast iga väljundit värv taastatakse.

print(Fore.RED + "See tekst on punane!")
print(Back.GREEN + "See tekst on rohelise taustaga!")
print(Style.BRIGHT + "See tekst on heledam!")
print(Fore.YELLOW + Style.BRIGHT + "Kollane ja ere!")



from colorama import Fore
import emoji

def mood_message(mood):
    if mood == "happy":
        print(Fore.GREEN + "Ты полон энергии и счастья! " + emoji.emojize(":smile:"))
    elif mood == "sad":
        print(Fore.BLUE + "Не переживай, все будет хорошо! " + emoji.emojize(":disappointed:"))
    elif mood == "tired":
        print(Fore.YELLOW + "Отдохни, ты это заслужил! " + emoji.emojize(":sleeping:"))
    elif mood == "excited":
        print(Fore.CYAN + "Похоже, у тебя большие планы! " + emoji.emojize(":star-struck:"))
    else:
        print(Fore.RED + "Пожалуйста, выбери правильное настроение (happy, sad, tired, excited).")

# Приветствие
print(Fore.MAGENTA + "Добро пожаловать! Надеюсь, у тебя отличный день! 🎉")

# Запрос настроения
user_mood = input("Как ты себя чувствуешь сегодня? (happy, sad, tired, excited): ").strip().lower()

# Выводим соответствующее сообщение
mood_message(user_mood)
