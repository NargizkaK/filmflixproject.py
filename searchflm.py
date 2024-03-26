from connectflm import*

def search_film():
    try:
        flConnect, flCursor = fl_access()
       
        print_field = input("Search by FilmID or Title or Year Released  Rating or Duration or Genre: ")
 
        # check if search_field value entered is SongID
        if print_field == "FilmID":
            film_id = int(input(f"Enter the value for {print_field}: "))
            flCursor.execute("SELECT * FROM tblfilms WHERE FilmID = ?", (film_id,))
            row = flCursor.fetchone()
 
            if row is None:
                print(f"No record with FilmID {film_id} exists in the films table!!")
            else:
                print("*" * 100)
                print(f"FilmID{'':<3}|Title{'':<25}|yearReleased{'':<3}|Rating{'':<3}|Duration{'':<3}|Genre{'':<10}")
                print("*" * 100)
                print(f"{row[0]:<9}|{row[1]:<30}|{row[2]:<15}|{row[3]:<9}|{row[4]:<11}|{row[5]:<16}")
                print("-" * 100)
 
        elif print_field.title() in ["Title" , "Year Released" , "Rating" , "Duration" "Genre"]:
            str_input = input(f"Enter the value for {print_field}: ")
          
            flCursor.execute(f'SELECT * FROM tblfilms WHERE {print_field} LIKE ?', (f'%{str_input}%',))
           
            rows = flCursor.fetchall()
            if not rows:
                print(f"No record with the field {print_field} matching {str_input} in the films table!")
            else:
                # display all matched records from the songs table
                for records in rows:
                    print(records)
        else:
            print(f"Search field {print_field} value is invalid !")
            # print(type(f'%{str_input}%,'))
 
    except sql.ProgrammingError as e:
        print(f"Search error: {e}")
if __name__ == "__main__":
    search_film()
     