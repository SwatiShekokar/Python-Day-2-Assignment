# 'h' or 'e' or 'o' or 'c' or 'd'
lottery="Hello Coders"
print("choose correct character to win the lottery!")
inputs = input(" ")

if inputs == lottery[0].lower() or inputs == lottery[1].lower() or inputs == lottery[4].lower() or inputs == lottery[6].lower() or inputs == lottery[8].lower():
    print("congratulation,you win the lottery")
else:
    print("sorry, You didn't win the lottery")