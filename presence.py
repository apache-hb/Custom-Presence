import os
import sys

try:
    from pypresence import Presence
except ImportError:
    os.system('python3 -m pip install pypresence')
    print('Setup complete, please restart')
    exit(5)

from time import sleep, time
from datetime import datetime
import json
import tkinter

try:
    if sys.argv[1] == '-w':
        wizard = True
except IndexError:
    wizard = False

default = [
    {
        'name': 'game name',
        'id': 'some id',
        'states': [
            {
                'name': 'state1',
                'details': '',
                'state': '',
                'small_image': '',
                'small_text': '',
                'large_image': '',
                'large_text': ''
            }
        ]
    },
    {
        'name': 'game other name',
        'id': 'some other id',
        'states': [
            {
                'name': 'state1',
                'details': '',
                'state': '',
                'small_image': '',
                'small_text': '',
                'large_image': '',
                'large_text': ''
            },
            {
                'name': 'state2',
                'details': '',
                'state': '',
                'small_image': '',
                'small_text': '',
                'large_image': '',
                'large_text': ''
            }
        ]
    }
]

if not os.path.exists('config.json'):
    file = open('config.json', 'w').close()
    json.dump(default, open('config.json', 'w'), indent=4)
    wizard = True
    print('Config file was generated')

default = json.load(open('config.json'))

if wizard:
    next_ = input('Do you want to add a game or a state to a game?').lower()
    if next_ == 'state':
        add = input('which game would you like to add this too?')

        another_state = {
            'name': input('Add name'),
            'details': input('Input details'),
            'state': input('input state'),
            'small_image': input('small image key'),
            'small_text': input('small image text'),
            'large_image': input('large image key'),
            'large_text': input('large image text')
        }
        for x in default:
            if x['name'].lower() == add.lower():
                x['states'].append(another_state)

    elif next_ == 'game':
        another_game = {
            'name': input('new name'),
            'id': input('input client id'),
            'states': [
                {

                }
            ]
        }

    else:
        print('either input game or state')

window = tkinter.Tk()
window.title('Don\'t close me')
window.geometry('300x20')

b = -1
for a in default:
    b += 1
    print(a['name'], b)

index = int(input('select index for game\n'))

d = -1
for c in default[index]['states']:
    d += 1
    print(c['name'], d)

subindex = int(input('select which state to use\n'))

client = Presence(default[index]['id'])
client.connect()

for key, value in default[index]['states'][subindex].items():
    if value == '':
        print(key, value)
        value = None
        print(key, value)



print(client.update(
    state=default[index]['states'][subindex].get('state'),
    details=default[index]['states'][subindex].get('details'),
    small_image=default[index]['states'][subindex].get('small_image'),
    small_text=default[index]['states'][subindex].get('small_text'),
    large_image=default[index]['states'][subindex].get('large_image'),
    large_text=default[index]['states'][subindex].get('large_text'),
    start=int(time())
))
print('opened a window, just minimize it')

window.mainloop()
