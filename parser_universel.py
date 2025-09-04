# POC-000 Parser Universel
# Démonstration simple : entrée brute → sortie ZGS
def parse_input(text: str) -> str:
    return f"⟦ZGS:: {text.strip()} ⟧"

if __name__ == "__main__":
    example = "Bonjour IA"
    print(parse_input(example))
