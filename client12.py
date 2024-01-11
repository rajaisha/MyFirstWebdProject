from socket import
client=connect()
client.connect(("192.168.206.109",9000))
print(client.recv(1024).decode())
client.send(bytes("WELCOME IN MY WORLD","UFT-8"))
While True:
    sm=(client.recv(1024)).decode()
    print("server:",sm)
    cm=input("client:")
    client.send(bytes(cm,"uft-8"))
    if sm=="bye" or "BYE":
        print("\n_______________________________________")
        print("CHAT HAS BEEN SAVED")
        print("\n_______________________________________")
        break
    else:
        continue
client=sm
