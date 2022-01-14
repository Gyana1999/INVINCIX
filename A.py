n=int(input("enter dictionary size"))

orders={}

for i in range(0,n):
    key=input("Name of District :")
    orders[key]=int(input("No. of Cases available:"))
sort_orders=sorted(orders.items(),key=lambda x:x[1],reverse=True)
for i in sort_orders:
    print(i[0],i[1])
