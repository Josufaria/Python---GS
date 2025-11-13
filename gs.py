# =====================================================================
# Projeto: Monitoramento de Bem-Estar e Requalificação Profissional
# Integrantes:
# - Nome: Josué Faria da Silva – RM: 563819
# - Nome: Julia Schiavi – RM: 562418
# =====================================================================

# Função que avalia o risco de burnout com base em estresse, sono e atividade física
def avaliar_bem_estar(estresse, sono, atividade):
# Verifica alto risco: estresse alto e pouco sono
    if estresse >= 7 and sono < 6:
        return "ALTO"
# Verifica risco médio: estresse moderado ou sono insuficiente
    elif estresse >= 5 or sono < 7:
        return "MÉDIO"
# Caso contrário, risco baixo    
    else:
        return "BAIXO"
    
# Função que retorna ações e cursos recomendados conforme o nível de risco    
def recomendar_acoes(risco):
# Ações e cursos para risco alto
    if risco == "ALTO":
        acoes = ["Agendar consulta psicológica", "Reduzir carga horária temporariamente"]
        cursos = ["Gestão do Estresse", "Equilíbrio entre vida pessoal e trabalho"]
 # Ações e cursos para risco médio
    elif risco == "MÉDIO":
        acoes = ["Fazer pausas durante o expediente", "Praticar atividade física leve"]
        cursos = ["Mindfulness", "Inteligência emocional no trabalho"]
# Ações e cursos para risco baixo
    else:
        acoes = ["Manter hábitos saudáveis", "Continuar rotina equilibrada"]
        cursos = ["Aprendizado Contínuo", "Autogestão de Carreira"]
    return acoes, cursos

# Função principal do programa
def main():
    print("="*60)
    print("Sistema de Bem-Estar e Futuro do Trabalho")
    print("="*60)

while True:
        try:
           # Coleta o nome do usuário
            nome = input("\nDigite seu nome: ")

           # Solicita dados com validação
            estresse = int(input("Em uma escala de 0 a 10, qual seu nível de estresse? "))
            sono = int(input("Quantas horas você dorme por noite (em média)? "))
            atividade = int(input("Quantos dias por semana pratica atividade física? "))

           # Avalia o risco e obtém recomendações
            risco = avaliar_bem_estar(estresse, sono, atividade)
            acoes, cursos = recomendar_acoes(risco)

           # Exibe os resultados e recomendações
            print("\n Resultado da Avaliação:")
            print(f"Nome: {nome}")
            print(f"Nível de risco: {risco}")
            print("\n Ações recomendadas:")
            for acao in acoes:
                print(f"- {acao}")
            print("\n Cursos sugeridos:")
            for curso in cursos:
                print(f"- {curso}")

        except ValueError:
            # Exibe a mensagem de erro caso um número válido não seja digitado
            print("\n Por favor, digite apenas números válidos nas perguntas!")
            continue  # reinicia o loop

        # Pergunta se o usuário quer repetir o processo
        repetir = input("\nDeseja avaliar outro colaborador? (s/n): ").strip().lower()
        # Finaliza o programa
        if repetir != "s":
            print("\n Muito obrigado pela confiança. Cuide da sua saúde e continue aprendendo!")
            break 

# Executa o programa principal
if __name__ == "__main__":
    main()        