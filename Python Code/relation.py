import re

relation_dict = {
    1 : "right arrow",
    2 : "plus",
    3 : "parallel 1",
    4 : "parallel 2",
    5 : "parallel 3",
    6 : "parallel 4",
    7 : "parallel 5",
    8 : "parallel 6",
    9 : "inverse right arrow"
}


# relation pattern regular expression
class relation_pattern():
    # transition label map

    def __init__(self, tran1: str, tran2: str):
        self.label = list(map(chr, range(65, 91)))
        self.label.extend(list(map(chr, range(97, 123))))
        self.label.extend(list(map(str, range(10))))
        self.__tranmap = dict()
        self.__tranmap[tran1] = self.label.pop(0)
        self.__tranmap[tran2] = self.__tranmap[tran1] if tran1 == tran2 else self.label.pop(0)
        self.__x = self.__tranmap[tran1]
        self.__y = self.__tranmap[tran2]
    
    def get_pattern(self, relation: str, string: str):
        '''
            Return a tuple with two elements, like (A, B)
            if True:
                A : 1 or 0, means existing path from x->y or not existing
                B : 1 or 0, means existing path from y->x or not existing
            else:
                pass
        '''

        string = string.replace(', ',',')
        new_string = ''
        for tran in string.split(','):
            if tran in self.__tranmap:
                new_string += self.__tranmap[tran]
            else:
                self.__tranmap[tran] = self.label.pop(0)
                new_string += self.__tranmap[tran]

        if relation == "right arrow":
            # Pattern: x.*y , not y.*x
            x2y1 = self.__x + '.*' + self.__y
            y2x1 = self.__y + '.*' + self.__x
            x2y_judge1 = bool(re.search(x2y1,new_string))
            y2x_judge1 = bool(re.search(y2x1,new_string))
            if (self.__x != self.__y) and x2y_judge1 and (not y2x_judge1):
                return (int(x2y_judge1), int(y2x_judge1))
            else:
                return (0, 1)
        elif relation == "plus":
            # Pattern: not x.*y , not y.*x
            x2y2 = self.__x + '.*' + self.__y
            y2x2 = self.__y + '.*' + self.__x
            x2y_judge2 = bool(re.search(x2y2,new_string))
            y2x_judge2 = bool(re.search(y2x2,new_string))
            if (not x2y_judge2) and (not y2x_judge2):
                return (int(x2y_judge2), int(y2x_judge2))
            else:
                return (1, 1)            


        elif relation == "parallel 1":
            # Pattern: x!=y, x{1}[^xy]*y{1}, y{1}[^yx]*x{1}
            x2y3 = self.__x + '{1}' + '[^' + self.__x + self.__y + ']*' + self.__y + '{1}'
            y2x3 = self.__y + '{1}' + '[^' + self.__y + self.__x + ']*' + self.__x + '{1}'
            x2y_judge3 = bool(re.search(x2y3, new_string))
            y2x_judge3 = bool(re.search(y2x3, new_string))
            if (self.__x != self.__y) and (x2y_judge3 ^ y2x_judge3):
                return (int(x2y_judge3), int(y2x_judge3)) 
            else:
                return (0, 0)
        elif relation == "parallel 2":
            # Pattern: x!=y, x{1}.*[xy]+.*[xy]+.*y{1}, y{1}.*[xy]+.*[xy]+.*x{1}
            x2y4 = self.__x + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__y + '{1}'
            y2x4 = self.__y + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__x + '{1}'
            x2y_judge4 = bool(re.search(x2y4, new_string))
            y2x_judge4 = bool(re.search(y2x4, new_string))
            if (self.__x != self.__y) and (x2y_judge4 ^ y2x_judge4):
                return (int(x2y_judge4), int(y2x_judge4)) 
            else:
                return (0, 0)
        elif relation == "parallel 3":
            # Pattern: x!=y, x{1}[^y]*[x]+[^y]*y{1}, y{1}[^x]*[y]+[^x]*x{1}
            x2y5 = self.__x + '{1}[^' + self.__y + ']*[' + self.__x + ']+[^' + self.__y + ']*' + self.__y +'{1}'
            y2x5 = self.__y + '{1}[^' + self.__x + ']*[' + self.__y + ']+[^' + self.__x + ']*' + self.__x +'{1}'
            x2y_judge5 = bool(re.search(x2y5, new_string))
            y2x_judge5 = bool(re.search(y2x5, new_string))
            if (self.__x != self.__y) and (x2y_judge5 and y2x_judge5):
                return (int(x2y_judge5), int(y2x_judge5)) 
            else:
                return (0, 0)
        elif relation == "parallel 4":
            # Pattern: x!=y, x{1}.*[xy]+.*[xy]+.*y{1}, y{1}.*[xy]+.*[xy]+.*x{1}
            x2y6 = self.__x + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__y + '{1}'
            y2x6 = self.__y + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__x + '{1}'
            x2y_judge6 = bool(re.search(x2y6, new_string))
            y2x_judge6 = bool(re.search(y2x6, new_string))
            if (self.__x != self.__y) and (x2y_judge6 and y2x_judge6):
                return (int(x2y_judge6), int(y2x_judge6)) 
            else:
                return (0, 0)
        elif relation == "parallel 5":
            # Pattern: x=y, x.*y, y.*x
            # x2y7 = self.__x + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__y + '{1}'
            # y2x7 = self.__y + '{1}.*[' + self.__x + self.__y + ']+.*[' + self.__x + self.__y + ']+.*' + self.__x + '{1}'
            x2y7 = self.__x + '.*' + self.__y
            y2x7 = self.__y + '.*' + self.__x
            x2y_judge7 = bool(re.search(x2y7, new_string))
            y2x_judge7 = bool(re.search(y2x7, new_string))
            if (self.__x == self.__y) and x2y_judge7:
                return (int(x2y_judge7), int(y2x_judge7)) 
            else:
                return (0, 0)
        elif relation == "parallel 6":
            # Pattern: x=y, x{1}.*[xy]+.*[xy]+.*y{1}, y{1}.*[xy]+.*[xy]+.*x{1}
            x2y8 = self.__x + '.*' + self.__y
            y2x8 = self.__x + '.*' + self.__y
            x2y_judge8 = bool(re.search(x2y8, new_string))
            y2x_judge8 = bool(re.search(y2x8, new_string))
            if (self.__x == self.__y) and x2y_judge8:
                return (int(x2y_judge8), int(y2x_judge8)) 
            else:
                return (0, 0)
        elif relation == "inverse right arrow":
            # Pattern: not x.*y , y.*x
            x2y9 = self.__x + '.*' + self.__y
            y2x9 = self.__y + '.*' + self.__x
            x2y_judge9 = bool(re.search(x2y9,new_string))
            y2x_judge9 = bool(re.search(y2x9,new_string))
            if (self.__x != self.__y) and y2x_judge9 and (not x2y_judge9):
                return (int(x2y_judge9), int(y2x_judge9))
            else:
                return (1, 0)
        else:
            return "Wrong relation!"