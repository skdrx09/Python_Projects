from random import choice, randint
import yaml

with open('./config.yaml', mode='r') as cfg:
    entity = yaml.load(cfg, Loader=yaml.FullLoader)


names_list = entity['Entity']['name']
my_name = choice(names_list)
names_list.remove(my_name)
other_name = choice(names_list)
names_list.remove(other_name)

person = choice(entity['Entity']['person'])

subject = []
for value in person.values():
    subject += value
my_subject = subject[randint(0, (len(subject)-1))]


for key in entity['Entity']['verb']:
    if key in person:
        verb = entity['Entity']['verb'][key]
my_verb = verb[randint(0, (len(subject)-1))]

obj_index = (len(entity['Entity']['object']) - 1)
my_object = entity['Entity']['object'][randint(0, obj_index)]

answer = choice(entity['Entity']['answer'])

print(f'\n{my_name}: {my_subject} {my_verb} {my_object}')
print(f'{other_name}: {answer}\n')