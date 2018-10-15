from sexp import *

# LEITURA DO ARQUIVO DE ENTRADA, RETORNA SEXP EM LISTA
def reading_file(nameFile):
    string_total = []
    stringF = []
    
    try:
        f = open(nameFile,'r')
        sexpList = parse_sexp(f.read())
    except:
        print("Falha ao abrir arquivo de leitura")
    finally:
        f.close()
    return sexpList

# FORMATANDO A LISTA QUE REPRESENTA A MAQUINA EM DICIONARIO
def moore_machine(sexpList): 
    '''
    dicionario moore_machine:
    
        type: ''
        symbols-in: []
        symbols-out: []
        states: []
        start: ''
        finals: []
        trans: [][]
        out-fn: [][]
    '''
    
    machine_in = {}
    machine_in['symbols-in'] = []
    machine_in['symbols-out'] = []
    machine_in['states'] = []
    machine_in['finals'] = []
    machine_in['trans'] = []
    machine_in['out-fn'] = []
    pos = 0

    for field in sexpList:
        if(field == 'moore'):
           machine_in['type'] = field

        elif(field[0] == 'symbols-in'):
            for data in field:
                if(data != 'symbols-in'):
                    machine_in['symbols-in'].append(data)

        elif(field[0] == 'symbols-out'):
            for data in field:
                if(data != 'symbols-out'):
                    machine_in['symbols-out'].append(data)
                                                    
        elif(field[0] == 'states'):
            for data in field:
                if(data != 'states'):
                    machine_in['states'].append(data)

        elif(field[0] == 'start'):
            machine_in['start'] = field[1]

        elif(field[0] == 'finals'):
            for data in field:
                if(data != 'finals'):
                    machine_in['finals'].append(data)
        
        elif(field[0] == 'trans'):
            for data in field:
                if(data != 'trans'):
                    machine_in['trans'].append(data)
                
        elif(field[0] == 'out-fn'):
            for data in field:
                if(data != 'out-fn'):
                    machine_in['out-fn'].append(data)
    return machine_in

# FORMATANDO A LISTA QUE REPRESENTA A MAQUINA EM DICIONARIO
def mealy_machine(sexpList):
    '''
    dicionario moore_machine:
    
        type: ''
        symbols-in: []
        symbols-out: []
        states: []
        start: ''
        finals: []
        trans: [][]
    '''
    
    machine_in = {}
    machine_in['symbols-in'] = []
    machine_in['symbols-out'] = []
    machine_in['states'] = []
    machine_in['finals'] = []
    machine_in['trans'] = []
    pos = 0

    for field in sexpList:
        if(field == 'mealy'):
           machine_in['type'] = field

        elif(field[0] == 'symbols-in'):
            for data in field:
                if(data != 'symbols-in'):
                    
                    machine_in['symbols-in'].append(data)

        elif(field[0] == 'symbols-out'):
            for data in field:
                if(data != 'symbols-out'):
                    # SEXP.PY TRAZ ESSES VALORES EM INT QUANDO NUMEROS, POR ISSO O CAST
                    machine_in['symbols-out'].append(str(data))
                                                    
        elif(field[0] == 'states'):
            for data in field:
                if(data != 'states'):
                    machine_in['states'].append(data)

        elif(field[0] == 'start'):
            machine_in['start'] = field[1]

        elif(field[0] == 'finals'):
            for data in field:
                if(data != 'finals'):
                    machine_in['finals'].append(data)

        elif(field[0] == 'trans'):
            for data in field:
                if(data != 'trans'):
                    # PARSE_SEXP DO SEXP.PY TRAZ ESSES VALORES EM INT QUANDO LIDO NUMEROS, POR ISSO O CAST
                    machine_in['trans'].append([data[0],data[1],data[2],str(data[3])])
    return machine_in 

# VERIFICACAO DA MAQUINA
def check_conditions(machine_in):
    test = 1
    if(machine_in['type'] != 'mealy' and machine_in['type']!= 'moore'):
        test = 0
    elif(len(machine_in['symbols-in']) == 0):
        test = 0
    elif(len(machine_in['symbols-out']) == 0):
        test = 0
    elif(len(machine_in['states']) == 0):
        test = 0
    elif(len(machine_in['start']) == 0):
        test = 0
    elif(len(machine_in['finals']) == 0):
        test = 0
    elif(len(machine_in['trans']) == 0):
        test = 0
    elif(machine_in['type'] == 'moore'):
        if(len(machine_in['out-fn']) == 0):
            test = 0
        #verificando se o estado inicial de moore é vazio, se nao for ele indica erro
        i = machine_in['start']
        for y in machine_in['out-fn']:
            if(i == y[0] and y[1] != []):
                 test = 0
            
    '''
    moore, verificar se o estado inicial tem o out com '()', se não começar o algoritmo não deveria rodar
    '''
    
    return test
    
#CONVERSAO DE MAQUINA DE MOORE PARA MEALY
def moore_to_mealy(machine_in):
    machine_out = {}
    machine_out['type'] = 'mealy'
    machine_out['symbols-in'] = machine_in['symbols-in']
    machine_out['symbols-out'] = machine_in['symbols-out']
    machine_out['start'] = machine_in['start']
    machine_out['states'] = []
    machine_out['finals'] = []
    machine_out['trans'] = []
    aux = []

    for field in machine_in['states']:
        if(field[:2] not in machine_out['states']): # verifica os 2 primeiros caracteres apenas, se ele existe ou não no estados
            machine_out['states'].append(field) # cria se não existe (apenas os 2 caracteres)

    for field in machine_in['finals']:
        if(field[:2] not in machine_out['finals']): # se o estado do final não estiver no finais (2 caractere) adiciona
            machine_out['finals'].append(field[:2])

    
    for trans_I in machine_in['trans']:
        for out_I in machine_in['out-fn']:
            for states in machine_out['states']:
                if(trans_I[1] == out_I[0]):# (q0,q1,a)
                    if(trans_I[0] == states): # verifica se ele é um estado original
                        machine_out['trans'].append([trans_I[0][:2],trans_I[1][:2],trans_I[2],out_I[1]])
                '''
                trans_I[0] = estado de origem (2 caractere)
                trans_I[1] = estado de destino (2 caractere)
                trans_I[2] = entrada
                out_I[1] = saida
                '''
        
    return machine_out

# CONVERSAO DE MAQUINA DE MEALY PARA MOORE
def mealy_to_moore(machine_in):
    machine_out = {}
    machine_out['type'] = 'moore'
    machine_out['symbols-in'] = machine_in['symbols-in']
    machine_out['symbols-out'] = machine_in['symbols-out']
    machine_out['start'] = machine_in['start']
    machine_out['states'] = []
    machine_out['finals'] = []
    machine_out['trans'] = []
    machine_out['out-fn'] = []

    aux = []

    for field in machine_in['states']: # jogar os estados no aux para trabalha-los
        aux.append([field])
    
    for field in aux:
        if(field[0] == machine_in['start']):
            field.append('()') # encontrou o inicial em aux e adiciona '()' nele
    
    for trans in machine_in['trans']:
        for state in aux: # aux é uma lista de estados
            if(trans[1] == state[0] and trans[3] not in state):
                state.append(trans[3]) # modificando campo do aux

    '''
    se for inicial precisa adicionar () no aux ai ficaria [q0,(),val1,val2] dps tratar-lo
    trans[1] = estado de saida
    state[0] = estado
    trans[3] = valor saida

    estado de saida = estado AND valor saida não está no estado (aux carrega [estado,valor,...]
    se nao tiver adiciona no aux o novo valor ficando aux[] = [estado,val1,val2,...]
    '''

    pos = 0
    for field in aux:
        if(len(aux[pos])== 1):
           aux[pos].append('()')
        elif(len(aux[pos]) > 2): # corrigindo o aux de ter o mesmo estado varios valores (precisa criar + estados)
            str_aux = ''
            for data in aux[pos]:
                if(data[:1] != 'q'): #se não for o primeiro campo (sempre começa com estado 'q')
                    aux[pos][0] += str_aux #incrementa o a string para diferenciar
                    aux.append([aux[pos][0],data]) #adiciona no aux no seguinte formato [estado,val]
                    str_aux += '`'
            del aux[pos] # deleta o aux utilizado (ja que ele não esta no formato devido) [estado,val1,val2,...]
            continue #pular o pos += 1
        pos += 1

    for field in aux: # adicionando todos os campos do aux no out-fn
        machine_out['out-fn'].append(field)
    

    for field in aux:
        machine_out['states'].append(field[0]) # o primeiro valor de cada campo aux são os estados

    for final_I in machine_in['finals']:
        for out_O in machine_out['out-fn']:
            if (final_I == out_O[0][:2]): # apenas verifica os 2 caracteres do estado out é final em mealy, se sim adiciona no final do moore (pode vir q2,q2`,etc)
                machine_out['finals'].append(out_O[0])

    for state_O in machine_out['states']:
        for trans_I in machine_in['trans']:
            for out_O in machine_out['out-fn']:
                if(state_O[:2] == trans_I[0][:2]): # ✓
                    if(trans_I[1] == out_O[0][:2] and trans_I[3] == out_O[1]):
                        machine_out['trans'].append([state_O,out_O[0],trans_I[2]])
                        '''
                        state_O = estado origem da transição
                        out_O[0] = estado destino da transição
                        trans_I[2] = entrada
                        '''
    return machine_out

# ESCRITA DA MAQUINA DE SAIDA
def write_machine(machine_out,nameFile):
    try:
        arquivo = open(nameFile,'w')
        arquivo.write('(')
        arquivo.write(machine_out['type'])
        arquivo.write('\n')
        arquivo.write(' (symbols-in')
        for i in machine_out['symbols-in']:
            arquivo.write(' ')
            arquivo.write(i)
        arquivo.write(')\n')
        arquivo.write(' (symbols-out')
        for i in machine_out['symbols-out']:
            arquivo.write(' ')
            arquivo.write(str(i))
        arquivo.write(')\n')
        arquivo.write(' (states')
        for i in machine_out['states']:
            arquivo.write(' ')
            arquivo.write(i)
        arquivo.write(')\n')
        arquivo.write(' (start ')
        arquivo.write(machine_out['start'])
        arquivo.write(')\n')
        arquivo.write(' (finals')
        for i in machine_out['finals']:
            arquivo.write(' ')
            arquivo.write(i)
        arquivo.write(')\n')
        arquivo.write(' (trans\n')
        arquivo.write(' ')
        cont = 0
        for i in machine_out['trans']:
            arquivo.write(' (')
            cont2 = 0
            for y in i:
                cont = cont+1
                if(cont2 > 0):
                    arquivo.write(' ')
                arquivo.write(str(y))
                cont2 = cont2+1
            arquivo.write(')')
            if(cont%4 == 0):
                arquivo.write('\n ')
        arquivo.write(')\n')
        if(machine_out['type'] == 'moore'):
            arquivo.write(' (out-fn\n')
            arquivo.write(' ')
            cont = 0
            for i in machine_out['out-fn']:
                arquivo.write(' (')
                cont2 = 0
                for y in i:
                    cont = cont+1
                    if(cont2 > 0):
                        arquivo.write(' ')
                    arquivo.write(str(y))
                    cont2 = cont2+1
                arquivo.write(')')
                if(cont%5 == 0):
                    arquivo.write('\n ')
            arquivo.write(')\n')
            arquivo.write(')')
    except: 
        print("#ERRO: Falha ao abrir o arquivo de escrita")
    finally:
        arquivo.close()
