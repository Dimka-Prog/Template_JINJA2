from jinja2 import Template
import pathlib
import matplotlib.pyplot as plt


def evalFunction(x, numFunc):
    if numFunc == 0:
        return pow(x, 3) - 6 * pow(x, 2) + x + 5
    elif numFunc == 1:
        return pow(x, 2) - 5 * x + 1
    elif numFunc == 2:
        return 1 / (pow(x, 2) + 1)


def createPict(x, y):
    line = plt.plot(x, y)
    plt.setp(line, color="blue", linewidth=2)

    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig("../HTML/pict.jpg")

    return "pict.jpg"


a = -2
b = 6
n = 30
namesFunctions = ["f(x)", "y(x)", "z(x)"]

h = (abs(a) + abs(b)) / n

x_list = []
f_list = []
numberFunction = 2
enumeration = a
for i in range(n + 1):
    x_list.append(enumeration)
    f_list.append(evalFunction(enumeration, numberFunction))
    enumeration += h

homePath = str(pathlib.Path.cwd())
homePath = homePath.partition('\\labJINJA')[0]

pathTemplateHTML = homePath + '\labJINJA\HTML\\template.html'
pathIndexHTML = homePath + '\labJINJA\HTML\index.html'
pathIndexCSS = homePath + '\labJINJA\CSS\index.css'

readHTML = open(pathTemplateHTML, 'r', encoding='utf-8-sig')
html = readHTML.read()
readHTML.close()

template = Template(html)
template.globals["len"] = len
template.globals["round"] = round
template.globals["pathCSS"] = pathIndexCSS
template.globals["nameFunc"] = namesFunctions
template.globals["numFunc"] = numberFunction
namePict = createPict(x_list, f_list)
resultHTML = template.render(x=x_list, y=f_list, a=a, b=b, n=n, pict=namePict)

writeHTML = open(pathIndexHTML, 'w', encoding='utf-8-sig')
writeHTML.write(resultHTML)
writeHTML.close()
