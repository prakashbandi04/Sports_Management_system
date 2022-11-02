import datetime
from basic_app.models import Room,Booking

def check_avail(room,check_in,check_out):
    print(check_in,check_out)
    avail_list = []
    book_list = Booking.objects.filter(Room=room)
    for b in book_list:
        if b.check_in > check_out or b.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
