# Validação de CPF - Python 3 

Essa solução facilita a validação de um ou vários CPFs, isso é útil para analisar uma base de clientes para identificar CPFs cadastrados de maneira equivocada ou para qualquer outra finalidade onde seja necessário saber se o CPF é válido ou não. 

Temos uma função chamada **ValidaCPF** dentro do módulo [**ferramentas**](ferramentas/__init__.py), para utilizar essa funcionalidade é necessário importar o módulo ````ferramentas```` no seu código principal, chamar a função ````ValidaCPF```` e passar como parâmetro uma string de números com 11 posições, lembre-se de adicionar os zeros à esquerda. 

A função retornará ````True```` para um CPF válido ou ````False````.

### Exemplo:

[Exemplo.py](Exemplo.py)

```python
#!/usr/bin/python3

from ferramentas import ValidaCPF

cpf = ValidaCPF('00000000191')

print(cpf)

# >>> True
```

Essa função pode ser utilizada para validações pontuais ou ser implementada em uma solução mais robusta para tratar bases com milhões de CPFs.

### Licença:
[Leia sobre a licença aplicada a esse Software.](LICENSE)

**Referências:**  <br/><font size="1">Macoratti.net, **Algoritmo de Validação do CPF.** Disponível em: <http://www.macoratti.net/alg_cpf.htm>. Acesso em: 01 nov. 2021.  <br/></font>
