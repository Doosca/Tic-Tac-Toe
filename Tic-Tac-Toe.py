def getting_started(ready_or_not):
 if ready_or_not.lower() in ["yes", "yeah"]:
    print("Okay! Let's get started.")
    print("I'll hand you the ingredients. Will you mix them in slow or fast?")
 else:
    print('...well get outta here then!')
    exit()
 return ready_or_not
def stirring_time(mix_slow_or_fast):
 if mix_slow_or_fast.lower() in ["slow", "slowly"]:
    print("Wow, you're like a cookie baking pro! We have to preheat the oven now. Make sure it's 350 degrees.")
    print("(type in the correct temperature)")
 else:
    print("There's flour everywhere! This is a mess, you're very bad at making cookies.")
    exit()
 return mix_slow_or_fast

print('***Lets make cookies!*** A text adventure game! Are you ready?')
a = input()
getting_started(a)
b = input()
stirring_time(b)

