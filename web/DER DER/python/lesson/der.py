command = ""
while True:
    command = input(">").lower()
    if command == "start":
        print("Music Started!")
    elif command == "stop":
        print("Music Stopped!")
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

