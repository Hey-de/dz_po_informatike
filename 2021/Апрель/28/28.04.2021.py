def main(a):
    for el in a:
        if len(el) == 1 and int(el) == 5:
            print(el+" оканчивается на 5")
            continue
        for i in range(1, len(el)):
            if int(el) % 10 ** (len(el)-i) == 5:
                print(el+" оканчивается на 5")

if __name__ == "__main__":
    data = []
    while True:
        scan = input("Введите число: ")
        if scan == "0":
            break
        data.append(scan)
    main(data)
