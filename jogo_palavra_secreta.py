import os # importando funções do sistema operacional
palavra_secreta = 'perfume' # nova_v
letras_acertadas = '' # nova_v | armazena letras acertadas
numero_tentativas = 0 # nova_v
while True:
    letra_digitada = input('Digite uma letra: ') # nova_v
    numero_tentativas += 1 # contabilizando total de tentativas
    if len(letra_digitada) > 1: # impedindo mais de 1 caracter
        print('Digite apenas uma letra.')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada # arquivo letras acertadas  
    palavra_formada = '' # nova_v | code p/ ver letras acertadas ou *
    for letra_secreta in palavra_secreta: # nova_v (letra_secreta)
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU, PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = '' # zerando variável
        numero_tentativas = 0 # zerando variável