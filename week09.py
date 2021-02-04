
num = int(input("Enter a number to count to: "))


for i in range(1,num):
  print(i)
print (num)

print("Now we will count down:")

while( num > 0):
  print(num)
  num = num - 1



while score > 5:
   score = int(input("Enter score between 0 and 100: "))
   score = score -1

grade = (score) /5

def score(grade):

 if grade >= 93 and grade <= 100:
    return "A"
 elif grade >= 90 and grade <=93:
    return "A-"
 elif grade >= 87 and grade <=90:
    return "B+"
 elif grade >= 83 and grade <=87:
    return "B"
 elif grade >= 80 and grade <=83:
    return "B-"
 elif grade >= 77 and grade <=80:
    return "C+"
 elif grade >= 73 and grade <=77:
    return "C"
 elif grade >= 70 and grade <=73:
    return "C-"
 elif grade >= 67 and grade <=70:
    return "D+"
 elif grade >= 63 and grade <=67:
    return "D"
 elif grade >= 60 and grade <=63:
    return "D-"
 else :
    return "F"