import random

def prob_1(u):
    m = 0
    while 1 + u != 1 :
        m += 1
        u = 10 ** (-m)
    return m-1,u*10

def verify_neasoc():
    u=prob_1(1)[1];
    x=1.0
    y = u / 10
    z = u /10
    if((x+y)+z == x+(y+z)):
        print ("Adunarea este asociativa")
    print("Adunarea nu este asociativa")

verify_neasoc();

def prob_2():

    while True:
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)
        c = random.uniform(0, 1)
        if(((a*b)*c!=a*(b*c))):
            print(a)
            print(b)
            print(c)
            print(f"Termeul din stanga: {(a*b)*c}")
            print(f"Termeul din dreapta: {a*(b*c)}")

            break
prob_2();

