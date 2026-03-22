import random
import os
import time
import sys

def escrever(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)  # velocidade (menor = mais rápido)
    print()  # quebra de linha no final

def limpar(): #Faz a troca de tela
    os.system("cls")


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





elif menu == '2':
    print('!!AINDA TRABALHANDO NISSO!!')
    exit()
elif menu == '3':
    exit()
