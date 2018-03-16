# Isto é um comentário. Ao executar o codigo, nada aqui será imprimido na tela do computador.

print('O comando print é uma função. Deve ser acompanhada de parenteses e serve para exibir uma mensagem de texto quando necessário.')

print('A seguir, as variáveis a e b recebem os valores 2 e 4.2, respectivamente.')

a = 2
b = 4.2

print('Podemos usar o comando print para exibir os valores contidos em variáveis. Nesta caso: a = %.5f e b = %.5f' % (a, b))

print('Vamos agora iniciar algumas operações aritméticas: +, -, x, /')

print('Soma          : a + b = %.5f' % (a + b))
print('Subtração     : a - b = %.5f' % (a - b))
print('Multiplicação : a * b = %.5f' % (a * b))
print('Divisão       : a / b = %.5f' % (a / b))

print('Vamos criar 4 novas variáveis para guardar os valores das operações efetuadas:\n c = a + b\n d = a - b\n e = a * b\n f = a \b')

c = a + b
d = a - b
e = a * b
f = a / b

print('c = %.5f d = %.5f e = %.5f f = %.5f' % (c,d,e,f))

print('Se for necessário armazenar muitos valores, precisamos de algo mais eficaz. Para isso, fazemos uso dos vetores (arrays)')

print('Mas antes precisamos informar ao Python que precisamos de uma biblioteca específica para isso chamada numpy')

import numpy as np

print('import numpy as np siginifica que queremos importar a biblioteca numpy e criamos um OBJETO chamado np. Este OBJETO serva para acessar as funcionalidades de numpy.')

# tamanho do array
n = 10

vetor = np.zeros(n)

vetor[0] = a
vetor[1] = b
vetor[2] = c
vetor[3] = d
vetor[4] = e
vetor[5] = f
vetor[6] = -1
vetor[7] = -1
vetor[8] = -1
vetor[9] = -1

print('Vamos usar o comando range para acessar de forma automática TODOS os valores do vetor')

for i in range(n):
    print('vetor[%d] = %.5f' % (i,vetor[i]))

print('Vamos usar o comando condicional if')

for i in range(n):
    if vetor[i] > 0:
        print('%.5f é positivo' % (vetor[i]))
    else:
        print('%.5f é negativo' % (vetor[i]))

print('A máquina pode nos enganar ao realizar operações aritméticas:')

s = 0
for i in range(1000):
    s = s + 0.1

print('Soma: %.15E não corresponde ao valor esperado (100) porque 0.1 não tem representação exata na forma binária.\n' % (s))

a = 1e16
b = 3
print('1e16 + 3 = %.18e, mas o resultado deveria ser 1.0000000000000003e+16!' % (a+b))

print('0.1/0.01 = %.15e e 0.1*0.01 = %.15e\n\n' % (0.1/0.01, 0.1*0.01))

a = 7604736536
b = 7604736535
er1 = np.sqrt(a) - np.sqrt(b)
er2 = (a - b)/(np.sqrt(a) + np.sqrt(b))
print('Erro de cancelamento: sqrt(%d) - sqrt(%d) = %.15f mas deveria ser: %.15f' % (a,b,er1, er2))
print('Quando escrevemos na forma cientifica, temos: %.15e e %.15e' % (er1,er2))

s = 0
for k in range(1, 101, 1):
    s = s + 2/(k*k)
    #print('k = %d' % (k))

print('s = %.15e' % (s))

s = 0
for k in range(100, 0, -1):
    s = s + 2/(k*k)
   # print('k = %d' % (k))

print('s = %.15e' % (s))


s1 = 0
for i in range(10):
    s = 0
    for k in range(1, 101, 1):
        s = s + 2/(k*k)
    s1 = s1 + s

print('s = %.15e' % (s1))

s1 = 0
for i in range(10):
    s = 0
    for k in range(100, 0, -1):
        s = s + 2/(k*k)
    s1 = s1 + s

print('s = %.15e' % (s1))

