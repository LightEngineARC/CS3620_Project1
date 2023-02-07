import json

file = open("./nodes.json")  # json is a file!
nodes = json.load(file)  # load is a function!
file.close()  # no memory leaks!

playing = True  # to track if the game has been ended

# previous node is in case they don't really want to quit
previousNode = nodes["start"]
currentNode = nodes["start"]  # set the start node

response = ""  # for storing responses. Ultimately not needed out of the playing loop
# for counting the nodes
# print(len(nodes.keys()))

# game loop
while playing:
    # print the text of the node, the narrative/decision
    print("\n" + currentNode['text'] + "\n")
    # Check win/fail condition
    if 'die' in currentNode.keys():
        print(currentNode['prompt'])
        print('You died')
    if 'win' in currentNode.keys():
        print(currentNode['prompt'])
        playing = False
        continue

    # get input using the question from the node that includes the keys for the next nodes
    response = input(currentNode['prompt'])

    # check if input is allowed at the node
    response = response.lower()

    # quit if quitting or get next node and loop
    if response == "quit":
        previousNode = currentNode
        currentNode = nodes[response]
        checkQuit = input(currentNode['prompt'])
        if checkQuit == "y":
            playing = False
        elif checkQuit == "n":
            currentNode = previousNode

    if playing and not (response in currentNode['list'].keys()):
        print("\nIt doesn't look like that option was found. Please make sure your input matches.\nType one of the all "
              "caps words in the prompt to continue\n")

    # Update the previousNode and currentNode
    if playing and response in currentNode['list'].keys():
        previousNode = currentNode
        currentNode = nodes[response]

print('\nThank you for playing\n')
