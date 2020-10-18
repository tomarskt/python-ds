import random

wins = 0
losses = 0
ties = 0
random_min=2
random_max=21
retries = 1000
deal_number=17

for x in range (0,retries):
    yourhand = random.randint(random_min,random_max)
    print("Your hand is currently {}.".format(yourhand))


    while(yourhand < deal_number) :
        yourhand = random.randint(random_min,random_max) + yourhand 
        print("Your hand is currently {}".format(yourhand))


    theirhand = random.randint(random_min,random_max)
    print("Their hand is currently {}.".format(theirhand))

    while(theirhand < deal_number) :
        theirhand = random.randint(random_min,random_max) + theirhand 
        print("Their hand is currently {}".format(theirhand))

    if yourhand == theirhand:
        ties = ties + 1
        print("It is a tie !!! (-:-)")
    elif theirhand > yourhand:
        if(theirhand > random_max):
            wins = wins + 1
            print("You win !!! :-) ")
        else:
            losses = losses + 1 
            print("They win !!! :-( ")
    elif yourhand > theirhand:
        if(yourhand > random_max):
            losses = losses + 1 
            print("They win !!! :-( ")
        else:
            wins = wins + 1
            print("You win !!! :-) ")

print("{} ties".format(ties))
print("{} wins".format(wins))
print("{} losses".format(losses))
print("{} total : {} ties {} wins {} losses".format(ties+wins+losses,ties,wins,losses))
    # if yourhand >= 17:
#   if yourhand > 21 or yourhand >= 17:
#     break
#   elif yourhand == 21:
#     break
#   elif yourhand >= 17:
#     pass
#   if theirhand < 17:
#     t = random.randint(2,21) + theirhand 
#     print("Their hand is currently {}".format(t))
#     if t > 21:
#       print("Their final hand is {}.".format(theirhand))
#     # if y > 21:
#     #   print("Your final hand is {}.".format(yourhand))
#     else:
#       print("Their final hand is {} and yours is {}.".format(t, y))
#   elif theirhand == 21:
#     break
#   elif theirhand >= 17:
#     pass
#   if t < y:
#     print("You win!")
#   elif y > t:
#     print("They win. :C")
#   if t > 21 and y < 21:
#     print("You win!")
#   elif t < 21 and y > 21:
#     print("They win. :C")
#   if t == y:
#     print("It's a tie!")
# Your hand is currently a 20
# Their hand is currently a 10
# Thier hand is currently a 15
# Their hand is currently a 22
# Your final hand is a 20 and theirs is 22
# We Win !!!
# Your hand is currently a 21
# Their hand is currently a 8
# Thier hand is currently a 10
# Thier hand is currently a 14
# Thier hand is currently a 18
# Your final hand is a 21 and theirs is 18
# We Win !!!
# Your hand is currently a 7
# Your hand is currently a 16
# Their hand is currently a 9
# Their hand is currently a 18
# Your final hand is a 16 and theirs is 18
# They win ...
# 0 ties
# 2 wins
# 3 losses