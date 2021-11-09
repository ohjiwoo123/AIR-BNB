from math import ceil
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage
from . import models

# 1
# return의 home.html은 템플릿 폴더안에 있는 home.html 같아야한다.
# view이름, all_rooms은 core -> urls.py의 all_rooms 같아야한다.
# context "rooms"는 home.html rooms와 같아야한다.
# def all_rooms(request):
#     # return HttpResponse(content="hello")
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     print(f"offset = {offset}", f"limit={limit}")
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)

#     return render(
#         request,
#         "rooms/home.html",
#         {
#             "potato": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count),
#     },
# )

# 2
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    # Paginator는 두가지 인자를 가진다. 1 object의 목록, 2 페이지번호
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        # rooms = paginator.get_page(page)
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
        # rooms = paginator.page(1)

    # print(vars(rooms.paginator))
