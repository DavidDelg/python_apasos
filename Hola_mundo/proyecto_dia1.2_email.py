# Generador de Email 

print('**** Bienvenido al generador de Email ****')
nombre = str(input('Digite su nombre: ')).lower()
apellido = str(input('Digite su apellido: ')).lower() 

generador_Email = nombre +'.'+ apellido + '@cuidadgotica.com'

print(f'''Tu nuevo email generado por el sistema es: 
      {generador_Email}
    **** Felicidades ****''')