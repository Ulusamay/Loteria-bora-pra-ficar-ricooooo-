from bs4 import BeautifulSoup
import requests
matriz = []
numeros = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
numerosComVezes = []
ordem = []
maiores = []
repetidos = []
print('QUANTO MAIOR DISTANCIA UM JOGO TIVER DO OUTRO, MAIS VAI DEMORAR PARA COLETAR OS DADOS!!')
doJogo = int(input('doJogo: '))
ateOJogo = int(input('ateOJogo: '))
print('Mostrando do Jogo ' + str(doJogo) + ' Até o Jogo ' + str(ateOJogo) + '...Aguarde')
for c in range(doJogo, ateOJogo+1):
    page = requests.get('https://confiraloterias.com.br/lotofacil/?concurso=' + str(c))
    soup = BeautifulSoup(page.text, 'html.parser')
    div = soup.find_all('div', class_='kit-lotofacil')
    for c in div:
        matriz.append(str(c.contents[0]))
for n in numeros:
    numerosComVezes.append([n, matriz.count(n)])
    ordem.append(matriz.count(n))
    print('Numero: ' + str(n) + ' Apareceu: ' + str(matriz.count(n)) + ' Vezes')
ordem.sort(reverse=True)
#print('NumerosComVezes: ', numerosComVezes)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('ORDEM DECRESCENTE: ', ordem)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
input()
