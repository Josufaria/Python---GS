# =====================================================================
# Projeto: Monitoramento de Bem-Estar e Requalificação Profissional
# Integrantes:
# - Nome: Josué Faria da Silva – RM: 563819
# - Nome: Julia Schiavi – RM: 562418
# =====================================================================

def avaliar_bem_estar(estresse, sono, atividade):

    if estresse >= 7 and sono < 6:
        return "ALTO"

    elif estresse >= 5 or sono < 7:
        return "MÉDIO"
    
    else:
        return "BAIXO"