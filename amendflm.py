from connectflm import *


# Create a function to update record(s) in a table in a database
def update_films():
    try:
        flConnect, flCursor = fl_access()

        # check if SongID exist before update
        film_id = int(input("Enter the FilmID to update a record: "))
        flCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))

        row = flCursor.fetchone()

        if row == None:
            print(f"No record with the FilmID {film_id} exists ")
        else:
            field_name = input("Enter the field (Title  or Year Released or Rating or Duration or Genre) ").title()
            if field_name not in ["Title" , "Year Released" , "Rating" , "Duration" , "Genre"]:
                print(f"Field {field_name} not a field name in the table")

            else:
                field_value = input(f"Enter the value for the field {field_name}: ")
                flCursor.execute(f"UPDATE tblFilms SET {field_name} = ? WHERE FilmID = ? ", (field_value,film_id,))
                flConnect.commit()
                print(f"Record {film_id} updated")            
    except sql.ProgrammingError as e:
        print(f"Update error: {e}")
        
    

if __name__ == "__main__":
    update_films()