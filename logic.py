#-*- coding: utf-8 -*-
from sql_interface import DbChinook

class Search_engine():
    def __init__(self, db):
        self.db = db

    def select_all_tracks(self):
        """Вибрати всі записи про треки"""
        res = self.db.select("""SELECT * FROM tracks;""")
        return res

    def select_name_tracks(self, text):
        """Вибрати всі треки із іменем, заданим користувачем"""
        text = '%'+text+'%'
        res = self.db.select('''SELECT t.Name, ar.Name, a.Title, t.Milliseconds
                            FROM tracks t
                            INNER JOIN genres g
                            USING(GenreId)
                            INNER JOIN albums a
                            ON a.AlbumId = t.AlbumId 
                            INNER JOIN artists ar
                            ON ar.ArtistId = a.ArtistId
                            WHERE t.Name LIKE ?; ''', text)
        return res

    def select_artist(self, text):
        """Вибрати всі треки із виконавцем, заданим користувачем"""
        text = '%'+text+'%'
        res = self.db.select('''SELECT t.Name 
                            FROM tracks t
                            INNER JOIN albums a
                            ON a.AlbumId = t.AlbumId 
                            INNER JOIN artists ar
                            ON ar.ArtistId = a.ArtistId
                            WHERE ar.Name LIKE ?; ''', text)
        return res
    
    def select_genre(self, text):
        """Вибрати всі треки із жанром, заданим користувачем"""
        text = '%'+text+'%'
        res = self.db.select('''SELECT t.Name
                            FROM tracks t
                            INNER JOIN genres g
                            USING(GenreId)
                            WHERE g.Name LIKE ?; ''', text)
        return res

if __name__=="__main__":
   from sql_interface import DbChinook
   db = DbChinook()
   engine = Search_engine(db)
   engine.select_all_tracks()