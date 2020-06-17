from time import *
at = int(input("A: "))
bt = int(input("B: "))
ct = int(input("C: "))

group = at * ct
bsq = bt ** 2
underr = bsq - 4 * group
undersq = underr ** 0.5
deno = 2 * at
nume = -bt - undersq
numeo = -bt + undersq

x = "X: "

mixture = nume/deno
mixtureOne = numeo/deno
print(str(x) + str(mixture) + " or " + str(x) + str(mixtureOne))

sleep(20)


