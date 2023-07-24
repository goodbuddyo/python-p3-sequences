#!/usr/bin/env python3


def print_fibonacci(index):
    if index == 0:
        print('[]')
        return []
    if index == 1:
        print('[0]')
        return [0]
    if index == 2:
        print('[0, 1]')
        return [0, 1]

    sequence = print_fibonacci(index - 1)

    sequence.append(sum(sequence[-2:]))
    print(list(sequence))
    return list(sequence)

#print(fib(11))

  #if n <= 0:
  #   return []
  #if n == 1:
  #   return [0]
  #result = [0, 1]
  #if n == 2:
  #   return result
  #for i in xrange(2, n):
  #   result.append(result[i-1] + result[i-2])
  #return result

  #if n <= 0:
  #  print('[]')
  #  return []
  #sequence = [0, 1]
  #while len(sequence) <= n:
  #  next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
  #  sequence.append(next_value)
  #print(sequence)

    #fibo_list = []]
    #a,b = 0,1
    #while b < n:
    #  fibo_list.append(a)
    #  print(fibo_list)
    #  a,b = b,a+b
       

#    num1 = 0
#    num2 = 1
#    next_number = 0
#    count = 1
#    fib_list = []
      
#    while(count <= length):
#      count += 1
#      num1 = num2
#      num2 = next_number
#      next_number = num1 + num2
#      t_number = num1 + num2
#      fib_list.append(next_number)

#    print(fib_list)

#    print_fibonacci(22)