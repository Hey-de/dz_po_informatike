from colorama import init, Fore, Back, Style
def do(a, b):
    if (b < 2) or (b > 9):
        print(Fore.RED+Back.BLACK+"FATAL ERROR: UNCORRECT DATATYPE")
        return
    if a == 0:
        return
    do(a // b, b)
    print(Fore.BLUE+Back.WHITE+str(a % b), end="")

    return
def main():
    print("Нажми Ctrl+C для выхода")
    try:
        a = int(input(Fore.BLACK+Back.WHITE+"Введите число: "))
        b = int(input(Fore.BLACK+Back.WHITE+"Введите основание системы счисления от 2 до 9: "))
        do(a, b)
    except ValueError:
        print(Fore.RED+Back.BLACK+"FATAL ERROR: UNCORRECT DATATYPE")
    except KeyboardInterrupt:
        print()
        print("Программа завершена")
        return
    finally:
        print()
    main()
if __name__ == '__main__':
    init(autoreset=True)
    main()
