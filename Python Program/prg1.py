from translate import Translator

trans = Translator(to_lang="ja")

try:
    with open('text.txt',mode='r') as my_file:
        text = my_file.read()
        result = trans.translate(text)
        with open('result.txt',mode='w') as my_file2:
            d = my_file2.write(result)  
            print(d)
            
except FileNotFoundError as error:
  	print(error)
except IOError as ioError:
    print(ioError)


print()