import time


def Secuencial(list, target):

    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def Binaria(list, target):
    start=0
    end= len(list) -1

    while start <= end:
        poi= (start + end)//2

        if list[poi] == target:
            return poi
        elif list[poi] < target:
            start = poi + 1
        else:
            end = poi-1

    return -1

if __name__ == "__main__":
    
    list =[1,3,9,8,9,0]
    trg = 3

    t1sec = time.perf_counter()
    sec_result = Secuencial(list, trg)
    t2sec = time.perf_counter()
    print(f"Tiempo Secuencial :{t1sec-t2sec:.10f}segundos")

    print(f"El objetivo a encontrar es: {trg}")

    if sec_result != -1:
        print(f"Secuencial encontrado, {sec_result}")
    else:
        print("target miss")

    t1bin = time.perf_counter()
    bin_result = Binaria(list, trg)
    t2bin = time.perf_counter()
    print(f"Tiempo Secuencial :{t1bin-t2bin:.10f}segundos")

    if bin_result != -1:
        print(f"Binario encontrado {bin_result}")
    else:
        print("target miss")
