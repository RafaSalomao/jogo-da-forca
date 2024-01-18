import os
import random
import desenhos

palavra_misteriosa = ''
palavra_formada = ''
categoria = ''
letras_encontradas = ' '
letras_erradas = ''
numero_tentativas = 0
numero_de_erros = 0

# Lista de frutas
frutas = ['banana', 'laranja', 'maca', 'uva', 'abacaxi', 'morango', 'melancia', 'pera', 'manga', 'limao']
# Lista de animais
animais = ['cachorro', 'gato', 'elefante', 'leao', 'girafa', 'tigre', 'papagaio', 'macaco', 'zebra', 'urso']
# Lista de países
paises = ['brasil', 'estados unidos', 'canada', 'australia', 'china', 'japao', 'india', 'franca', 'alemanha', 'italia']
# Lista de cores
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja', 'preto', 'branco', 'marrom', 'cinza']
# Lista de profissões
profissoes = ['engenheiro', 'professor', 'medico', 'advogado', 'programador', 'enfermeiro', 'contador', 'designer', 'policial', 'chef']


# Imprime como está o desempenho do jogador
def status_jogo():   
    print()        
    print(f'Frase formada: {palavra_formada}')
    print('Letras erradas: ', ', '.join(letras_erradas))
    print(f'Dica: {categoria}')

# Desenha o boneco conforme os erros
def desenha_boneco():
    if numero_de_erros == 0:
        desenhos.desenho_0()
    elif numero_de_erros == 1:
        desenhos.desenho_1()
    elif numero_de_erros == 2:
        desenhos.desenho_2()
    elif numero_de_erros == 3:
        desenhos.desenho_3()
    elif numero_de_erros == 4:
        desenhos.desenho_4()
    elif numero_de_erros == 5:
        desenhos.desenho_5()
    elif numero_de_erros == 6:
        desenhos.desenho_6()
    elif numero_de_erros == 7:
        desenhos.desenho_7()

# imprime como a frase está formada.
def imprime_frase_formada():
    global palavra_formada
    for letra in palavra_misteriosa:
        if letra in letras_encontradas:
            palavra_formada += letra
        else:
            palavra_formada += '_'

# Verifica se todas as letras foram encontras
def valida_vitoria():
    if palavra_formada == palavra_misteriosa:
        print('Parabens! Você acertou.')
        print(f'Quantidade de tentativas {numero_tentativas}x.')
        return True
    return False # Caso não tenha ganhado, retorna Falso

# Verifica se o jogador cometeu 7 erros
def valida_derrota():
    if numero_de_erros == 7:
        print(f'Você perdeu! A palavra era {palavra_misteriosa}')
        return True
    return False # Caso não tenha perdido, retorna Falso

# Sistema sorteia a cateria e uma palavra
def sorteio_categoria_palavra():
    global palavra_misteriosa
    global categoria

    categoria_selecionada = random.randint(1, 5)

    if categoria_selecionada == 1:
        palavra_misteriosa = random.choice(frutas)
        categoria = 'Fruta'
    elif categoria_selecionada == 2:
        palavra_misteriosa = random.choice(animais)
        categoria = 'Animais'
    elif categoria_selecionada == 3:
        palavra_misteriosa = random.choice(paises)
        categoria = 'Países'
    elif categoria_selecionada == 4:
        palavra_misteriosa = random.choice(cores)
        categoria = 'Cores'
    elif categoria_selecionada == 5:
        palavra_misteriosa = random.choice(profissoes)
        categoria = 'Profissões'

sorteio_categoria_palavra()

while True:
    os.system('clear')

    palavra_formada = ''

    letra_digitada = input('Digite uma letra: ').lower()

    # Valida se mais de uma letra foi digitada
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra já foi digitada
    if (letra_digitada in letras_encontradas) or (letra_digitada in letras_erradas):
        print('Essa letra já foi digitada')
    # Guarda as letras acertadas pelo usuário
    elif letra_digitada in palavra_misteriosa:
        letras_encontradas += letra_digitada
    # Guarda as letras erradas    
    else:
        letras_erradas += letra_digitada
        numero_de_erros += 1
    
    imprime_frase_formada()

    status_jogo()

    desenha_boneco()

    numero_tentativas += 1

    # Finaliza o jogo em caso de vitória ou derrota
    if valida_vitoria() or valida_derrota():
        break

    input('Digite [enter] para continuar...')
