def log(data):
    text = str(f'Name: {data.name}\n'
               f'Typ: {data.typ}\n'
               f'Pos: {data.x}')
    with open('logfile.txt', 'w') as lf:
        lf.write(text)
