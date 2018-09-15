def value_with_mask(value, mask):
    result = ''
    for c in mask:
        if c != 'X':
            result += c
        else:
            # Se nao tem mais caracteres em value, eh um erro.
            if len(value) == 0:
                return None
            result += value[0]
            value = value[1:]

    # Se sobrou algum caracter eh um erro.
    if len(value) > 0:
        return None

    return result
