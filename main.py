import random
import os
import time
import sys

     #FUNCOES
def escrever(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)  # velocidade (menor = mais rápido)
    print()  # quebra de linha no final

def input_animado(texto):
    escrever(texto)
    return input()

def limpar(): #Faz a troca de tela
    os.system("cls")

     #Script principal
limpar()
     
print('=' * 20)
print('BEM VINDO AO: E SE ?')
print('=' * 20)

menu = input('1. PLAY \n2. OPTIONS \n3. EXIT \n ')

if menu == '1':
    escrever("Carregando........")
    time.sleep(2)
    #limpar() #deve limpar o terminal (troca de tela)

    alimentos = ['Manga', 'Arroz', 'Feijao', 'Batata', 'macarrao', 'Morango', 'Biscoito', 'Doce', 'Leite', 'Banana'] #LISTA
    alimEscolhidos = random.sample(alimentos, 5) #RANDOMIZA A LISTA SELECIONADA 'alimentos'
    #SAMPLE ESCOLHE SEM REPETIR O ELEMENTO // CHOICE PODE REPETIR O ELEMENTO

    print(f'Voce vai ao Mercado ! \nChegando la voce olha a sua lista: {alimEscolhidos}')
    inp = input_animado('oque fazer? \n1.Ir fazer suas compras \n2.Ir embora')

    if  inp == '1':
        #limpar() #deve limpar o terminal (troca de tela)
        escrever("Andando.......")
        time.sleep(0.5)

        print('Voce foi no corredor das frutas.')

        verlista = input_animado('Deseja ver a lista ? \n sim/nao').strip().lower()

        if verlista == 'sim':
            escrever(alimEscolhidos)

        elif verlista == 'nao':
            escrever('Por enquanto to progrmando o SIM')
        else:
            escrever('ERRO Escolha sim ou nao')
            escrever('Impossivel de Continuar')
            exit()
            
        Tem_Fruta = input_animado('Vamos la!, possui fruta em sua lista ?\n').strip().lower()

        if Tem_Fruta == 'sim':
            pegarfruta = input_animado('Deseja pegar a fruta ?\n')

        elif Tem_Fruta == 'nao':
            escrever('Por enquanto to progrmando o SIM')
        else:
             print('ERRO Escolha sim ou nao')
             exit()
elif menu == '2':
    print('!!AINDA TRABALHANDO NISSO!!')
    exit()
elif menu == '3':
    exit()
