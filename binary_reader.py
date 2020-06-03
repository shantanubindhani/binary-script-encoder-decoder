from time import sleep as delay


def encode(data, bits=8):
    """
    data : required a data of char sequence or as can be called string.
            e.g. Any fucking text!.
    bits : max number of bits allowed , 
            default : 8
    """
    binary = ""
    bvalue = ord(str(data))
    b_list = [2**val for val in range(bits)][::-1]

    for n in b_list:
        if (n <= bvalue):
            binary += "1"
            bvalue -= n
        else:
            binary += "0"
    while binary[0] == "0":
        binary = binary[1:]
    return binary


def decode(data, bits=8):
    """
    data : required a data of binary sequence
            e.g. 10, 1010, 110110, 00000001 etc.
    bits : max number of bits allowed , 
            default : 8
    """
    data = list(data)
    b_list = [2**val for val in range(bits)][::-1]
    value = 0
    l = len(data)

    for i in range(bits-l):
        data.insert(0, 0)
    for i in range(8):
        value += int(data[i])*b_list[i]
    return chr(value)


def call_encode():
    data = "Enter the text : "
    data = input(data)

    if " " in data:
        data = data.split(" ")
    else:
        data = [data, ]

    text = ""

    for x in data:
        for char in x:
            binary = encode(char)
            text += binary
            text += " "
        text = text[:len(text)-1]
        text += "/"

    text = text[:len(text)-1]

    print("\n"+"="*80)
    print("The encoded text is :")
    print("[ "+text+" ]")
    print("="*80)


def call_decode():
    try:
        data = "Enter the binary text : "
        data = input(data)

        if data.isalpha():
            raise ValueError
        for i in range(2, 10):
            if str(i) in data:
                raise ValueError

        if "/" in data:
            data = data.split("/")
        else:
            data = [data, ]

        text = ""

        for x in data:
            if " " in x:
                x = x.split(" ")
            else:
                x = [x, ]

            for char in x:
                char = decode(char)
                text += char
            text += " "

        text = text[:len(text)-1]

        print("\n"+"="*80)
        print("The decoded text is :")
        print("[ "+text+" ]")
        print("\n"+"="*80)
    except:
        print("\n please enter only binary digits.")


def main():
    try:
        choice = """
        Please enter your choice :
            1.Encode the text to binary
            2.Decode the binary script
            
            --> """
        try:
            choice = int(input(choice))
            if choice != 1 and choice != 2:
                print("enter a valid choice!, rn again.")
                delay(2)
                exit()
        except ValueError:
            print("enter a valid choice!, run again.")
            delay(2)
            exit()

        if (choice == 1):
            call_encode()
        else:
            call_decode()

        termi = input("press enter.")
        del termi
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
