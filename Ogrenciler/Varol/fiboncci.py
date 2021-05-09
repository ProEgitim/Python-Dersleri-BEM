# 1,1,
# 1,1,2
# 1,1,2,3
# 1,1,2,3,5

ilksayi=1
ikincisayi=1
fibo=[ilksayi,ikincisayi]

for i in range(0,20):
    ilksayi,ikincisayi=ikincisayi,ilksayi+ikincisayi
    fibo.append(ikincisayi)
print(fibo)