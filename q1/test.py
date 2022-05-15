rm = input('Insira seu RM (Apenas números): ')
rmStr = [int(i) for i in str(rm)]
rmSum = rmStr[0] + rmStr[1] + rmStr[2] + rmStr[3] + rmStr[4]
cardPicker = {
    (1, 2): "Rei Espadas",
    (3, 4): "Rei Ouros",
    (5, 6): "As Ouros",
    (7, 8): "7 Ouros",
    (9, 0): "10 Espadas"
}

rm_Int2Str = repr(rmSum)
lastDigitRm = rm_Int2Str[-1]
card = list(cardPicker.keys())[
    list(cardPicker.values()).index(int(lastDigitRm))]
print(card)
