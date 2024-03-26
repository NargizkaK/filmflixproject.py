from connectflm import *


def delete_films():
    try:
        flConnect, flCursor = fl_access()
        
        #check if songID exist before delete
        film_id = int(input(f"Enter the filmID to delete records" ))
        flCursor.execute("SELECT * FROM tblFilms WHERE FilmID = ?", (film_id,))
        row = flCursor.fetchone()
        
        #invoke the function method and assing it to a variable called row
        row = flCursor.fetchone # fetch single or unique record
        
        if row == None: 
            print(f'No record with FilmID {film_id} in the films table!')
        else: #if there is a match with song ID provided
            flCursor.execute('Delete from tblfilms where filmID = ?',(film_id,))
            flConnect.commit()
            
            print(f'Record {film_id} deleted from the tblFilms table')
            
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    delete_films()

        
        
        