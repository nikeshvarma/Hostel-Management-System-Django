from django.contrib import messages
from django.shortcuts import render, redirect
from user.views import payment_request_date_expiry, next_due
from user.models import Profile
from . import Checksum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def payment(request):
    try:
        payment_request_date_expiry(request)
        paytm_params = {
            "MID": 'wuozEn97922111650508',
            "WEBSITE": "WEBSTAGING",
            "INDUSTRY_TYPE_ID": "Retail",
            "CHANNEL_ID": "WEB",
            "ORDER_ID": str(request.user.profile.room.room_id),
            "CUST_ID": str(request.user.email),
            "MOBILE_NO": str(request.user.profile.contact_no),
            "EMAIL": str(request.user.email),
            "TXN_AMOUNT": str(request.user.profile.billing_amount),
            "CALLBACK_URL": "http://localhost:8000/payment/handlerequest/",
        }

        paytm_params['CHECKSUMHASH'] = Checksum.generate_checksum(paytm_params, 'N&dcG8knGh@AU307')
        return render(request, 'paytm/paytm.html', {'paytm_params': paytm_params})

    except AttributeError:
        messages.add_message(request, messages.INFO, 'Room not found for payment')
        return redirect('userhome')


@csrf_exempt
def handlerequest(request):
    received_data = request.POST
    paytmChecksum = ''
    response_dict = {}

    for key, value in received_data.items():
        if key == 'CHECKSUMHASH':
            paytmChecksum = value
        else:
            response_dict[key] = value
    isValidChecksum = Checksum.verify_checksum(response_dict, "N&dcG8knGh@AU307", paytmChecksum)

    if isValidChecksum:
        print('Checksum Matched')
        return redirect('payment_done')
    else:
        print("Checksum Mismatched")

    return render(request, 'paytm/payment_status.html', {'response_dict': response_dict})
