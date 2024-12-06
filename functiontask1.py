a = int(input("birinci ededi daxil ein:"))
b = int(input("ikinci ededi daxil ein:"))
c = int(input("ucuncu ededi daxil ein:"))
def test_function(*args):
    return args
qiymetler = max(test_function(a, b, c))
print("en boyuk eded: ", qiymetler)