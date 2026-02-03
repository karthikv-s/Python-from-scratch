def emoji_converter(message):
    words=message.split(" ")

    mapping={
        ":)":"😊",":(":"😢"
    }
    output=""
    for i in words:
        
        output+=mapping.get(i,i)+""
    return output
message=input(">")

print(emoji_converter(message))