# Cores ANSI para Texto (de 30 a 37, e de 90 a 97 para brilhantes)
cores_texto = {
    "preto": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    "preto_brilhante": "\033[90m",
    "vermelho_brilhante": "\033[91m",
    "verde_brilhante": "\033[92m",
    "amarelo_brilhante": "\033[93m",
    "azul_brilhante": "\033[94m",
    "magenta_brilhante": "\033[95m",
    "ciano_brilhante": "\033[96m",
    "branco_brilhante": "\033[97m"
}

# Cores ANSI para Fundo (de 40 a 47, e de 100 a 107 para brilhantes)
cores_fundo = {
    "preto_fundo": "\033[40m",
    "vermelho_fundo": "\033[41m",
    "verde_fundo": "\033[42m",
    "amarelo_fundo": "\033[43m",
    "azul_fundo": "\033[44m",
    "magenta_fundo": "\033[45m",
    "ciano_fundo": "\033[46m",
    "branco_fundo": "\033[47m",
    "preto_brilhante_fundo": "\033[100m",
    "vermelho_brilhante_fundo": "\033[101m",
    "verde_brilhante_fundo": "\033[102m",
    "amarelo_brilhante_fundo": "\033[103m",
    "azul_brilhante_fundo": "\033[104m",
    "magenta_brilhante_fundo": "\033[105m",
    "ciano_brilhante_fundo": "\033[106m",
    "branco_brilhante_fundo": "\033[107m"
}

# Resetando para as cores padrão
reset = "\033[0m"

# Você pode acessar essas cores da seguinte forma:
# Exemplo de como usar:
print(f"{cores_texto['verde_brilhante']}Texto vermelho{reset}")
print(f"{cores_fundo['preto_brilhante_fundo']}Texto com fundo azul{reset}")
