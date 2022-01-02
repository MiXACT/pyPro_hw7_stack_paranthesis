class Stack:
    def __init__(self, user_stack):
        self.user_stack = user_stack

    def isEmpty(self):
        if not self.user_stack:
            return True
        else:
            return False

    def push(self, item):
        self.user_stack.append(item)

    def pop(self):
        top_item = self.user_stack.pop()
        return top_item

    def peek(self):
        top_item = self.user_stack[len(self.user_stack)-1]
        return top_item

    def size(self):
        return len(self.user_stack)


if __name__ == '__main__':
    my_stack = []
    index = []
    input_s = input('Введите строку со скобками для проверки сбалансированности: ')
    opn_paranthesis = '({['
    cls_paranthesis = ')}]'
    result = 'Сбалансированно'
    opn_par_stack = Stack(my_stack)
    index_stack = Stack(index)

    if len(input_s) % 2 != 0:
        result = 'Несбалансированно'
    else:
        for i in input_s:
            if i in opn_paranthesis:
                opn_par_stack.push(i)
                index_stack.push(opn_paranthesis.find(i))
            else:
                if input_s.find(i) != 0 and cls_paranthesis.find(i) == index_stack.peek():
                    opn_par_stack.pop()
                    index_stack.pop()
                else:
                    result = 'Несбалансированно'
                    break
        if opn_par_stack.size() > 0:
            result = 'Несбалансированно'
    print(result)