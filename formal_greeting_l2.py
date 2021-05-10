#version 1
def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))
#version 2
def ask_for_user_info():
    user_name = input("What is your name?")
    user_title = input("What is your title?")
    return[user_name, user_title]
#the return is a list because of the []
#version 3
def ask_for_user_info_dictionary():
    user_name = input("What is your name?")
    user_title = input("What is your title?")
    return {
        "name": user_name
        "title": user_title
    }

#print(ask_for_user_info())
user_info = ask_for_user_info_dictionary()
greeting = make_formal_greeting(user_info["name"], user_info["title"])
print(greeting)
#there are many ways to do things. 