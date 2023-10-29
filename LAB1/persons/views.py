from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


def main_page(request):
    persons = Person.objects.order_by('name')
    return render(request, 'persons_list.html', {'items': persons})


@csrf_exempt
def records(request):
    if request.method == "GET":
        persons = Person.objects.order_by('id')
        person_serializer = PersonSerializer(persons, many=True)
        return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            new_person = JSONParser().parse(request)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        person_serializer = PersonSerializer(data=new_person)
        if person_serializer.is_valid():
            result = person_serializer.save()
            return HttpResponse(
                headers={"Location": f"/api/v1/persons/{result.id}"},
                status=status.HTTP_201_CREATED
            )
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def record_by_id(request, pk):
    if request.method == "GET":
        try:
            person = Person.objects.get(id=pk)
            person_serializer = PersonSerializer(person)
            return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PATCH':
        updated_data = JSONParser().parse(request)
        try:
            person = Person.objects.get(id=pk)
        except Person.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        person_serializer = PersonSerializer(person, data=updated_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            person = Person.objects.get(id=pk)
        except Person.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def create(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('persons')
#         else:
#             error = 'Ошибка при заполнении формы'
#
#     form = PersonForm()
#     data = {
#         'form': form
#     }
#     return render(request, 'create.html', data)
