f=open("intro.txt",'r')
for x in f:
      print(x)
f.close()
def program1():
    f = open("intro.txt","a")
    text=input("Enter the text:")
    f.write(text)
    
    f.close()
program1()
