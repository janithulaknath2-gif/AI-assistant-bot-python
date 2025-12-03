# --------------Movie Recomend system ------------------
movies = {
    "comedy": [
        "Home Alone",
        "Rush Hour",
        "Kung Fu Panda",
        "Despicable Me",
        "The Secret Life of Pets",
        "Diary of a Wimpy Kid",
        "Dumb and Dumber",
        "The Lego Movie",
        "Minions",
        "Zootopia",
        "Rat Race",
        "The Other Guys",
    ],
    "romance": [
        "The Fault in Our Stars",
        "To All the Boys I’ve Loved Before",
        "The Notebook",
        "La La Land",
        "10 Things I Hate About You",
    ],
    "horror": [
        "The Ring",
        "The Conjuring",
        "Annabelle",
        "Lights Out",
        "Insidious",
        "Mama",
    ],
    "action": [
        "Spider-Man: Homecoming",
        "Avengers: Endgame",
        "Doctor Strange",
        "Black Panther",
        "Shazam!",
        "Jumanji: Welcome to the Jungle",
        "Mission: Impossible",
    ],
}

trending_movies = [
    "Frankenstein",
    "Zootopia 2",
    "Wicked: For Good",
    "Wake Up Dead Man: A Knives Out Mystery",
    "KPop Demon Hunters",
    "In Your Dreams",
    "Champagne Problems",
    "The Carman Family Deaths",
]


def movie_recomend(movies, trending_movies):
    print("Welcome to Movie Recomended System ")
    category = input("Enter Your Favourite Movie Category : ")
    c = 1  # set numbers
    if category.lower() in movies.keys():
        print(f"---------Recomended {category} Movies-----------")
        for m in movies[category]:
            print(f"{c}. {m}")
            c = c + 1
        c = 0
    else:
        print("This ctegory Not Found ")
        check = input("Do You want see Trending movie list (y/n)")
        if check.lower() == "y":
            print("___________Trending Movies ___________")
            for t in trending_movies:
                print(c, ".", t)
                c = c + 1
        else:
            print("Thank you for using Movie Recommendation System")


# ---------------------------Simple calculator ----------------------

symbols = ["+", "-", "*", "/", "**", "//"]


def calculator(symbols):
    while True:
        try:
            n1 = int(input("Insert first  Number : "))
            n2 = int(input("Insert Second Number : "))
            break
        except ValueError:
            print("Please Use Numbers ")
        except Exception as e:
            print(f"Error is  {e}")
    print("______________________")
    print("Addtion= + ")
    print("______________________")
    print("Subtraction = -")
    print("______________________")
    print("multipication = *")
    print("______________________")
    print("Division = /")
    print("______________________")
    print("power = **")
    print("______________________")
    print("floor division = // ")
    print("______________________")
    operator = input("Enter the Arithmetic Operator : ")
    while operator not in symbols:
        print("Please Enter Valid Arithmetic Operators ")
        operator = input("Please Insert Valid Arithmetic Operator : ")
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2
    elif operator == "**":
        result = n1**n2
    else:
        result = n1 // n2
    print(f"Anwser is : {result}")


# -------Spam detactor ------------
spam_words = [
    "free",
    "win",
    "winner",
    "money",
    "cash",
    "prize",
    "offer",
    "click",
    "buy",
    "subscribe",
    "urgent",
    "limited",
    "deal",
    "discount",
    "bonus",
    "guarantee",
    "credit",
    "loan",
    "gift",
    "reward",
]


def spamdetector(spam_words):
    spam = input("Insert the Word : ").lower()
    if spam in spam_words:
        print("This masage is  Spam Word ")
    else:
        print("This masage is Safe ")


# -----------------add and view notes---------------
Notes = []


def addnote(Notes=Notes):
    while True:
        text = input("add  the Note : ")
        Notes.append(text)
        c = input("If you want to add  Note : (yes/no)").lower()
        if c == "yes":
            continue
        elif c == "no":
            break


def viewnote(Notes=Notes):
    c = 0
    for x in Notes:
        c = c + 1
        print(f"------- {c}. Note ----------")
        print(x)
        print("------------------------")


name = input("Enter your name  :  ")
print(f"------ Welcome {name} to AI Assistant Bot ------")
Service_details = {}

while True:
    print("---------------------------")
    print("1.Movie Recomended System")
    print("2.Simple calculator")
    print("3.Spam detector ")
    print("4.Add Notes")
    print("5.View notes")
    print("6.Exit")
    print("---------------------------")
    while True:
        try:
            choice = int(input("Chose the Service number : "))
            while choice > 7 or choice < 0:
                print("---------------------------")
                print("1.Movie Recomended System")
                print("2.Simple calculator")
                print("3.Spam detector ")
                print("4.Add Notes")
                print("5.View notes")
                print("6.Exit")
                print("---------------------------")
                choice = int(input("Chose the Service number : "))
            break
        except ValueError:
            print("Please use Numbers For Choices ")
    Service_details[name] = choice
    if choice == 1:
        movie_recomend(movies, trending_movies)
    elif choice == 2:
        calculator(symbols)
    elif choice == 3:
        spamdetector(spam_words)
    elif choice == 4:
        addnote()
    elif choice == 5:
        viewnote()
    else:
        print(f"Thanks {name} for Using AI assitent Bot ")
        break
