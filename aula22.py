# Definição das perguntas, alternativas e respostas corretas
questions = [
    {
        "question": "Quem foi o primeiro presidente dos Estados Unidos?",
        "options": ["1. George Washington", "2. Abraham Lincoln", "3. Thomas Jefferson"],
        "answer": 1
    },
    {
        "question": "Em que ano a Segunda Guerra Mundial terminou?",
        "options": ["1. 1945", "2. 1939", "3. 1942"],
        "answer": 1
    },
    {
        "question": "Qual foi a civilização antiga que construiu as pirâmides de Gizé?",
        "options": ["1. Romanos", "2. Egípcios", "3. Maias"],
        "answer": 2
    },
    {
        "question": "Quem foi o imperador romano durante a erupção do Monte Vesúvio em 79 d.C.?",
        "options": ["1. Nero", "2. Tito", "3. Calígula"],
        "answer": 2
    },
    {
        "question": "Qual o nome da política de segregação racial que ocorreu na África do Sul?",
        "options": ["1. Apartheid", "2. Holocausto", "3. Jim Crow"],
        "answer": 1
    },
    {
        "question": "Qual foi a principal causa da Primeira Guerra Mundial?",
        "options": ["1. Assassinato do arquiduque Francisco Ferdinando", "2. Invasão da Polônia", "3. Ataque a Pearl Harbor"],
        "answer": 1
    },
    {
        "question": "Quem foi a primeira mulher a ganhar um Prêmio Nobel?",
        "options": ["1. Marie Curie", "2. Rosalind Franklin", "3. Ada Lovelace"],
        "answer": 1
    },
    {
        "question": "Em que ano Cristóvão Colombo chegou à América?",
        "options": ["1. 1492", "2. 1500", "3. 1607"],
        "answer": 1
    },
    {
        "question": "Qual a cidade-estado grega famosa por seus guerreiros espartanos?",
        "options": ["1. Atenas", "2. Esparta", "3. Corinto"],
        "answer": 2
    },
    {
        "question": "Quem escreveu a obra 'A Origem das Espécies'?",
        "options": ["1. Isaac Newton", "2. Albert Einstein", "3. Charles Darwin"],
        "answer": 3
    }
]

# Função para executar o quiz
def run_quiz():
    score = 0
    for i, question in enumerate(questions):
        print(f"\nPergunta {i+1}: {question['question']}")
        for option in question["options"]:
            print(option)
        answer = int(input("Digite o número da sua resposta: "))
        if answer == question["answer"]:
            print("Correto!")
            score += 1
        else:
            print("Incorreto.")
    
    print(f"\nVocê acertou {score} de {len(questions)} perguntas.")
    print("Gabarito:")
    for i, question in enumerate(questions):
        print(f"Pergunta {i+1}: {question['question']}")
        print(f"Resposta correta: {question['options'][question['answer'] - 1]}")

# Executa o quiz
if __name__ == "__main__":
    run_quiz()