import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:

        self.__clear()

        print("Implement new music.")
        
        title = input("Determine the name of the song: ")
        artist = input("Determine the name of the artist: ")
        year = input("Determine the year of the publication: ")

        new_song_informations = {
            "title": title, "artist": artist, "year": year
        }

        return new_song_informations
    
    def registry_song_success(self, controller_response: dict) -> None:
        self.__clear()
        message = """
            Music successfully registered!

            * Title: {}
            * Count: {}
        """.format(
            controller_response["attributes"]["title"],
            controller_response["count"]
        )
        print(message)
    
    def registry_song_fail(self, controller_response: dict) -> None:
        self.__clear()
        message = """
            Failure to record music!

            * Erro: {}
        """.format(
            controller_response["error"],
        )
        print(message)

    def __clear(self):
        os.system("cls")