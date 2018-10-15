import sys
from func import *


def main(args):
    # VERIFICA ENTRADA CORRETA
    if len(args) == 5:
        # RECEBE LISTA DO SEXP
        reading = reading_file(args[2])
        
        if (reading[0] == 'moore'):
            machine_in = moore_machine(reading)
            if(check_conditions(machine_in)):
                machine_out = moore_to_mealy(machine_in)
            else:
                print("#ERROR: Erro no arquivo de entrada")
                return 0
                
        elif (reading[0] == 'mealy'):
            machine_in = mealy_machine(reading)
            if(check_conditions(machine_in)):
                machine_out = mealy_to_moore(machine_in)
            else:
                print("#ERROR: Erro no arquivo de entrada")
                return 0
        else:
            print("ERROR: Erro na formatação do arquivo de entrada")
            return 0
        write_machine(machine_out,args[4])
    else:
        print("#ERRO: Entrada inválida. Consulte o documento Readme.md")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
