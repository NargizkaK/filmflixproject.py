import sqlite3 as sql # imported sqlite module


def fldb_access():
    try:
     # how to access DB
        with sql.connect('filmflix.db') as flConnect:
            flCursor = flConnect.cursor() 
            
            return flConnect, flCursor
    
    except sql.OperationalError as e:  
        print(f"Connection failed: {e}")
        
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
   
    except sql.Error as er:
        print(f"This error: {er}")
   
        

if __name__ == "__main__":
    
    fldb_access()