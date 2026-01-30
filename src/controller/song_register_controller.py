from datetime import datetime
from typing import TypedDict

class SongInformations(TypedDict):
    title: str
    artist: str
    year: int


class SongRegisterController:
    def insert(self, new_song_informations: SongInformations) -> dict:
        #Principio da Responsabilidade Única
        try:
            self.__verify_songs_informations(new_song_informations)
            self.__verify_if_song_already_registered(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_songs_informations(self, new_song_informations: SongInformations) -> None:
        if len(new_song_informations["title"]) > 100:
            raise Exception("Song title with more than 100 characters.")

        current_year = datetime.now().year
        year = new_song_informations["year"]

        if year >= current_year:
            raise Exception("Invalid music year.")

    def __verify_if_song_already_registered(self, new_song_informations: SongInformations) -> None:
        #interação com Model
        pass

    def __insert_song(self, new_song_informations: SongInformations) -> None:
        #interação com Model
        pass

    def __format_response(self, new_song_informations: SongInformations) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_informations["title"]
            }
        }
    
    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err)
        }

