from androidhelper import Android

def text_bin(char):
    ascii = ord(char)
    bin_string = ""
    while ascii != 0:
        resto = ascii % 2
        ascii //= 2
        bin_string = str(resto) + bin_string
    return "0" * (8 - len(bin_string)) + bin_string


def bin_text(code_8bit):
    soma = sum(2**i * int(code_8bit[8-i-1]) for i in range(8))
    return chr(soma)


while True:
    op = input("Texto para binario ou binário para texto?(1/2) ")
    if op in ["1", "2"]:
        break

while True:
    opd = input("Quer colar?(s/n) ")
    if opd in ["s", "n"]:
        break

copied = opd == "s"

if op == "1":
    if copied:
        texto = Android().getClipboard().result.strip()
        print("Você colou:", texto)
    else:
        texto = input("Digite o texto que vai ser convertido: ").strip()
    saida = []
    for char in texto:
        saida.append(text_bin(char))
    v = " ".join(saida)
else:
    if copied:
        codigo = Android().getClipboard().result.strip()
        print("Você colou:", codigo)
    else:
        codigo = input("Diga o código binário: ").strip()
    codigo = "".join([i for i in codigo if i in ["0", "1"]])
    assert len(codigo) % 8 == 0, "O código deve ser dividido em sessões de 8 bit"
    codigo = [codigo[8*(i-1):8*i] for i in range(1, 1+len(codigo)//8)]
    texto = ""
    for section in codigo:
        texto += bin_text(section)
    v = texto

print("Tradução:", v)

while True:
    op = input("Deseja copiar?(s/n) ")
    if op in ["s", "n"]:
        break

if op == "s":
    a = Android()
    a.setClipboard(v)
