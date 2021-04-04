def my_fun(string, braket, d):
    
    CORRECTION_FLAG = True
    BRAKET_WITH_MISTAKE = None
    BRAKET_WITHOUT_CLOSING = None

    answer = (CORRECTION_FLAG, BRAKET_WITH_MISTAKE, BRAKET_WITHOUT_CLOSING)
    string_dict = {}

    k = d.keys()
    new_dict = {}
    for i in range(len(braket)):
        for key in k:
            if braket[i] == key:
                new_dict.update({braket[i]: d.get(key)})
    
    stack = []
    rezult = []
    for i in range(len(string)):
        el = []
        el_rez = []
        for key in new_dict.keys():
            if string[i] == key:
                el.append(i)
                el.append(key)
                stack.append(el)
                rezult.append(el)
                break
            elif string[i] == new_dict.get(key) and stack[len(stack)-1][1] == key:
                el.append(i)
                el.append(new_dict.get(key))
                rezult.append(el)
                del stack[len(stack)-1]
                break
            elif ((string[i] == new_dict.get(key) and stack[len(stack)-1][1] != key)):
                el.append(i)
                el.append(new_dict.get(key))
                rezult.append(el)
                for i in range(len(rezult)):
                    for j in range(len(stack)):
                        if rezult[i] == stack[j]:
                            CORRECTION_FLAG = False
                            BRAKET_WITH_MISTAKE = (rezult[len(rezult)-1][1], rezult[len(rezult)-1][0])
                            BRAKET_WITHOUT_CLOSING = (rezult[len(rezult)-2][1], rezult[len(rezult)-2][0])
                            answer = (CORRECTION_FLAG, BRAKET_WITH_MISTAKE, BRAKET_WITHOUT_CLOSING)
                            return answer
    if len(stack) != 0:
        for i in range(len(rezult)):
            for j in range(len(stack)):
                if rezult[i] == stack[j] and rezult[i+1] != stack[j]:
                    CORRECTION_FLAG = False
                    BRAKET_WITH_MISTAKE = (rezult[i+1][1], rezult[i+1][0])
                    BRAKET_WITHOUT_CLOSING = (rezult[i][1], rezult[i][0])
                    answer = (CORRECTION_FLAG, BRAKET_WITH_MISTAKE, BRAKET_WITHOUT_CLOSING)
    return answer
    
if __name__=="__main__":
    string = list(input("Введите строку : "))
    braket = list(input("Введите проверочную скобку: "))
    for i in range(len(string)):
        for j in range(len(braket)):
            if string[i] == braket[j]:
                d = {"[": "]", "(": ")", "<": ">", "{": "}"}   
                answer = my_fun(string, braket, d)
                print(answer)
            else: 
                print("Попробуй ввести для поиска те скобки, которые действительно есть в строке")
        