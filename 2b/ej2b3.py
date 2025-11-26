
def triangle_area_calculate(base, height):
    # Write here your code
    if base <= 0 or height <= 0:
        raise ValueError("Number must be greater than 0.")
    return (base * height) / 2
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'scrip

print(triangle_area_calculate(33, 45))
