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
    
    def __clear(self):
        os.system("cls")
