class Bin_Heap:
    '''
    chidren at indeces 2 * i and 2 * i + 1
    their parents at indeces floor(i / 2)
    heap_list[0] - wasted element
    '''
    def __init__(self):
        self.heap_size = 0
        self.heap_list = [0]

    def perc_up(self, k):
        while k // 2 > 0:
            if self.heap_list[k] < self.heap_list[k // 2]:
                self.heap_list[k], self.heap_list[k // 2] =\
                    self.heap_list[k // 2], self.heap_list[k]
            else:
                break
            k //= 2

    def perc_down(self, k):
        while k * 2 <= self.heap_size:
            tmp = self.min_child(k)
            if self.heap_list[k] > self.heap_list[tmp]:
                self.heap_list[k], self.heap_list[tmp] =\
                    self.heap_list[tmp], self.heap_list[k]
            else:
                break
            k = tmp

    def min_child(self, k):
        if 2 * k + 1 > self.heap_size:
            return 2 * k
        elif self.heap_list[2 * k] > self.heap_list[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def insert(self, k):
        self.heap_list.append(k)
        self.heap_size += 1
        self.perc_up(self.heap_size)

    def extract_min(self):
        '''
        weird logic, but it works
        '''
        extracted = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_list.pop()
        self.heap_size -= 1
        self.perc_down(1)
        return extracted

    def heap_construct(self, array):
        self.heap_size += len(array)
        self.heap_list = self.heap_list + array[:]
        k = len(array) // 2
        while k > 0:
            self.perc_down(k)
            k -= 1

def main():
    array = [24, 2, 9, 7, 4]
    test = Bin_Heap()
    test.heap_construct(array)
    test.insert(int(input()))
    print(test.extract_min())
    print(test.extract_min())
    print(test.extract_min())
    print(test.extract_min())
    print(test.extract_min())
    print(test.extract_min())

if __name__ == '__main__':
    main()
