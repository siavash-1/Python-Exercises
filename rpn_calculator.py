#se version
import os 
import time 
huvud_stack=[] 
def clear():
  os.system("cls") 

def lagg_till_tal(stacken):
stacken.insert(0, float(input("tal: "))) 
except ValueError: 
print("inte ett tal") 
lagg_till_tal(stacken) 
else: 
clear() 
def operation(stacken): #funktion för att använda en operation på stackens tal try: 
print("[+] [-] [/] [*] [r]") 
operator=input("> ") 
if operator=="+": 
stacken[0]=(stacken[0]+stacken[1]) 
stacken.pop(1) 
clear() 
elif operator=="-": 
stacken[0]=(stacken[1]-stacken[0]) 
stacken.pop(1) 
clear() 
elif operator=="*": 
stacken[0]=(stacken[0]*stacken[1]) 
stacken.pop(1) 
clear() 
elif operator=="/": 
stacken[0]=(stacken[1]/stacken[0]) 
stacken.pop(1) 
clear()
elif operator=="r": 
if stacken[0]<0: 
print("inte tillåtet att ta roten ur negativa tal!!!!!") 
time.sleep(2) 
clear() 
else: 
stacken[0]=(stacken[0]**(1/2)) 
clear() 
elif operator=="q": 
quit() 
else: 
print("inte en operator") 
operation(stacken) #om man skriver något som inte är en operator så körs funktionen om 
except IndexError: #om stacken inte har tillräckligt med tal i stacken print("inte tillräckligt med tal i stacken") 
time.sleep(2) 
clear() 
except ZeroDivisionError: #man kan inte dela med noll 
print("division med noll är förbjudet!!!!!!") 
time.sleep(2) 
clear() 
def huvud_funktion(stacken): #huvud funktionen som hanterar de andra funktionerna och tolkar användarens kommandon 
while True: 
print(""" 
[a : lägg till tal i stacken] [o : operation på tal] 
[d : ta bort första tal] [s : byt plats på första och andra talet i stacken] [c : rensa stacken] [q : avsluta] 
""") 
print(stacken) 
kommando=input(">: ") 
if kommando=="a": 
lagg_till_tal(stacken) 
elif kommando=="o": 
operation(stacken)
elif kommando=="d":#ta bort lägsta nivån av stacken 
try: 
stacken.pop(0) 
except IndexError: #om stacken är tom ska programmet inte göra något på drop och swap funktionerna 
pass 
finally: 
clear() 
elif kommando=="s":#byt plats på första och andra nivåen av stacken try: 
stacken[0],stacken[1]=stacken[1],stacken[0] 
except IndexError: 
pass 
finally: 
clear() 
elif kommando=="c": #rensa stacken 
stacken=[] 
clear() 
elif kommando=="q":#avsluta 
quit() 
else: 
clear() 
huvud_funktion(huvud_stack)
