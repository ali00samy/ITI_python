import voewls_count as vc
import sorted_list
import email_domains
import auth as auth
import mario_pyramid
from email_validation import validate
from multiplication import multi


emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@it.eg",
    "zzz@gmail.com",
]


def run_vowel_count():
    word = input("Enter a word: ")
    vc.voewls_count(word)


def run_sorted_list():
    sorted_list.sort()


def run_email_domains():
    email_domains.get_domains(emails)


def run_email_validation():
    for i in range(5):
        email = input("Enter your email: ")
        if validate(email):
            print("Welcome")
            break
        else:
            print("Try again, invalid email.")
    else:
        raise Exception("Try again later.")


def run_auth():
    name = input("enter ur name : ")
    auth.Check(name)


def run_multi():
    num = int(input("enter number "))
    multi(num)


def run_mario():
    mario_pyramid.mario_pyramid2()


tasks = [
    ("Count vowels in a word", run_vowel_count),
    ("Sort list of numbers", run_sorted_list),
    ("Extract email domains", run_email_domains),
    ("Validate user email", run_email_validation),
    ("Validate name and password", run_auth),
    ("Get multiplication", run_multi),
    ("Print Mario pyramid", run_mario),
]


if __name__ == "__main__":
    print("Available tasks:")
    for i, (name, _) in enumerate(tasks, start=1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Enter the number of the task you want to run: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1][1]()  # run selected function
        else:
            print("Invalid choice. Number out of range.")
    except ValueError:
        print("Please enter a valid number.")
