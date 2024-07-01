from dashboard_app.lists import CATEGORIES

def total_cart(request):
    total = 0
    if "cart" in request.session.keys():
        for key, value in request.session["cart"].items():
            total += int(value["totalPrice"])
    return {"total_cart": total}

def categories(request):
    return {"CATEGORIES": CATEGORIES}