#EV = q*v(Pitch)+(1+q)v(Bat)
#Typical Numbers q = 0.2/1+q=1.2

q = 0.2

q1 = 1.2

pitch = input("What is The Pitch Speed?\n")

bat = input("What is the Bat Speed?\n")

EV = q*pitch+(q1)*bat

print(EV + "MPH")
