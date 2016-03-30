import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "This is a secret number game"
print "number 1 to 99,can try 6 times"
while guess != secret and tries < 6:
    guess = input("input your number:")
    if guess < secret:
        print "it's low"
    elif guess > secret:
            print "it's too high"

    tries = tries + 1

if guess == secret:
    print "Got it"
else:
    print "No More time"
    print "the number is:",secret
