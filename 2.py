fibo_list = [1,2]
even_sum = 0


for i in range(30):
    fibo_list.append(fibo_list[i] + fibo_list[i+1])
    if fibo_list[-1] >= 4000000:
        break
    
for number in fibo_list:
    if number % 2 == 0:
        even_sum += number
print(even_sum)