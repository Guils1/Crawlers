import requests
from lxml import html


nome=str(input("Digite seu nome:\n--> "))
print()
print(f'{"Seja bem vindo,%s.":^110}'%nome)
print()
while True:
    print(f'{"%s, você deseja comprar ou arrendar terras?":^110}'%nome)
    print()
    print(f'{"Tecle 1 para arrendar ou 2 para comprar.":^120}')
    resp=int(input("-->"))
    print()
    print()
    
    if resp==2:
        print('-='*20,'Fazendas para comprar no Brasil','-='*20)
        print()
        pag=requests.get('https://fazendaaberta.com.br/pesquisar/fazendas-a-venda-no-brasil?sort=&cidade=-1&tipoDeTransacao=VENDER&tipoImovel=FAZENDA&idAnuncio=&unidadeMedida=HECTARE&areaMinima=&areaMaxima=&valorMinimo=0&valorMaximo=0')
        venda=html.fromstring(pag.content)
        
        print(f'{"CIDADE":<60}', f'{"ÁREA":<30}',f'{"VALOR"}')
        print()
        
        for i in range(1,482):
            conteudo=venda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/a[1]/figure/h4/text()')
            area=venda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/div/div/dl[1]/dd/text()')
            valor=venda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/a[1]/div/text()')
            print(f'{conteudo[0]:.<58} {area[0]:.<35} {valor[0]:<30}')

    if resp==1:
        print('-='*20,'Fazendas para arrendar no Brasil','-='*20)
        pag=requests.get('https://fazendaaberta.com.br/pesquisar/fazendas-para-arrendar-no-brasil?sort=&cidade=-1&tipoDeTransacao=ARRENDAR&tipoImovel=FAZENDA&idAnuncio=&unidadeMedida=HECTARE&areaMinima=&areaMaxima=&valorMinimo=0&valorMaximo=0')
        arrenda=html.fromstring(pag.content)
        print(f'{"CIDADE":<60}', f'{"ÁREA":<25}',f'{"VALOR POR MÊS"}')
        print()
        for i in range(1,11):
            conteudo=arrenda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/a[1]/figure/h4/text()')
            area=arrenda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/div/div/dl[1]/dd/text()')
            v_mes=arrenda.xpath(f'/html/body/div[1]/main/section[1]/div/div[2]/div[{i}]/div/div/div/dl[2]/dd/text()')
            print(f'{conteudo[0]:.<58} {area[0]:.<25} {v_mes[0]:<15}')
            print()
        print('-='*60)
        
    ro=input('Digite (Home) para voltar para a página inicial ou (Exit) para finalizar a navegação!\n-->')
    if ro.upper()=='HOME':
        continue
    elif ro.upper()=='EXIT':
        break
    print('=-'*80)
    print()
    print()
print('\nObrigado pela presença, até a próxima!'.upper())