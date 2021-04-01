def my_fun(string, scob, d):
    k = d.keys()
    new_dict = {}
    for i in range(len(scob)):
        for key in k:
            if scob[i] == key:
                new_dict.update({scob[i]: d.get(key)})
    marker = []
    ke = new_dict.keys()
    mark = []
    rezult = {}
    for i in range(len(string)):
        for key in ke:
            if string[i] == key:
                rez = []
                rezult.update({i: key})
                rez.append(i)
                for j in range(i, len(string)):
                    if string[j] == new_dict.get(key):
                        rezult.update({j: new_dict.get(key)})
                        rez.append(j)
                        break
                mark.append(rez)
    if len(mark) == 1:
        answer = (True, None, None)
    elif len(mark) == 0:
        answer  = "Скобка в последовательности не найдена..."
    else:   
        i = 0    
        while i!= len(mark)-1:
            if (mark[i][0] < mark[i+1][0] and mark[i][1] < mark[i+1][1] and mark[i][1] < mark[i+1][0]) or (mark[i][0] < mark[i+1][0] and mark[i][1] > mark[i+1][1]):
                answer = (True, None, None)
            elif mark[i][1] > mark[i+1][0] and mark[i][1] < mark[i+1][1]:
                k = rezult.keys()
                for key in k:
                    if key == mark[i][1]:
                        secvalue = (rezult.get(key), key)
                    elif key == mark[i+1][0]:
                        thivalue = (rezult.get(key), key)
                answer = (False, secvalue, thivalue)
            i+=1
    return answer

if __name__=="__main__":
    string = list(input("Введите строку: "))
    scob = list(input("Введите проверочную скобку: "))
    d = {"[": "]", "(": ")", "<": ">", "{": "}"}   
    answer = my_fun(string, scob, d)
    print(answer)