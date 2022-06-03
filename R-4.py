#Represent a node of the singly linked list  
class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class SwapNodes:  
    #Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    #addNode() will add a new node to the list  
    def addNode(self, data):  
        #Create a new node  
        newNode = Node(data);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            #newNode will become new tail of the list  
            self.tail = newNode;  
              
    #swap() will swap the given two nodes  
    def swap(self, n1, n2):  
        prevNode1 = None;  
        prevNode2 = None;  
        node1 = self.head;  
        node2 = self.head;  
          
        #Checks if list is empty  
        if(self.head == None):  
            return;  
              
        #If n1 and n2 are equal, then list will remain the same  
        if(n1 == n2):  
            return;  
              
        #Search for node1  
        while(node1 != None and node1.data != n1):  
            prevNode1 = node1;  
            node1 = node1.next;  
              
        #Search for node2  
        while(node2 != None and node2.data != n2):  
            prevNode2 = node2;  
            node2 = node2.next;  
              
        if(node1 != None and node2 != None):  
              
            #If previous node to node1 is not None then, it will point to node2  
            if(prevNode1 != None):  
                prevNode1.next = node2;  
            else:  
                self.head  = node2;  
                  
            #If previous node to node2 is not None then, it will point to node1  
            if(prevNode2 != None):  
                prevNode2.next = node1;  
            else:  
                self.head  = node1;  
                  
            #Swaps the next nodes of node1 and node2  
            temp = node1.next;   
            node1.next = node2.next;   
            node2.next = temp;  
        else:  
            print("Swapping is not possible");  
              
    #display() will display all the nodes present in the list  
    def display(self):  
        #Node current will point to head  
        current = self.head;  
          
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data),  
            current = current.next;  
         
   
sList = SwapNodes();  
   
#Add nodes to the list  
sList.addNode(13);  
sList.addNode(14);  
sList.addNode(15);  
sList.addNode(16);  
sList.addNode(17);  
   
print("Original list: ");  
sList.display();  
   
   
#Swaps the node 14 with node 17 
sList.swap(14,17);  
   
print("List after swapping nodes: ");  
sList.display();  