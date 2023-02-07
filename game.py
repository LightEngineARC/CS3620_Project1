import json

file = open("./nodes.json")
nodes = json.load(file)

print(nodes['start'])

playing = True
previousNode = None
currentNode = nodes["start"]

# game loop
while playing:
    # print the text of the node, the narrative/decision
    print(currentNode['text']+"\n\n")
    # get input using the question from the node that includes the keys for the next nodes
    response = input(currentNode['prompt'])

    # check if input is allowed at the node
    response = response.lower()

    # Update the previousNode and currentNode
    if response in currentNode['list'].keys():
        previousNode = currentNode
        currentNode = nodes[response]

    # quit if quitting or get next node and loop

