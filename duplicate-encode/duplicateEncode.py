def duplicate_encode(word):
    
    encoder = {}
    for character in word:
        if character in encoder:
            encoder[character] = ')'
        else:
            encoder[character] = '('

    resultado = ""
    for character in word:
        resultado = resultado + encoder.get(character)
    
    return resultado


#Casos Tests: comprobar si los números de una fila son únicos.
if __name__ == '__main__':


    casoTest1 = "din"
    assert duplicate_encode(casoTest1) == "((("
    
    casoTest2 = "recede"
    assert duplicate_encode(casoTest2) == "()()()"