def fibonacci(n):
    fib_seq = []
    a,b = 0,1
    
    while len(fib_seq) < n:
        fib_seq.append(a)
        a, b = b, a + b

    return fib_seq

num_termos = int(input("Digite o numero de termos que deseja ter na sequencia fibonacci: "))

if num_termos <=0:
    print("Informe um numero válido, maior que zero.")

else:
    resultado = fibonacci(num_termos)
    print(f"A sequencia fibonnaci ate o numero de termos {num_termos}: ")
    print(resultado)
