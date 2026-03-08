risposta_corretta = 6.6

while True:
    dato = input("Ciao, quanto fa 2.6 + 4? (usa il punto): ")
    
    try:
        valore_float = float(dato)
        
        if valore_float == risposta_corretta:
            print("Allora sei più intelligente di quanto pensassi!")
            break
        else:
            print("Valore errato. Riprova!")
            
    except ValueError:
        print("Errore: non hai inserito un numero valido!")