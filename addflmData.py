from connectflm import *

def add_film():
    try:
        flConnect, flCursor = fl_access()
        
        film_title= input('Enter film title: ')
        film_yearReleased= int(input('Enter year release: '))
        film_rating= input('Enter Film rating: ')
        film_duration= int(input('Enter film duration in minutes: '))
        film_genre= input('Enter film genre: ')
        
        
       
        flCursor.execute('Insert into tblFilms values(Null,?,?,?,?,?)',(film_title,film_yearReleased,film_rating,film_duration,film_genre))
    
        flConnect.commit()
        print(f'{film_title}insert in the film table')
    except sql.OperationalError as e:
        print(f'Failed because: {e}')
            
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
   
    except sql.Error as er:
        print(f"This error: {er}")
if __name__ == "__main__":
    add_film()        
