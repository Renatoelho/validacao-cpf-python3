#!/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = '1.0.0'


def ValidaCPF(numcpf):

    if len(num) == 11:
        radical = list(num)[:-2]
        dv = list(num)[-2:]

        # Calculando DV 1

        try:
            num_cal = 10
            soma1 = 0
            for x in radical:
                soma1 = soma1 + (num_cal * int(x))
                num_cal = num_cal - 1
            calc_dv_1 = soma1 % 11
            if calc_dv_1 < 2:
                dv_1 = 0
            else:
                dv_1 = 11 - calc_dv_1

            #print(soma1, dv_1)

            # Calculando DV 2
            
            try:
                num_cal = 11
                soma2 = 0
                radical.append(str(dv_1))
                for x in radical:
                    soma2 = soma2 + (num_cal * int(x))
                    num_cal = num_cal - 1
                calc_dv_2 = soma2 % 11
                if calc_dv_2 < 2:
                    dv_2 = 0
                else:
                    dv_2 = 11 - calc_dv_2

                #print(soma2, dv_2)

                # Teste CPF v�lido?
                
                try:
                    if ''.join(dv).strip() == str(dv_1)+str(dv_2).strip():
                        return True
                    else:
                        return False

                except Exception as erro:
                    # print('Ocorreu o seguinte erro na compara��o dos DVs: {}'.format(erro))
                    return False

            except Exception as erro:
                # print('Ocorreu o seguinte erro no c�lculo do DV 2: {}'.format(erro))
                return False

        except Exception as erro:
            # print('Ocorreu o seguinte erro no c�lculo do DV 1: {}'.format(erro))
            return False

    else:
        # print('CPF fora da formata��o correta. Ex.: 00000000191 (11 caracteres)')
        return False
