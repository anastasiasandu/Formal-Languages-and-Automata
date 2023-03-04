		    
		    = tm_config_file format details =



1) Template:


formatul general este cel pe care l-am folosit si pentru dfa/nfa-uri


particularitati de precizat:


- am considerat starile ca fiind numere

- sigma e alcatuit din litere mici ale alfabetului englez cu exceptia:
	= literelor 'r' si 'l' care vor reprezenta 'right', respectiv 'left' la parcurgerea tranzitiilor
	= litera 'x' care va inlocui caracterele 'parcurse'/'validate'
    + '*' - caracter special care in context desparte doua secvente ale input-ului

- limbajul de pe banda trebuie sa fie format din caractere din sigma + caracterul '_' care reprezinta ' '

- in cadrul tranzitiilor am considerat ca sablon:
	(stare curenta)","(caracter citit de pe banda)" "(1/2)","(stare urmatoare)
		(1)"x r"/"x l" - care inlocuieste caracterul de pe banda cu x si se deplaseaza 'r' (right) or 'l' (left)
		(2)"r"/"l" - care doar se deplaseaza pe banda

- ca reguli de validare:
	= printre stari trebuie sa se gaseasca si A (starea de accept) si R (starea de reject) 
	= fiecare stare si caracter din tranzitii trebuie sa existe in listele deja citite de stari/caractere sau sa faca parte din multimea {'_','x','r','l'}


daca toate aceste conditii sunt indeplinite, TM-ul este considerat valid



2) Exemplu ilustrat:


aceast tm va valida toate string-urile de forma:

W*W ,  unde W este format din orice combinatie a literelor 'a' si 'b'

3)
Metoda de rulare:
python3 tm_validation_engine.py tm_config_file
python3 tm_acceptance.py <cuvantul de verificat>



