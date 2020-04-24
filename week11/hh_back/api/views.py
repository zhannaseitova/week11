from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from api.models import Company, Vacancy

def company_list(request):
    try:
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    except:
        return JsonResponse({'message': 'error: no such companies'})


def company_detailed(request, id):
    try:
        company = Company.objects.get(id=id)
        return JsonResponse(company.to_json(), safe=False)
    except:
        return JsonResponse({'message': 'error: no company'})


def company_vacancies(request, id):
    try:
        company__vacancies = Vacancy.objects.filter(company_id=id)
        vacancies_json = [v.to_json() for v in company__vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({'message': 'error: no vacancies in this company'})


def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({'message': 'error: no vacancies'})


def vacancy_detailed(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        return JsonResponse(vacancy.to_json(), safe=False)
    except:
        return JsonResponse({'message': 'error: no such vacancy'})


def top_vacancies(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({'message': 'error: there are no top 10 vacancies'})
