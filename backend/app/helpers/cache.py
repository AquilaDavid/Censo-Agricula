import hashlib


def gerar_chave_cache(prefixo, valor):
    return (
        f"{prefixo}:"
        f"{hashlib.md5(valor.encode()).hexdigest()}"
    )