# Спросить человека размеры поля (х * у), получить их ОДНИМ вводом '7x8', "нарисовать" поле буковками о без использования цикла.
size = input('Какого размера поле ты хочешь?\n')
xy = size.split('x')
x = int(xy[0])
y = int(xy[1])
print(('O' * y + '\n') * x)
