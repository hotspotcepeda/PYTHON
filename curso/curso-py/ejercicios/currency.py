# convierte a $ distintas monedas y despues las suma.

""" ¿Cuánto te queda en yuanes? 560
¿Cuánto te queda en yenes? 2455
¿Cuánto le queda en won? 3280 """

# 1 yuan = 0,14 $
# 1 yen = 0,0076 $
# 1 won = 0,00077 $

import emoji

yuan = int(input('\nInserte la cantidad de Yuanes: '))
yen = int(input('Inserte la cantidad de Yenes: '))
won = int(input('Inserte la cantidad de Wones: '))

yuan_dolar = (yuan * 0.14)
yen_dolar = (yen * 0.0076)
won_dolar = (won * 0.00077)

print("\nYUANES EN DOLARES:  ", yuan_dolar, "💲")
print("YENES EN DOLARES: ", yen_dolar, "💲")
print("WONES EN DOLARES: ", won_dolar, "💲")

suma_dolares = (yuan_dolar + yen_dolar + won_dolar)

print("\nTotal en dolares: ", suma_dolares,"🤑")
