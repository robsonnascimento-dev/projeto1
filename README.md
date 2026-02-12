Sistema de Triagem Inteligente (S.T.I)

Projeto desenvolvido em Python com o objetivo de simular um sistema de cadastro e classificação de risco de pacientes em uma unidade de saúde.

O sistema realiza:
- Cadastro de pacientes
- Validação de CPF (evita duplicidade)
- Classificação de risco por nível de gravidade
- Cálculo de pontuação de prioridade
- Organização da fila de atendimento

---

Funcionalidades

✔ Cadastro de pacientes  
✔ Validação para impedir CPF duplicado  
✔ Classificação automática por cores de triagem  
✔ Cálculo de prioridade baseado em:
- Gravidade (peso maior)
- Tempo de espera  

✔ Estrutura de fila de atendimento  

---

Lógica de Classificação

A classificação segue o seguinte critério:

| Gravidade | Cor     | Prioridade |
|-----------|--------|------------|
| 8 a 10    | 🔴 Vermelho | Emergência |
| 5 a 7     | 🟡 Amarelo  | Urgente |
| 3 a 4     | 🟢 Verde    | Pouco urgente |
| 1 a 2     | 🔵 Azul     | Não urgente |

A pontuação é calculada com a fórmula:

Quanto maior a pontuação, maior a prioridade no atendimento.

---
Tecnologias Utilizadas

- Python 3
- Estruturas de dados:
  - `set` (controle de CPFs cadastrados)
  - `list` (fila de atendimento)
  - `dict` (dados do paciente)
