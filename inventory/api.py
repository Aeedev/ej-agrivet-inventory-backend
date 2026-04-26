from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Product


# =============================
# LOGIN
# =============================
@csrf_exempt
@api_view(['POST'])
def login_user(request):
    try:
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        if user:
            login(request, user)
            return Response({"success": True})
        return Response({"success": False})
    except Exception as e:
        print("LOGIN ERROR:", e)
        return Response({"success": False, "error": str(e)})


# =============================
# PRODUCTS
# =============================
@csrf_exempt
@api_view(['GET', 'POST'])
@login_required
def get_products(request):

    # ===== GET =====
    if request.method == 'GET':
        try:
            products = Product.objects.all()
            return Response([
                {
                    "id": p.id,
                    "name": p.name,
                    "category": p.category,
                    "brand": p.brand,
                    "price_per_kg": float(p.price_per_kg or 0),
                    "price_per_sack": float(p.price_per_sack or 0),
                    "quantity": p.quantity
                } for p in products
            ])
        except Exception as e:
            print("GET ERROR:", e)
            return Response({"error": str(e)})

    # ===== POST =====
    if request.method == 'POST':
        print("🔥 POST HIT")
        print("DATA:", request.data)

        try:
            name = request.data.get("name")
            if not name:
                return Response({"success": False, "error": "Name required"})

            product = Product.objects.create(
                name=name,
                category=request.data.get("category") or "",
                brand=request.data.get("brand") or "",
                price_per_kg=float(request.data.get("price_per_kg") or 0),
                price_per_sack=float(request.data.get("price_per_sack") or 0),
                quantity=20
            )

            print("✅ CREATED:", product.id)
            return Response({"success": True})

        except Exception as e:
            print("❌ POST ERROR:", e)
            return Response({"success": False, "error": str(e)})