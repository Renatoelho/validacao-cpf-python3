#!/usr/bin/python3

from ferramentas.valida_cpf import Cpf

CPF: bool = Cpf.valida_cpf('00000000191')

print(CPF)
