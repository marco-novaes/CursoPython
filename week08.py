from pip._vendor.distlib.compat import raw_input

choice = raw_input("Enter C for Circle, T for Triangle, or R for Rectangle: ")

if choice == "C":
    radius = float(raw_input("Enter the radius: "))
    Area = 3.14159 * radius ** 2
    print(Area)

elif choice == "T":
      base = float(raw_input("Enter the base: "))
      high = float(raw_input("Enter the high: "))
      area = (base * high) /2
      print(area)
elif choice == "R":
    b = float(raw_input("Enter the base: "))
    h = float(raw_input("Enter the high: "))
    area1 = b * h
    print (area1)
else:
   print ("Don't have this on this calculator.")
