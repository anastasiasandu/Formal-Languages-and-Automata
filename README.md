# Formal-Languages-and-Automata

PROJECT 1 <br />
Exercise 1. <br />
Implement a library/program in a programming language of your choosing to load and validate a DFA input file. <br />
dfaparserengine.py dfaconfigfile <br />
Exercise 2. <br />
Implement a library/program in a programming language of your choosing to test acceptance of a DFA - loaded from a DFA config file. <br />
dfaacceptanceengine.py dfaconfigfile word to test <br />
<br />
    PROJECT 2 <br />
Exercise  1. <br />
Extend  the  library/program  you  implemented  in  L1.Ex1  toload and validate a NFA input file. <br />
nfaparserengine.py   nfaconfigfile <br />
Exercise 2. <br />
Implement  a  library/program  in  a  programming  language  ofyour choosing to test acceptance of a NFA - loaded from a NFA config file. <br />
nfaacceptanceengine.py   nfaconfigfile  word to test <br />
Exercise 3. <br />
Implement  a  library/program  in  a  programming  language  ofyour choosing to convert a NFA - loaded from a NFA config file, to a DFA. <br />
nfaconversionengine.py   nfaconfigfile <br />  
Exercise 4.( Bonus)  <br />
Implement a library/program in a programming lan-guage of your choosing to test acceptance of anε−NFA. <br />
enfaacceptanceengine.py   enfaconfigfile  word to test <br />
<br />
    PROJECT 3 <br />
Exercise 1.<br />
Implement a library/program in a programming language of your choosing to simulate the Myhill-Nerode theorem - minimize a DFA to thesmallest DFA with the same level ofcompleteness. <br />
dfaminimizationengine.py  dfaconfigfile <br />
The above command should print the resulted DFA in the format presented in L1.Appendix <br />
Exercise 2.  <br />
Implement a library/program in a programming lan-guage of your choosing to minimize a DFA to the smallest (potentially) incom-plete <br />
DFA.advdfaminimizationengine.py  dfaconfigfile <br />
The above command should print the resulted DFA in the format presented inL1.Appendix <br />
<br />
    PROJECT 4 <br /> 
Exercise 1. <br /> 
Implement a program in a programming language of your choosing to crawl a category of the ads listing website olx.ro and generate auto-matic  <br /> 
sub-categorizations of the listings using regular expressions. For the purpose of crawling and navigating through the HTML DOM tree, youmay use any <br /> 
specialized library you wish, in any programming language. For2p,  you  must  build  at  least4sub-categorization  filters,  and  display  theresults into the <br />  console.For3p,  you  must  build  at  least 10sub-categorization  filters,  and  display  theresults into the console. For4p,  you  must  build  at  least 10 <br /> 
sub-categorization  filters,  and  display  theresults into a webpage.  <br /> 
<br /> 
    PROJECT 5 <br /> 
<br /> 
Exercise 1. <br />
Create a program-readable format to fully describe aCon-text Free Grammar. Your format should  differentiate  between  terminals,non-terminals, productions  <br />
and start point. Implement  a  library/program  in  a  programming  language  of  your  choosing  toload and validate a CFG in the format you created. <br />
cfgvalidationengine.py   cfgconfigfile <br /> 
You must also include two additional files along with the script: <br />
•A READMDE file to describe your format <br />
•An example cfgconfigfile input <br />
Exercise 2. <br />
Implement  a  library/program  in  a  programming  language  ofyour choosing to simplify a CFG using: <br />
•“useless” reduction <br />
•“null” reduction <br />
•“unit” reduction <br />
cfgreductionengine.py  cfgconfigfile <br />
The  above  command  should  print  the  resulted  CFG  in  the  same  format  as  the input. <br />
<br />
    PROJECT 6 <br />
Exercise 1. <br />
Create a program-readable format to fully describe a TuringMachine, similar to L5.Ex1. Implement  a  library/program  in  a  programming  language  of  your  choosing  toload and validate a TM in the format you created. <br />
tmvalidationengine.py   tmconfigfile <br />
You must also include two additional files along with the script: <br />
•A READMDE file to describe your format <br />
•An example tmconfigfile input <br />
Exercise 2. <br />
Implement  a  library/program  in  a  programming  language  ofyour  choosing  to  run  an  input  against  a  TM  -  as  inSipser 3.8-  using  theformat you created.
