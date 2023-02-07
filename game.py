import json

file = open("./nodes.json")
nodes = json.load(file)

playing = True
previousNode = nodes["start"]
currentNode = nodes["start"]
response = ""
print(len(nodes.keys()))
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
