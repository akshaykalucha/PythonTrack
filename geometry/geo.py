import rect
import circle

# animate geometric designs for kids
print("Animate any geometric figure")
print("What geometric figure do you want to animate? :\n1)Rectangle\n2)Circle\n3)triangle")
inp = int(input())

if inp == 1:
    print("Animating rectangle")
elif inp == 2:
    print("Animating circle")
else:
    print("Default: animating triangle")