def convert(nptStr):
 xStr = nptStr.replace(':)', '🙂').replace(':(', '🙁')
 return xStr
def main():
 usrNpt = input('')
 walrus = convert(usrNpt)
 print('', walrus)
print = main()
