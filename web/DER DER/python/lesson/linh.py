command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Music already started")
        else:
            started = True
            print("Music started!")
    elif command == "stop":
        if not started:
            print("Music already stopped!")
        else:
             started = False
        print("Music stopped!")
    elif command == "help":
        print("""
Type - start to start the music
Type - stop to stop the music
Type - quit to exit
        """)
    elif command == "quit":
        break
    else:
        print(f"Command not found ({command})")


