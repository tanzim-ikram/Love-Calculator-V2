# LOVE CALCULATOR - V2

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is your partner's name? ")


name1 = name1.lower()
name2 = name2.lower()
name3 = name1 + name2
# print(name3)

T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")
# print(T, R, U, E)

true_sum = T + R + U + E 
# print(true_sum)

L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")
# print(L, O, V, E)

love_sum = L + O + V + E
# print(love_sum)

join = int(str(true_sum)+ str(love_sum))

if join > 90:
    
    print(f"Your score is {join}, you guys are made for each other!")

elif join >= 50 and  join <= 90:

    print(f"Your score is {join}, you are alright together.")
else:
    print(f"Your score is {join}. Stay away from each other!")


