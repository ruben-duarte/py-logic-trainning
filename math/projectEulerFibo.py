print("Fibonacci problem")
number = int(input("Enter a number: "))

def sum_fibo_even_numbers(number):
  fibo_numbers = [1,2]
  for indice in range(number-2):
    new_fibo = fibo_numbers[indice] + fibo_numbers[indice+1]
    fibo_numbers.append(new_fibo)
  fibo_even = [ ]
  sum = 0
  for index in fibo_numbers:
       if index % 2 == 0 and index<4000000:
         fibo_even.append(index)
         sum += index
  print(fibo_numbers)       
  print(fibo_even, sum)
  return fibo_even,fibo_numbers, sum

sum_fibo_even_numbers(number)

 
    