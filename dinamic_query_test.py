df_argentina = {
    'id' : '2',
    'month' : ['01', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO']
    }

final_month = []

month2 = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO']
month3 = ['ENE', 'FEB',  'MAR', 'ABR', 'MAY']
month4 = ['01', '02', '03', '04', '05']



for i in df_argentina['month']:
    if i in month2: 
        final_month = month2
        print('ja foi')
    elif i in month3: 
        final_month = month3
        print('ja foi')
    elif i in month4: 
        final_month = month4
    break

query = f'''
TESTANDO O CODIGO
SE PEGAR O MES {final_month[0]}
É PQ DEU CERTO
E AGORA O SEGUNDO MÊS {final_month[1]}
'''

print(query)
