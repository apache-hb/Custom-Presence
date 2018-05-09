import os

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

default = json.load(open('config.json'))

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

window.mainloop()
