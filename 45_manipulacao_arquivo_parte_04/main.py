try:
    arquivo = input("informe o nome do arquivo(sem extensoes)").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

    novo_texto= input("digite o texto:\n")

    with open(f"{arquivo}.txt,", "r", encoding="utf-8") as f:
        f.write(novo_texto)
except Exception as e:
    print(f"Nao foi possivel atualizar o arquivo. {e}")