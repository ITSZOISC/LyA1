import pandas as pd

def analizador_lexico(matriz_transicion, palabra):
    estado_actual = 'q0'
    resultado = []

    # inicio
    resultado.append(('Este es el inicio', estado_actual))

    for letra in palabra:
        letra = str(letra)  # letra a cadena
        if estado_actual in matriz_transicion.index and letra in matriz_transicion.columns:
            estado_actual = str(matriz_transicion.loc[estado_actual, letra])
            resultado.append((letra, estado_actual))
            if estado_actual == 'error':
                print(f'Error: Caracter "{letra}" no válido.')
                break  # Termina si hay un error
        else:
            print(f'Error: Caracter "{letra}" no válido.')
            break  # Termina si hay un error

    # caracteres válidos y sus estados
    for letra, estado in resultado:
        print(f'Letra: {letra}, Estado: {estado}')

# Excel matriz transicion
archivo_excel = "matriz_transicion.xlsx"
matriz_transicion = pd.read_excel(archivo_excel, index_col=0)

# Palabra reservada
palabra_reservada = input("Ingrese la cadena: ")

# resultado análisis léxico
analizador_lexico(matriz_transicion, palabra_reservada)


