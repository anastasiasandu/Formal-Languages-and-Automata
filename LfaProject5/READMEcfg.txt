= cfg_config_file format details =



1) Template:


formatul general este cel pe care l-am folosit si pentru dfa/nfa-uri


particularitati de precizat:


- am considerat variabilele ca fiind doar litere de tipar ale ale alfabetului englez
("The variable symbols often are represented by capital letters" - Lecture 8)

- printre simbolurile ce reprezinta terminale, "*" reprezinta sirul vid

- in cadrul regulilor de transformare a variabilelor am considerat ca sablon:
	(variabila de inlocuit)"-"(grup de variabile si/sau terminale cu care se inlocuieste, separate prin " ")

- variabila de start este introdusa la final pentru a fi retinuta separat (se verifica astfel si unicitatea ei)

- ca reguli de validare:
	= fiecare caracter (variabila/terminal) trebuie sa existe in listele deja citite de variabile/terminale
	= cel putin unul din grupurile din dreapta semnului "-" trebuie sa fie format doar din caractere de tip terminal pentru a asigura producerea unor string-uri finite


daca toate aceste conditii sunt indeplinite, CFG-ul este considerat valid



2) Exemplu ilustrat:


acest cfg va valida toate string-urile de forma:

0.....0 1.....1 2.....2 2.....2 1.....1 0.....0
(n ori) (m ori) (p ori) (p ori) (m ori) (n ori)

3) Metoda de rulare
python3 cfg_validation_engine.py cfg_config_file
