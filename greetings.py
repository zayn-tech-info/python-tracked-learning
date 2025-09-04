def greet_people(name, lang): 
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__" : 
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides a Personal greetings."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()
    greet_people(args.name, args.lang)
    print(args.name, args.lang)