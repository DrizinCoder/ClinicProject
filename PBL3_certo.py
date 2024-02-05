'''O QUE AINDA TENHO QUE FAZER!!!
popular o codigo com a função popular codigo
concertar as entradas para o molde correto
Aplicar o metodo de herança
'''

import os
from PBL3Classes import Paciente
from PBL3Classes import Sessão
from PBL3Classes import Clinica
from PBL3Classes import Recepção
from PBL3Classes import Dentista
from PBL3Funções import criarlinha
from PBL3Funções import popularSistema

# Programa principal

sessaoAtiva = 0
pacienteID = 0
sessaoID = 0
Nome = 0

c = Clinica()
r = Recepção()
d = Dentista()
popularSistema()
os.system('cls')

while True:

    print('''
1- Recepção
2- Dentista
0- Sair
''')
    
    while True:

        try:
            seleçãoDeMenu = int(input('Escolha o menu referente ao seu cargo na clínica: '))
            if seleçãoDeMenu >= 3:
                print('Essa opção não está presente no menu.')
            else:
                break
        
        except ValueError:
            print('Opção inválida, digite novamente')

    os.system('cls')


    while seleçãoDeMenu == 1:

        criarlinha()
        print('''
1 - Cadastrar nova sessão clinica 
2 - Listar sessões clinicas 
3 - Buscar sessões clinicas *
4 - Iniciar sessões clinicas *
5 - Cadastrar novo paciente 
6 - listar pacientes
7 - Marcar consulta   
8 - Listar horários marcado de um paciente
9 - Confirmar se paciente está na sessão e adiciona-lo a fila
10 - Listar próximo paciente da fila de atendimento
11 - Listar consultas realizadas na sessão
12 - Encerrar sessão *               
0 - Sair do menu "Recepção"   
    ''')
        criarlinha()

        while True:

            try:
                escolhaMenuRecep = int(input('Escolha a operação a ser feita: '))
                break
        
            except ValueError:
                print('Opção inválida, digite novamente')
        
        os.system('Cls')
    
        if escolhaMenuRecep == 1:
            data = input('Digite a data da sessão [dd/mm/aaaa]: ')
            horario = input('Digite o horario de inicio da sessão [hh:mm]: ')
            tempoSessao = input('Digite o tempo da sessão: ')
            sessaoID += 1
            s = Sessão(data, horario, tempoSessao, sessaoID)
            r.adicionarSessao(s)           
        
        elif escolhaMenuRecep == 2:
            r.listarSessoes()
        
        elif escolhaMenuRecep == 3:
            sessaoBuscada = c.buscarSessao()

            if sessaoBuscada != None:
                print(f'A sessão encontrada: Data: {sessaoBuscada['Data']} | Horario: {sessaoBuscada['Horario']} | Tempo da sessao: {sessaoBuscada['Tempo da Sessao']}')

            else:
                print('Nenhuma sessão encontrada.')

        elif escolhaMenuRecep == 4:
            sessaoAtiva = c.iniciarSessao()

            if sessaoAtiva == None:
                print('A sessão não pode ser iniciada pois não esta cadastrada no sistema.')
        
        elif escolhaMenuRecep == 5:
            nome = input('Digite o nome do paciente: ')
            cpf = input('Digite o CPF do paciente: ')
            pacienteID += 1
            p = Paciente(nome, cpf, pacienteID)
            r.adicionarPaciente(p)
        
        elif escolhaMenuRecep == 6:
            r.listarPacientes()
            
        elif escolhaMenuRecep == 7:
            cpf = input('Digite o CPF do paciente: ')
            r.marcarHorario(cpf)

        elif escolhaMenuRecep == 8:
            cpf = input('Digite o CPF do paciente: ')
            r.horarioPacientes(cpf)
        
        elif escolhaMenuRecep == 9:
            cpf = input('Digite o CPF do paciente: ')
            r.confirmarHorario(sessaoAtiva, cpf)
        
        elif escolhaMenuRecep == 10:
            r.listarPrimeiroDaFila()
        
        elif escolhaMenuRecep == 11:
            r.listarConsultas()
        
        elif escolhaMenuRecep == 12:
            if sessaoAtiva == 0 or sessaoAtiva == None:
                print('nenhuma sessão iniciada. Não é possível encerrar sessão')
            
            else:
                sessaoAtiva = c.encerrarSessao(sessaoAtiva)

        elif escolhaMenuRecep == 0:
            seleçãoDeMenu = 10
        
        else:
            print('opção inválida. Digite uma opção disponível.')
    
    while seleçãoDeMenu == 2:

        criarlinha()
        print('''
1- Procurar sessão clínica registrada
2- Iniciar Sessão clínica
3- Atender paciente
4- Anotar prontuário
5- Ler primeiro prontuário de um paciente
6- Ler último prontuário de um paciente
7- encerrar sessão
0- Sair do menu "Dentista"
''')
        criarlinha()

        while True:

            try:
                escolhaMenuDentista = int(input('Escolha a operação a ser feita: '))
                break
        
            except ValueError:
                print('Opção inválida, digite novamente')
        
        os.system('Cls')
    
        if escolhaMenuDentista == 1:
            sessaoBuscada = c.buscarSessao()
            if sessaoBuscada != None:
                print(f'A sessão encontrada: Data: {sessaoBuscada['Data']} | Horario: {sessaoBuscada['Horario']} | Tempo da sessao: {sessaoBuscada['Tempo da Sessao']}')

            else:
                print('Nenhuma sessão encontrada.')

        
        elif escolhaMenuDentista == 2:
            sessaoAtiva = c.iniciarSessao()

            if sessaoAtiva == None:
                print('A sessão não pode ser iniciada pois não esta cadastrada no sistema.')

        # ADICIONE UM MÉTODO NA FUNÇÃO CLÍNICA QUE PERMITE A LEITURA DE TODOS OS PRONTUÁRIOS DO PACIENTE 

        elif escolhaMenuDentista == 3:
            Nome = d.atenderPaciente()
        
        elif escolhaMenuDentista == 4:
            if Nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                d.anotarProntuario(Nome)

        elif escolhaMenuDentista == 5:
            if Nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                d.primeiroProntuario(Nome)

        elif escolhaMenuDentista == 6:
            if Nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                d.ultimoProntuario(Nome)
        
        elif escolhaMenuDentista == 7:
            if sessaoAtiva == 0 or sessaoAtiva == None:
                print('nenhuma sessão iniciada. Não é possível inicar sessão')
            
            else:
                sessaoAtiva = c.encerrarSessao(sessaoAtiva)
        
        elif escolhaMenuDentista == 0:
            break
        
        else:
            print('Caracter inválido. Digite um aopção válida.')
    
    if seleçãoDeMenu == 0:
        break
