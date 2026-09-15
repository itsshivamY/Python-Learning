file = open('youtube.txt','w')

try:
    file.write('Devesh aur Coffee')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('Codding with Devesh')
