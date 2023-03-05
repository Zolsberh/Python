from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

hd = 'Страница с домашним заданием'
sts = 'Домашнее задание выполнено!!!'

tm = env.get_template('main.html')
msg = tm.render(titel='Домашнее задание', hd=hd, sts=sts)

print(msg)
