# 📘  Monitoramento de Bem-Estar e Requalificação Profissional  

## 🧠 Sobre o Projeto  
Este projeto tem como objetivo **avaliar o risco de burnout** de colaboradores no contexto do **Futuro do Trabalho**, considerando três fatores essenciais para o bem-estar:  
- Nível de **estresse** 😫  
- Quantidade de **horas de sono** 😴  
- Frequência de **atividade física** 🏃‍♂️  

Com base nesses dados, o sistema classifica o risco em **ALTO**, **MÉDIO** ou **BAIXO**, oferecendo **ações recomendadas** e **sugestões de cursos** voltados para desenvolvimento pessoal e saúde mental.

---

## ⚙️ Funcionalidades  
✔️ Coleta de dados do usuário com validação;
✔️ Classificação automática do nível de risco;  
✔️ Recomendações personalizadas; 
✔️ Loop contínuo para avaliação de vários colaboradores;  
✔️ Tratamento de erros (entradas inválidas). 

---

## 🧩 Estrutura do Código  

### 🔍 1. `avaliar_bem_estar(estresse, sono, atividade)`  
Função que avalia o risco com base nas combinações de estresse e sono.

### 🎓 2. `recomendar_acoes(risco)`  
Retorna ações e cursos indicados conforme o nível de risco.

### 🖥️ 3. Loop principal  
Realiza:  
- Coleta de nome e dados numéricos  
- Validação  
- Saída formatada  
- Pergunta para continuar ou encerrar  

---


## 👩‍💻 Desenvolvedores  
- **Josué Faria da Silva** – RM: 563819  
- **Julia Schiavi** – RM: 562418  