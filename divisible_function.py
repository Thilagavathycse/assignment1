def divisible(start=200,end=1500):
    for i in range(start,end+1):
        if i%75==0 and i%100==0:
            print(i)
divisible(start=200,end=1500)
