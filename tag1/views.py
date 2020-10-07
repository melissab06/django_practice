from django.shortcuts import HttpResponse
from django.shortcuts import render

def main(request): 
    return HttpResponse("메인 페이지")

def test(request):
    context = {'키': '키 값이다',
                "num_1" : 100,
                "flt_1": 10.123,
                "str_1": "문자열 저장",
                'list_1': [10,20,"리스트"],
                "dic_1": {"a": "a 저장", "b": "b 저장"}
                }
    print('test 접속')
    return render(request, "tag1/test.html", context)

def tempcode(request):
    result = {
            "순위": [[1, 2, ["a","b","c"], 4, 5], ['육','7', '팔', '구', '10'],[11, 12, 13, 14, 15]] 
            }  #딕셔너리 안에 리스트    
    return render(request, "tag1/tempcode.html", result)

def login(request):
    return render(request, "tag1/login.html")

def office(request):
    return render(request, "tag1/office.html")

def table(request):
    return render(request, "tag1/table.html")

def url(request):
    context = {
                "url": [
                    {"네이버": "https://www.naver.com"},
                    {"구글": "https://www.google.co.kr"},
                    {"다음": "http://www.daum.net"}
                ]
            }
    
    return render(request, "tag1/url.html", context)

def worldcup(request):
    context = {
            "결과": 
            [["순위", "국가", "승점", "승", "무", "패", "득점", "실점", "골득실"],
             [1, {"이란":"https://www.naver.com"}, 17, 5, 2, 0, 6, 0, 6],
             [2, {"대한민국":"https:google.co.kr"}, 13, 4, 1, 2, 9, 7, 2],
             [3, {"시리아": "http://www.daum.net"}, 8, 2, 3, 2, 3, -1, 0],
            ] 
            }
    return render(request, "tag1/worldcup.html", context)
#def test1(request):
#    return HttpResponse("test one 접속완료")