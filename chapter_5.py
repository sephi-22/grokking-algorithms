#Example of pushing and popping in a queue (enqueue/dequeue)

def person_is_seller (name):
    return name[-1]=='m' #Checks whether their name ends with the letter m. If it does, they're a mango seller.

from collections import deque
search_queue = deque() #Creates a new queue
search_queue + = graph["you"] #Adds all of your neighbors to the search queue

while search_queue: #While the queue isn't empty
    person = search_queue.popleft() #grabs the first person off the queue
    if person_is_seller(person): #Check whether the person is a mango seller
        print (person + " is a mango seller!")
        return True
    else:
        search_queue += graph[person] #No they aren't. Add all of their friends (neighbors) to the search queue.
return False #If you reached here, no one in your queue was a mango seller.

#Before checking a person it is important to make sure they haven't been checked already. To do  that, you'll keep a list of
#people you've already checked.
#Here's the final code for breadth-first algorithm

def search(name):
    search_queue = deque()
    search_queue+=graph[name]
    searched = [] #This array is how you keep track of which people you've searched before.
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: #Only search this person if you' haven't already searched them.
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #Marks this person as searched
    return False

search("You")
