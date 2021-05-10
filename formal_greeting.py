def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

#mustard = make_formal_greeting("Mustard," "Colonel")
#print(mustard)

def ask_for_user_info():
    user_name = input("What is your name?")
    user_title = input("What is your title?")

    print(make_formal_greeting(user_name, user_title))

ask_for_user_info()