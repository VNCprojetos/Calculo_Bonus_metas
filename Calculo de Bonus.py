meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 260000
nota = 9

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Ganhou Bonus por meta alcançada, Bonus do funcionario foi de {}'.format(bonus))
    print('Recebeu a Nota: {}'.format(nota))

elif nota >= 9 or (vendas_funcionario > meta_funcionario):
    bonus2 = 0.01 * vendas_funcionario
    print('Funcionario Ganhou bonus por Nota ou Meta Individual, Bonus de {}'.format(bonus2))
    print('Recebeu a Nota: {}'.format(nota))
else:
    print('Funcionario não tem direito ao bonus')


# PODE ALTERAR TANTO A PORCENTAGEM DE BONUS TANTO OS DADOS DAS VENDAS DE ACORDO
# COM O MES E A INTENSÃO SERÁ GERAR O RESULTADO DA COMISSÃO DO FUNCIONARIO, MAS PARA
# ISSO A META LOJA E A META FUNCIONARIO DEVEM SER ATINGIDAS JUNTAS.
