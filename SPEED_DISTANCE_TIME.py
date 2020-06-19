asko = str(input("What do you want to find: " ))



if asko == "1":
    d =int(input("Distance: "))
    t =int(input("Time: "))
    s = d/t
    print("Speed: " + str(s))
elif asko == "2":
    s = int(input("Speed: "))
    t = int(input("Time: "))
    d = s * t
    print("Distance: " + str(d))    
elif asko == "3":
  d = int(input("Distance: "))
  s = int(input("Speed: "))
  t = d/s
  print("Time: " + str(t))    
