Operation = ['*', '-', '/', '=', '>', '<', '>=', '==', '<=', '%', '+', '+=', '-=', '*=', '/=']  # 运算符
Delimiter = ['(', ')', ',', ';', '.', '{', '}', '<', '>', '"', '<<', '>>']  # 分界符
KeyWord = ['bool', 'char', 'class', 'double', 'false', 'float', 'getchar', 'include', 'int', 'long', 'main',
           'null', 'open', 'printf', 'private', 'public', 'put', 'read', 'return', 'short', 'scanf', 'signed',
           'static', 'stdio', 'string', 'struct', 'true', 'unsigned', 'void', 'cout', 'cin']   #关键字
LeftNoteFlag = 0  # /*注释清除标记
RightNoteFlag = 0  # */注释清除标记


class Complier():  # 封装成编译器
    str = ""
    #判断单个字符是否为字母
    def IsLetter(self, Char):
        if ((Char >= 'a' and Char <= 'z') or (Char >= 'A' and Char <= 'Z')):
            return True
        else:
            return False

    #判断单个字符是否为数字
    def IsDigit(self, Char):
        if (Char <= '9' and Char >= '0'):
            return True
        else:
            return False

    #判断单个字符是否为空格
    def IsSpace(self, Char):
        if (Char == ' '):
            return True
        else:
            return False

    # 清除字符串中前后的空格
    def RemoveSpace(self, List):
        indexInList = 0
        for String in List:
            List[indexInList] = String.strip()
            indexInList += 1
        return List

    # 判断注释类型
    def IsNote(self, String):
        global LeftNoteFlag
        global RightNoteFlag
        index = 0
        for Char in String:
            if (index < len(String)):
                index += 1
            if (Char == '/'):
                if (String[index] == '/'):
                    return 2
                elif (String[index] == '*'):
                    if (LeftNoteFlag == 0):
                        LeftNoteFlag += 1
                    return 1
            elif (Char == '*'):
                if (String[index] == '/'):
                    if (RightNoteFlag == 0):
                        RightNoteFlag += 1
                    return 3
            if (len(String) == index + 1):
                return False
    def isHeadFile(self, String):
        if ('<' in String) and ('>' in String):
            return True
        else:
            return False

    def isStr(self, String):
        if ('"' in String) and ('"' in String):
            return True
        else:
            return False

    # 删除列表中的单行注释（//）或者多行注释（/*   */）
    def DeleteNote(self, List):
        RemoveList = []
        LeftNoteNum1 = 0
        indexInList = 0
        LeftNoteNumber = 0
        global LeftNoteFlag
        global RightNoteFlag
        for String in List:
            Flag = self.IsNote(String)
            index = 0
            LeftNoteNum1 = 0
            if (Flag):
                for Char in String:
                    if (index < len(String) - 1):
                        index += 1
                    if (Flag == 1):
                        if (Char == '/' and String[index] == '*'):
                            if (index != 1):
                                LeftNoteNum1 = index - 2
                            else:
                                LeftNoteNumber = index - 1
                            if (LeftNoteNum1 == 0):
                                LeftNoteNum1 = LeftNoteNumber
                                LeftNoteFlag = 1
                            else:
                                pass
                        if (Char == '*' and String[index] == '/'):
                            if (index != len(String) - 1):
                                String = String[0:LeftNoteNum1] + String[index + 1:]
                            else:
                                String = String[0:LeftNoteNum1]
                            LeftNoteFlag = 0
                            break
                        if (index + 1 == len(String) and RightNoteFlag == 0 and LeftNoteFlag == 1):
                            if (LeftNoteNum1 == 0):
                                RemoveList.append(String)
                            else:
                                String = String[0:LeftNoteNum1]
                            break
                    elif (Flag == 2):
                        if (Char == '/' and String[index] == '/'):
                            String = String[0:index - 1]
                            break
                    elif (Flag == 3):
                        if (Char == '*' and String[index] == '/'):
                            if (LeftNoteFlag != 0 and index != len(String) - 1):
                                String = String[index:]
                            elif (LeftNoteFlag == 0 and index != len(String)):
                                String = String[0:index - 1] + String[index + 1:]
                            elif (LeftNoteFlag != 0 and index + 1 == len(String)):
                                RemoveList.append(String)
                            RightNoteFlag = 0
                            LeftNoteFlag = 0
                            break
            else:
                if (LeftNoteFlag != 0 and RightNoteFlag == 0):
                    RemoveList.append(String)
                elif (LeftNoteFlag != 0 and RightNoteFlag != 0):
                    LeftNoteFlag = 0
                    RightNoteFlag = 0
                else:
                    pass
            List[indexInList] = String
            if (indexInList < len(List) - 1):
                indexInList += 1
        for ListString in RemoveList:
            List.remove(ListString)
        return List

    def Reader(self, List):
        count = 0
        ResultList = []
        for String in List:
            Letter = ''
            Digit = ''
            letter = ''
            index = 0
            for Char in String:
                if (index < len(String) - 1):
                    index += 1
                if (Char == '"'):
                    letter += Char
                    if (count == 0):
                        count += 1
                        Letter += Char
                    else:
                        count = 0
                        Letter += Char
                        ResultList.append(Letter)
                        Letter = ''
                elif (self.IsLetter(Char) or count == 1):
                    if (self.IsLetter(String[index]) or self.IsDigit(String[index]) or count == 1):
                        Letter += Char
                    elif (self.IsSpace(String[index]) or (String[index] in Delimiter) or (
                            String[index] in Operation) or (String[index:index + 2] in Operation)):
                        Letter += Char
                        ResultList.append(Letter)
                        Letter = ''
                else:
                    if (self.IsDigit(Char) and count == 0):
                        if (self.IsLetter(String[index]) or self.IsDigit(String[index])):
                            Digit += Char
                        elif (self.IsSpace(String[index]) or (String[index] in Delimiter) or (
                                String[index] in Operation) or (String[index:index + 2] in Operation)):
                            Digit += Char
                            ResultList.append(Digit)
                            Digit = ''
                    else:
                        if (Char == '#'):
                            ResultList.append('#')
                        else:
                            if (Char in Delimiter):
                                ResultList.append(Char)
                            else:
                                if (Char in Operation):
                                    letter += Char
                                    if (String[index] in Operation):
                                        letter += String[index]
                                        ResultList.append(letter)
                                        letter = ''
                                    else:
                                        ResultList.append(letter)
                                        letter = ''
                                else:
                                    if (self.IsSpace(Char)):
                                        pass
        return ResultList

    def combine_head(self, List):
        index = 0
        while(index < len(List) - 1):
            if List[index] == "include":
                if List[index + 3] == ".":
                    List[index + 1] = List[index + 1].__add__(List[index + 2]).__add__(List[index + 3]).__add__(List[index + 4]).__add__(List[index + 5])
                    del List[index + 2]
                    del List[index + 2]
                    del List[index + 2]
                    del List[index + 2]
                else:
                    List[index + 1] = List[index + 1].join(List[index + 2]).join(List[index + 3])
                    del List[index + 2]
                    del List[index + 2]
            elif (List[index] == '<' and List[index + 1] =='<') or (List[index] == '>' and List[index + 1] =='>'):
                List[index] = List[index].__add__(List[index + 1])
                del List[index + 1]
            index += 1
        return List

    def JugeMent(self, List):
        FormatFlag = 0
        indexInList = 0
        for String in List:
            if (indexInList < len(String) - 1):
                indexInList += 1
            if (len(String) == 1):
                if (String == '#'):
                    print('#   特殊符号')
                    self.str = self.str + '#   特殊符号\n'
                elif (String in Delimiter):
                    '''
                    if (String == '<'):
                        if (List[indexInList] in KeyWord):
                            print('<   特殊符号')
                            self.str = self.str + '<   特殊符号\n'
                    elif (String == '>'):
                        if (List[indexInList - 3] in Delimiter or List[indexInList - 4] in KeyWord):
                            print('>   特殊符号')
                            self.str = self.str + '>   特殊符号\n'
                    else:
                    '''
                    print(String + '   特殊符号')
                    self.str = self.str + String + '   特殊符号\n'
                elif (String in Operation):
                    if (String == '%'):
                        if (not (List[indexInList].isdigit())):
                            print('%   特殊符号')
                            self.str = self.str + '%   特殊符号\n'
                            FormatFlag = 1
                            continue
                    print(String + '   运算符')
                    self.str = self.str + String + '   运算符\n'
                else:
                    if (String.isdigit()):
                        print(String + '   数字')
                        self.str = self.str + String + '   数字\n'
                    elif (String.isalnum()):
                        if (FormatFlag == 0):
                            print(String + '   标识符')
                            self.str = self.str + String + '   标识符\n'
                        else:
                            print(String + '   格式变量')
                            self.str = self.str + String + '   格式变量\n'
                            FormatFlag = 0
            else:
                if (String in KeyWord):
                    print(String + '   关键字')
                    self.str = self.str + String + '   关键字\n'
                elif (String in Delimiter):
                    print(String + '   特殊符号')
                    self.str = self.str + String + '   特殊符号\n'
                elif (String in Operation):
                    print(String + '   运算符')
                    self.str = self.str + String + '   运算符\n'
                elif (self.isHeadFile(String)):
                    print(String + '   特殊符号')
                    self.str = self.str + String + '   特殊符号\n'
                elif(self.isStr(String)):
                    print(String + '   串')
                    self.str = self.str + String + '   串\n'
                else:
                    if (String.isdigit()):
                        print(String + '   数字')
                        self.str = self.str + String + '   数字\n'
                    elif (String.isalnum()):
                        if (FormatFlag == 0):
                            print(String + '   标识符')
                            self.str = self.str + String + '   标识符\n'
                        else:
                            print(String + '   格式变量')
                            self.str = self.str + String + '   格式变量\n'
                            FormatFlag = 0


def main():
    ComPlier = Complier()
    SourceProgram = []
    #Filepath = input("请输入文件路径：")
    Filepath = input("请输入文件路径：")
    for line in open(Filepath, 'r', encoding='UTF-8-sig'):
        line = line.replace('\n', '')
        SourceProgram.append(line)
    SourceProgram = ComPlier.DeleteNote(SourceProgram)
    SourceProgram = ComPlier.RemoveSpace(SourceProgram)
    #print(SourceProgram)
    SourceProgram = ComPlier.Reader(SourceProgram)
    #print(SourceProgram)
    SourceProgram = ComPlier.combine_head(SourceProgram)
    #print(SourceProgram)
    ComPlier.JugeMent(SourceProgram)


if __name__ == "__main__":
    main()
