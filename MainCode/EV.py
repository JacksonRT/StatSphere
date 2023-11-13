#EV = q*v(Pitch)+(1+q)v(Bat)
#Typical Numbers q = 0.2/1+q=1.2

Mf = .2

Ps = int(input("What is The Pitch Speed?\n"))

Bs = int(input("What is the Bat Speed?\n"))

Ve = Mf * (Ps) + (1 + Mf) * Bs

print (Ve, "MPH")
