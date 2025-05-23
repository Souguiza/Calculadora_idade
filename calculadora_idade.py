from datetime import datetime, date

print("=== Calculadora de Idade ===")

# Entrada da data de nascimento
data_str = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")
data_nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()

# Data atual
data_hoje = date.today()

# Cálculo da idade
idade = data_hoje.year - data_nascimento.year
if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

print(f"\n🧓 Você tem {idade} anos.")

# Dias vividos
dias_vividos = (data_hoje - data_nascimento).days
print(f"📆 Você já viveu aproximadamente {dias_vividos} dias.")

# Dias até o próximo aniversário
proximo_aniversario = date(data_hoje.year, data_nascimento.month, data_nascimento.day)
if proximo_aniversario < data_hoje:
    proximo_aniversario = date(data_hoje.year + 1, data_nascimento.month, data_nascimento.day)

dias_para_aniversario = (proximo_aniversario - data_hoje).days
print(f"🎉 Faltam {dias_para_aniversario} dias para o seu próximo aniversário.")
