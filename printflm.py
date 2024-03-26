from connectflm import*

def print_films():
    try:
        flConnect, flCursor = fl_access()
        flCursor.execute("SELECT * FROM tblFilms")
 
        # fetch all selected records using the fetchall method and assigned it to a variable
        all_films = flCursor.fetchall() # fetchall method fetches the selected records
 
        if all_films:
            #display a line of 100 * from left to right
            print("*" * 100)
            # format the heading using field names: SongID, Title, Artist, Genre
            print(f"FilmID{'':<3}|Title{'':<25}|yearReleased{'':<3}|Rating{'':<3}|Duration{'':<3}|Genre{'':<10}")
            print("*" * 100)
 
            for aFilm in all_films:
                # 0         1       2          3        
                #(1,       'Test', 'Tester', 'coding')
                print(f"{aFilm[0]:<9}|{aFilm[1]:<30}|{aFilm[2]:<15}|{aFilm[3]:<9}|{aFilm[4]:<11}|{aFilm[5]:<16}")
                print("-" * 100)
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    print_films()
