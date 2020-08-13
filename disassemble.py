import dis


def test(number):
    return str(number) + str(number)


def test2(string):
    print("Hello", string)


# this will display the disassembly of test()
dis.dis(test)

dis.dis(test2)
