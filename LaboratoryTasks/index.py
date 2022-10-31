from jinja2 import Template

pathTemplateHTML = '\PythonLabs\web-backend\Hotel\HTML\\template.html'
pathIndexHTML = '\PythonLabs\web-backend\Hotel\HTML\index.html'
pathMacros = "\PythonLabs\web-backend\Hotel\HTML\macros.html"

readHTML = open(pathTemplateHTML, 'r', encoding='utf-8-sig')
html = readHTML.read()
readHTML.close()

student = [
    ["Алина", "38.03.05", "Бизнес-информатика", ["Базы данных", "Программирование", "Эконометрика", "Статистика"], "ж"],
    ["Вадим", "38.03.01", "Экономика", ["Информатика", "Теория игр", "Экономика", "Эконометрика", "Статистика"], "м"],
    ["Ксения", "38.03.01", "Экономика", ["Информатика", "Теория игр", "Статистика"], "ж"]
]


def add_spaces(text):
    return " ".join(text)


template = Template(html)
template.globals['add_space'] = add_spaces
template.globals['len'] = len
resultHTML = template.render(user=student[1], pathMacros=pathMacros)

writeHTML = open(pathIndexHTML, 'w', encoding='utf-8-sig')
writeHTML.write(resultHTML)
writeHTML.close()
