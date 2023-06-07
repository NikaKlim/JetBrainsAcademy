print("How many pencils would you like to use:")
pencil = int(input())
print("Who will be the first (John, Jack):")
name = input()
print("|"*pencil)
#names = ("John","Jack")

while pencil !=0:
    
    print(name+"'s turn:")
    turn = int(input())
    pencil-= turn
    print("|"*pencil)
    if name=="John":
        name = "Jack"
    else:
        name = "John"
