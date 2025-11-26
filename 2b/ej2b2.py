
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0: 
            return True      
        else:
            return False
    else:
        return False
    pass 


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el
# script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

print(check_leap_year(2023))
