message=input(">")
words=message.split(" ")

mapping={
    ":)":"😊",":(":"😢"
}
output=""
for i in words:
    
    output+=mapping.get(i,i)+""
print(output)