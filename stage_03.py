
with open('artifact.txt','r') as f:
    text = f.read()

with open("artifact.txt",'w') as f:
    f.write(text+"i have added one line")

print(text)
