# =====================================================================
# Projeto: FutureWork Balance - Monitoramento de Bem-Estar e Requalificação no Futuro do Trabalho
# Integrantes:
# - Nome: Josué Faria da Silva – RM: 563819
# - Nome: Julia Schiavi – RM: 562418
# =====================================================================

import os

# Arquivo onde os resultados serão armazenados
ARQUIVO_HISTORICO = "historico_bem_estar.txt"

# Base de cursos do futuro 
cursos_futuro = {
    "ALTO": [
        "Gestão do Estresse no Trabalho Digital",
        "Saúde Mental e IA: Como usar tecnologia a seu favor",
        "Mindfulness para Ambientes Remotos"
    ],
    "MÉDIO": [
        "Produtividade Sustentável em Escritórios Híbridos",
        "Organização Inteligente com Ferramentas de IA",
        "Inteligência Emocional no Trabalho"
    ],
    "BAIXO": [
        "Trabalhando com IA: Carreiras do Futuro",
        "Autogestão de Carreira e Lifelong Learning",
        "Criatividade e Resolução de Problemas"
    ]
}

# Sistema de medalhas 
def atribuir_medalha(risco):
    if risco == "BAIXO":
        return "🏅 Medalha de Bem-Estar Excelente"
    elif risco == "MÉDIO":
        return "🥈 Medalha de Equilíbrio Parcial"
    else:
        return "🥉 Medalha de Atenção Necessária"

# IA baseada em regras + score
def avaliar_bem_estar(estresse, sono, atividade):
    score = 0

    if estresse >= 7:
        score += 3
    elif estresse >= 5:
        score += 2
    else:
        score += 1

    if sono < 6:
        score += 3
    elif sono < 7:
        score += 2
    else:
        score += 1

    if atividade >= 4:
        score -= 1
    elif atividade == 0:
        score += 2

    if score >= 6:
        return "ALTO"
    elif score >= 4:
        return "MÉDIO"
    else:
        return "BAIXO"

# Recomendações baseadas no risco
def recomendar_acoes(risco):
    if risco == "ALTO":
        acoes = ["Agendar apoio psicológico", "Reduzir carga horária temporariamente"]
    elif risco == "MÉDIO":
        acoes = ["Realizar pausas durante o trabalho", "Praticar exercícios leves"]
    else:
        acoes = ["Manter rotina saudável", "Continuar com equilíbrio pessoal"]
    return acoes, cursos_futuro[risco]

# Registrar histórico em arquivo
def salvar_historico(nome, risco):
    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - Risco: {risco}\n")

# Mostrar histórico
def mostrar_historico():
    if not os.path.exists(ARQUIVO_HISTORICO):
        print("\n📁 Nenhum histórico registrado ainda.")
        return
    
    print("\n=== 📚 HISTÓRICO DE AVALIAÇÕES ===")
    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


# ===========================
# SISTEMA PRINCIPAL
# ===========================

print("🧠💻 Bem-vindo(a) ao FutureWork Balance ")
print("Aqui, tecnologia e cuidado humano trabalham juntos para transformar o futuro do trabalho.\n")

while True:

    tentativas = 0  # contador de erros

    #validação nome
    try:
        while True:
            nome = input("Digite seu nome: ").strip()

            if nome.replace(" ", "").isalpha():
                break
            else:
                tentativas += 1
                print("❌ Digite um nome válido (somente letras).")

            if tentativas >= 3:
                print("\n❌ Muitas tentativas inválidas. O sistema será encerrado.")
                exit()

        while True:
            #validação do nível de estresse
            try:
                estresse = int(input("Nível de estresse (0 a 10): "))
                if 0 <= estresse <= 10:
                    break
                else:
                    raise ValueError
            except ValueError:
                tentativas += 1
                print("⚠️ Digite um número válido entre 0 e 10.")

            if tentativas >= 3:
                print("\n❌ Muitas tentativas inválidas. O sistema será encerrado.")
                exit()

        
        while True:
            #validação das horas de sono
            try:
                sono = int(input("Horas de sono por noite: "))
                if sono >= 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                tentativas += 1
                print("⚠️ Digite apenas números válidos e positivos.")

            if tentativas >= 3:
                print("\n❌ Muitas tentativas inválidas. O sistema será encerrado.")
                exit()

        
        
        while True:
            #validação da atividade física
            try:
                atividade = int(input("Dias de atividade física por semana: "))
                if atividade >= 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                tentativas += 1
                print("⚠️ Digite apenas números válidos e positivos.")

            if tentativas >= 3:
                print("\n❌ Muitas tentativas inválidas. O sistema será encerrado.")
                exit()

        # Avaliação final
        risco = avaliar_bem_estar(estresse, sono, atividade)
        acoes, cursos = recomendar_acoes(risco)
        medalha = atribuir_medalha(risco)

        print("\n✨ RESULTADO DA AVALIAÇÃO ✨")
        print(f"Nome: {nome}")
        print(f"Risco detectado: {risco}")
        print(f"Recompensa: {medalha}")

        print("\n📌 Ações recomendadas:")
        for a in acoes:
            print(f"- {a}")

        print("\n📚 Cursos sugeridos para o futuro do trabalho:")
        for c in cursos:
            print(f"- {c}")

        salvar_historico(nome, risco)

        ver = input("\nDeseja visualizar o histórico geral? (s/n): ").lower()
        if ver == "s":
            mostrar_historico()

    except ValueError:
        print("\n📢 Erro inesperado.")
        continue

    repetir = input("\nDeseja avaliar outro colaborador? (s/n): ").lower()
    if repetir != "s":
        print("\n🌟 Obrigado por utilizar o FutureWork Balance!")
        print("Lembre-se: o futuro do trabalho começa com o cuidado de hoje.\n")
        break
