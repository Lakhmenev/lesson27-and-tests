from cars.models import Car
from django.http import JsonResponse


def get_car(request, pk):
    # TODO напишите view-функцию здесь (Readme.md, Задание get_car)
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse(
        {
            "id": car.id,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        }
    )


def search(request):
    # TODO напишите view-функцию здесь (Readme.md, Задание car_search)
    cars_list = Car.objects.all()
    search_text = request.GET.get("brand", None)
    if search_text:
        cars_list = cars_list.filter(brand=search_text)
    response = []
    for car in cars_list:
        response.append(
            {
                "id": car.id,
                "name": car.name,
                "brand": car.brand,
                "status": car.status,
            }
        )

    return JsonResponse(response, safe=False)
