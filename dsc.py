#Arrange words in a string in the order of their length
def sort_length(string): 
    words = string.split() 
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)

string = input("Enter a sentence: ") 
result = sort_length(input_string) 
print(result)

#remove duplicates from an array 
def removedup(array):
    if not array:
        return []
    uniarray = [array[0]]
    for element in array[1:]:
        if element != uniarray[-1]:
            uniarray.append(element)
    return uniarray

array = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
result = removedupl(array)
print(result)

#design your own stack 
class ClubNode:
    def __init__(self, value, club):
        self.value = value
        self.club = club
        self.next = None

class ClubStack:
    def __init__(self):
        self.top = None

    def push(self, value, club):
        new_node = ClubNode(value, club)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} from {club} club!")

    def pop(self, count=1):
        if self.is_empty():
            print("The stack is empty. Cannot pop.")
            return None
        
        popped_values = []
        for _ in range(count):
            if self.is_empty():
                break
            popped_node = self.top
            self.top = self.top.next
            popped_values.append(f"{popped_node.value} from {popped_node.club} club!")
        
        for message in popped_values:
            print(f"Popped {message}")

    def peek(self):
        if self.is_empty():
            print("The stack is empty. Nothing to peek.")
            return None
        print(f"Top value: {self.top.value} | Club: {self.top.club}")
        return self.top.value

    def is_empty(self):
        return self.top is None


club_stack = ClubStack()
club_stack.push(1, "Synergy")
club_stack.push(2, "DSC")
club_stack.push(3, "Literary")
club_stack.peek()
club_stack.pop(2)  
club_stack.pop()   
club_stack.pop();  