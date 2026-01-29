def introduction_page() -> str:
    message = '''
        Music System
    *Register Song - 1
    *Create Playlist - 2
    *Exit - 5
    '''

    print(message)
    command = input("Command: ")
    return command