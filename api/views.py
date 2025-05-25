from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.throttling import BaseThrottle
from .models import Subscription
from rest_framework.exceptions import Throttled
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class SubscriptionThrottle(BaseThrottle):
    def allow_request(self, request, view):
        if not request.user or not request.user.is_authenticated:
            raise Throttled(detail="Authentication required.")

        try:
            subscription = Subscription.objects.filter(user=request.user, is_expire=False).first()
        except Subscription.DoesNotExist:
            raise Throttled(detail="No active subscription found.")
        
        if subscription is None:
            raise Throttled(detail="Your subscription has Expire.")

        if subscription.has_hits_left():
            subscription.increment_usage()
            return True

        # Raise Throttled to trigger get_throttled_response()
        raise Throttled(detail=f"You have reached your API usage limit for: {subscription.plan} plan.")



class ProductListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    throttle_classes = [SubscriptionThrottle]
    

    def get_throttled_response(self, wait):
        return Response({
            "detail": "You have reached your API usage limit for this plan. Please upgrade your subscription."
        }, status=status.HTTP_429_TOO_MANY_REQUESTS)
    

