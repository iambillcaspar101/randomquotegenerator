import random
import json
import os

# File to store quotes
FILE_NAME = "quotes.json"

# Load quotes from file or use defaults
def load_quotes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    else:
        # Default quotes if file doesn't exist
        return [
            "Believe you can and you're halfway there.",
            "The secret to getting ahead is getting started.",
            "Your only limit is your mind.",
            "Action is the foundational key to all success.",
            "Don't watch the clock; do what it does. Keep going.",
            "A year from now, you will wish you had started today.",
            "Fall seven times, stand up eight.",
            "Success is a journey, not a destination.",
            "Small daily improvements are the key to stunning long-term results.",
            "The comeback is always stronger than the setback.",
            "You are capable of more than you know.",
            "Don't compare your chapter 1 to someone else's chapter 20.",
            "Failure is not the opposite of success; it's a part of success.",
            "What you focus on expands.",
            "Be stronger than your excuses.",
            "The future depends on what you do today.",
            "Your attitude determines your direction.",
            "Don't wait for opportunity. Create it.",
            "Your mistakes are proof that you are trying.",
            "The pain you feel today will be the strength you feel tomorrow.",
            "Embrace the challenge, for it is the path to growth.",
            "Consistency is more important than perfection.",
            "Push yourself, because no one else is going to do it for you.",
            "The only person you are destined to become is the person you decide to be.",
            "Your mind is a garden. Your thoughts are the seeds. You can grow flowers or you can grow weeds.",
            "Wake up with determination. Go to bed with satisfaction.",
            "A smooth sea never made a skilled sailor.",
            "Stop doubting yourself. Work hard and make it happen.",
            "The key to success is to focus on goals, not obstacles.",
            "Let your faith be bigger than your fear."
        ]

# Save quotes to file
def save_quotes(quotes):
    with open(FILE_NAME, "w") as file:
        json.dump(quotes, file, indent=4)

# Functions
def get_random_quote():
    return random.choice(quotes)

def add_quote(new_quote):
    quotes.append(new_quote)
    save_quotes(quotes)

def remove_quote(quote):
    if quote in quotes:
        quotes.remove(quote)
        save_quotes(quotes)
        return True
    return False

# Main program
if __name__ == "__main__":
    quotes = load_quotes()
    print("Welcome to the Inspirational Quote Generator!")

    while True:
        print("\nOptions:")
        print("1. Get a random quote")
        print("2. Add a new quote")
        print("3. Remove a quote")
        print("4. Show all quotes")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nHere's your quote:")
            print(get_random_quote())

        elif choice == "2":
            new_quote = input("Enter the new quote: ")
            add_quote(new_quote)
            print("Quote added successfully!")

        elif choice == "3":
            quote_to_remove = input("Enter the exact quote you want to remove: ")
            if remove_quote(quote_to_remove):
                print("Quote removed successfully!")
            else:
                print("Quote not found!")

        elif choice == "4":
            print("\nAll Quotes:")
            for idx, quote in enumerate(quotes, 1):
                print(f"{idx}. {quote}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
