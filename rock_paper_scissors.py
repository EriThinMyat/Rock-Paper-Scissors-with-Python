import random
import time 

class RockPaperScissors:
    def __init__(self):
        self.result = []
        self.options = {
            "r" : "rock",
            "p" : "paper",
            "s" : "scissors"
        }
        self.emoji_options = {
        "r": "✊",  # Rock
        "p": "✋",  # Paper
        "s": "✌️"   # Scissors
        }
        self.ties = 0
        self.losses = 0
        self.wins = 0


    def main_menu(self):
        menu_items = {
            "1" : "Play Game",
            "2" : "View Results",
            "0" : "Exit Program"
        }

        print("-" * 25)
        print("*** Main Menu ***")
        for key, val in menu_items.items():
            print(f"{key}. {val}")
        print("-" * 25)


    def choose_menu(self):
        while True:
            self.main_menu()

            try:
                choose = int(input("Choose... "))
            except ValueError:
                print("Invalid input")
                continue

            if choose == 0:
                print("Have a nice day!")
                break

            elif choose == 1:
                self.play_game_menu()

            elif choose == 2:
                self.show_results()

            else:
                print("Invalid number.")


    def show_results(self):
        if not self.result:
            print("No result yet.")
            return
       
        print("Your Results")
        for ind, result in enumerate(self.result, 1):
            print(f"{ind}. {result}")
        print(f"Total Wins: {self.wins}")
        print(f"Total Losses: {self.losses}")
        print(f"Total Draws: {self.ties}")
    

    def game_menu(self):
        menu_items = {
            "1" : "Play Game",
            "0" : "Return Back"
        }

        print("-" * 25)
        for key, val in menu_items.items():
            print(f"{key}. {val}")
        print("-" * 25)


    def play_game_menu(self):
        while True:
            self.game_menu()

            try:
                choose = int(input("Choose... "))
            except ValueError:
                print("Invalid input.")
                continue

            if choose == 0:
                print("Return Back to Main Menu...")
                break

            elif choose == 1:
                self.play_game()

            else:
                print("Invalid number.")


    def counter(self, second = 3):
        print("Go Ready...")
        for i in range(second, 0, -1):
            print(f"{i}")
            time.sleep(1)
        print("Start...")


    def play_game(self):
        self.counter()
        user_input = input("Your turn: ").strip().lower()

        if user_input in self.options:
            user_choice_key = user_input

        elif user_input in self.options.values():
            user_choice_key = [k for k, v in self.options.items() if v == user_input][0]

        else:
            print("No matched choice found.")
            return

        computer_choice_key = random.choice(list(self.options))

        user_choice = self.options[user_choice_key]
        user_choice_emoji = self.emoji_options[user_choice_key]
        computer_choice = self.options[computer_choice_key]
        computer_choice_emoji = self.emoji_options[computer_choice_key]

        print("-" * 25)
        print(f"Your choice: {user_choice_emoji} {user_choice.capitalize()}")
        print(f"Computer choice: {computer_choice_emoji} {computer_choice.capitalize()}")

        if user_choice_key == computer_choice_key:
            result = "🤝 Draw!"
            self.ties += 1

        elif ((user_choice_key == "r" and computer_choice_key == "p") or
              (user_choice_key == "p" and computer_choice_key == "s") or
              (user_choice_key == "s" and computer_choice_key == "r")):
            result = "💀 You Lose!"
            self.losses += 1

        else:
            result = "🏆 You Win!"
            self.wins += 1

        self.result.append(f"{user_choice_emoji} {user_choice.capitalize()} Vs {computer_choice_emoji} {computer_choice.capitalize()} -> {result}")
        print(result)



if __name__ == "__main__":
    play = RockPaperScissors()
    play.choose_menu()