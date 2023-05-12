usuario = {
    'nombre': 'Juan',
    'apellidos': 'Penas',
    'telefono': {
        'casa': '7441234567',
        'movil': '7447654321'
    },
    'habilidades': ['tocar guitarra', 'ir a la playa', 'los animales'],
    # 'trabajo': ('Lu', 'Mie', 'Vie'),
}

# Items devuelve el atributo y valor del objeto
# for atributo, valor in usuario.items():
#     print("Atributo %s Valor %s" %(atributo, valor))

for valor in usuario.values():
    print("Valor %s" %(valor))

# # Accediendo a los atributos del objeto a otro objeto
# print('Telefono movil %s' %(usuario['telefono']['movil']))
# # Accediendo a los atributos del objeto a un array
# print('Habilidad %s' %(usuario['habilidades'][1]))
# # Accediendo a los atributos del objeto a una tupla
# print('Trabajo %s' %(usuario['trabajo'][2]))