def validate_non_empty_string(value, field_name="Campo"):
    """
    Garante que as strings não estejam vazias.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Erro de Validação: {field_name} deve ser uma string não vazia.")
    return value.strip()

def validate_positive_number(value, field_name="Valor"):
    """
    Garante que valores numéricos sejam todos positivos, incluindo o zero.
    """
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"Erro de Validação: {field_name} deve ser um número >= 0.")
        #preços iguais à 0: possibilidade de produtos grátis (promoção de marketing ou cliente bonificado)
    return float(value)

def validate_positive_int(value, field_name="Quantidade"):
    """
    Garante que valores numéricos inteiros sejam todos positivos, incluindo o zero.
    """
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"Erro de Validação: {field_name} deve ser um número inteiro >= 0.")
    return value

def validate_min_length(value, min_len, field_name="Texto"):
    """
    Garante que string tenha um mínimo de caractere considerável.
    """
    if not isinstance(value, str) or len(value.strip()) < min_len:
        raise ValueError(f"Erro de Validação: {field_name} deve ter pelo menos {min_len} caracteres.")
    return value.strip()
