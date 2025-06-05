# Jak nakonfigurovat nový disk ve Windows
Otevřeme program "diskpart" 
(například napsáním `diskpart` v commandline příkazovém řádku).  
(Potvrdíme spušeění jako admin, otevře se nové okno co vypadá jako terminál)
  
Tam napíšeme:  
```
list disk
select disk X
clean
change gpt
create partition primary
list partition
format fs=ntfs quick
assign p
```
Kde výsledek prvního příkazu ukáže všechny disky i když je
 jinak windows třeba neukazuje.  
`X` v druhé řádce je číslo disku se kterým chceme pracovat.  
Ideálně prázdný disk, protože příkaz `clean` na další řádce ho promaže a 
příkaz `change gpt` také a navíc změní typ pro partitioning, aby ho windows lépe poznalo.  
Poslední příkaz pak přiřadí disku i písmeno.

