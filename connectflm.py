import sqlite3 as sql # imported sqlite module
def fl_access():
    try:
        with sql.connect('Python/project.py/filmflix.db') as flConnect:
            flCursor = flConnect.cursor() #cursor function is used to call the execute method
            
            return flConnect, flCursor
    
    except sql.OperationalError as e:   # raise sqlerror
        #use the errorr raised to handle the exeption/error
        print(f"Connection failed: {e}")
        
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
   
    except sql.Error as er:
        print(f"This error: {er}")
   
        

if __name__ == "__main__":
    
    fl_access()
