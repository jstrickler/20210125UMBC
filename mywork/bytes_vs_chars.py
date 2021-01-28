

name = "Fred"
print(name[0])

bname  = b'Fred'
print(bname[0])

message = "39\u00B0"
print(message)
print(message[2])
print(len(message))

bmessage = message.encode()  # convert str to bytes  (encoded UTF)
print(bmessage)
print(len(bmessage))
print(bmessage[2])
print(bmessage[3])

print(name.encode())
print(bname.decode())
