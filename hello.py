print("Hello, world!")
print("Here is my message:")
with open('message.txt','r') as f:
    print(f.read().upper())
print("Good-bye!")
