from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, redirect

pri_data = {
        '1' : ['Абрамов Александр Альбертович', '2004'],
        '2' : ['Близнюк Илья Сергеевич', '2005'],
        '3' : ['Зверев Андрей Александрович', '2000'],
        '4' : ['Карагузин Максим Игоревич', '2002'],
        '5' : ['Круглик Евгений Дмитриевич', '2003'],
        '6' : ['Лысков Влас Евгеньевич', '2003'],
        '7' : ['Маклюсов Роман Романович', '1999'],
        '8' : ['Манешин Антон Сергеевич', '2001'],
        '9' : ['Петрачков Александр Викторович', '2003'],
        '10' : ['Сафонов Глеб Александрович', '2006'],
        '11' : ['Терешин Роман Павлович', '2004'],
        '12' : ['Чертков Федор Андреевич', '2001'],
    }

year_animal = {
    1 : "козы",
    2 : "обезьяны",
    3 : "петуха",
    4 : "собаки",
    5 : "свиньи",
    6 : "крысы",
    7 : "быка",
    8 : "тигра",
    9 : "кролика",
    10 : "дракона",
    11 : "змея",
}

class new_year():
    def __init__(self, year):
        self.year = int(year)

    def print(self):
        if int(self.year) >= 2015 and int(self.year) <= 2025:
            return f"Год {year_animal[self.year - 2014]}"
        else:
            return redirect(f"/home", permanent=True)

class year_interpreter():
    def __init__(self, year):
        self.year = int(year)
    @property
    def print(self):
        if int(self.year) >= 2015 and int(self.year) <= 2025:
            return "Всё хорошо"
            return f"Год {year_animal[self.year - 2014]}"
        else:
            #raise PermissionDenied()
            return redirect(f"/home", permanent=True)

menu = ["Коротко", "Подробнее", "Главное"]
data_db = [
    {
        "id": 1,
        "title": "Илон Маск",
        "content": "Биография Илона Маска",
        "is_public": True
     },

    {
        "id": 2,
        "title": "Жириновский",
        "content": "Биография Жириновскорого",
        "is_public": True
     },

    {
        "id": 3,
        "title": "Баба Яга",
        "content": "Биография бабы яги",
        "is_public": False
     }

]
float = 3.7

# Create your views here.
def index(request):
    #get = request.GET
    #get_1 = dict(get)
    #print(get_1[name])
    #return HttpResponse(f"Пусто")

    data = {
        "title": "Главная страница",
        "menu": menu,
        "float": float,
        "posts": data_db
    }

    return render(request, "women/index.html", data)


def about(request):
    return redirect("spisok_pri", '12')
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_group(request):
    conclusion = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_data.items():
        conclusion += number + '.'
        conclusion += mas_of_info[0]
        conclusion += '</p>'

    return HttpResponse(conclusion)


def pri_id(request, number_student):

    if str(number_student) in pri_data:
        conclusion = '<h1> ПрИ-201 </h1> <p>'
        group_mas = pri_data[str(number_student)]
        conclusion += f'{group_mas[0]} {group_mas[1]}'
        conclusion += '</p>'
        return HttpResponse(conclusion)
    else:
        return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')

def year_handler(request, year_number):

    if year_number >= 2015 and year_number <= 2025:
        y_i = year_interpreter(year_number)
        return HttpResponse(f"<h1> {y_i.print} </h1>")
    else:
        return redirect("about")


def post_detail(request):
    get = request.GET
    if(get):
        get = dict(get)
        str_get = ""
        for i, j in get.items():
            str_get += i
            str_get += '='
            str_get += j[0]
            str_get += "|"
        #str_get += get[0]
        str_get = str_get[:len(str_get) - 1]
        return HttpResponse(f"<h1> {str_get} </h1>")
    else:
        return HttpResponse(f"<h1> Get is empty </h1>")


def get_data_type(requenst):
    year = new_year(2016)
    return HttpResponse(f"<h1> {year.print()} </h1> <br><br> <h1> {data_db} </h1>")

def get_data_for_number(request, number):
    return HttpResponse(f"<h1> Всё хорошо </h1>")



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> +Страница не найдена проверьте адресс. </h1>")

def page_bad_request_400(request, exception):
    return HttpResponseBadRequest("<h1> Плохой запрос </h1>")

def page_forbiden_403(request, exception):
    return HttpResponseNotFound('<h1> Такого года нету </h1>')

def page_not_found_404(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес! </h1>')

def page_server_error_500(exception):
    return HttpResponseServerError('<h1> Ошибка cтраницы </h1>')