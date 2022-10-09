class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.front == None and self.rear == None
    
    def enqueue(self, item): # O(1)
        # overflow 상태가 존재하지 않음
        if not self.isEmpty(): # 공백 상태가 아닐 땐 rear만 옮겨주면 됨 
            new_node = Node(item) # 원형 큐가 아니기 때문에 rear에 삽입될 새 노드의 링크는 None임(new_node.link = None)
            self.rear.link = new_node # None에서 새 노드로 링킹
            self.rear = new_node # 이후 rear포인터를 새 노드로 옮겨 줌
        else: # 공백 상태일 땐 front = rear = new_node 임
            new_node = Node(item)
            self.front = new_node
            self.rear = new_node
    
    def dequeue(self):
        # underflow 고민안해도 됨. isEmpty()일 땐 그냥 self.front = None으로 두는게 맞음
        # 대신 큐가 한 개의 항목만 가지고 있을 땐 front와 rear값이 동일한 항목을 가리키고 있기 때문에 분리해서 처리해야 함
        if not self.isEmpty(): 
            data = self.front.data # 큐 전단 데이터 저장
            if self.front == self.rear: # 큐 항목이 1개일 경우
                self.front = None
                self.rear = None
            else: # 큐 항목이 여러 개일 경우
                self.front = self.front.link
            return data

    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else: return None

    def display(self, msg='LinkedQueue:'):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()

    def clear(self): 
        self.front = None
        self.rear = None

def testLinkedQueue():
    print('연결된 구조의 큐 구현\n')
    queue = LinkedQueue()
    for i in range(10):
        queue.enqueue(i)
    queue.display('큐 enqueue 9회:')
    print(f'\tdequeue() --> {queue.dequeue()}')
    print(f'\tdequeue() --> {queue.dequeue()}')
    print(f'\tdequeue() --> {queue.dequeue()}')
    queue.display('큐 dequeue 3회:')

    queue.enqueue('수퍼맨')
    queue.enqueue('배트맨')
    queue.enqueue('원더우먼')
    queue.enqueue('아쿠아맨')
    queue.display('큐 enqueue 4회:')
    print(f'\tdequeue() --> {queue.dequeue()}')
    queue.display('큐 dequeue 1회:')
    print(f'\tpeek() --> {queue.peek()}')

testLinkedQueue()