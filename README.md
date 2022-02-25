# Validação de CPF - Python 3 

Essa solução facilita a validação de um ou vários CPFs. Isso é útil para analisar uma base de clientes, para identificar CPFs cadastrados de maneira equivocada ou para qualquer outra finalidade onde seja necessário saber se o CPF é válido ou não. 

Temos um método chamado **valida_cpf**, dentro da classe **Cpf**. Para utilizar essa funcionalidade é necessário importar o módulo ````ferramentas```` no seu código principal, chamar o método ````valida_cpf```` e passar como parâmetro uma string de números com 11 posições. Lembre-se de adicionar os zeros à esquerda. 


A função retornará ````True```` para um CPF válido ou ````False```` (para um CPF inválido).

### Exemplo:

[exemplo_cpf.py](exemplo_cpf.py)

```python
#/usr/bin/python3

from ferramentas.valida_cpf import Cpf

CPF: bool = Cpf.valida_cpf('00000000191')

print(CPF)

# >>> True 
```

Essa função pode ser utilizada para validações pontuais ou ser implementada em uma solução mais robusta, para tratar bases com milhões de CPFs.

### Licença:
[Leia sobre a licença aplicada a esse Software.](LICENSE)

**Referências:**  <br/><font size="1">Macoratti.net, **Algoritmo de Validação do CPF.** Disponível em: <http://www.macoratti.net/alg_cpf.htm>. Acesso em: 01 nov. 2021.  <br/></font>
