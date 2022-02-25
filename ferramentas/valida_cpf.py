# -*- coding: utf-8 -*-

__version__ = '1.0.0'


class Cpf:
    def valida_cpf(num: str) -> bool:
        if len(num) == 11:
            radical: list = list(num)[:-2]
            dv: list = list(num)[-2:]

            # Calculando DV 1
            try:
                num_cal: int = 10
                soma1: int = 0
                for x in radical:
                    soma1 = soma1 + (num_cal * int(x))
                    num_cal = num_cal - 1
                calc_dv_1: int = soma1 % 11
                if calc_dv_1 < 2:
                    dv_1: int = 0
                else:
                    dv_1 = 11 - calc_dv_1

                # Calculando DV 2
                try:
                    num_cal = 11
                    soma2: int = 0
                    radical.append(str(dv_1))
                    for x in radical:
                        soma2 = soma2 + (num_cal * int(x))
                        num_cal = num_cal - 1
                    calc_dv_2: int = soma2 % 11
                    if calc_dv_2 < 2:
                        dv_2: int = 0
                    else:
                        dv_2 = 11 - calc_dv_2

                    # Teste CPF válido?
                    try:
                        if ''.join(dv).strip() == str(dv_1)+str(dv_2).strip():
                            return True
                        else:
                            return False

                    except Exception:

                        return False

                except Exception:

                    return False

            except Exception:

                return False

        else:

            return False
