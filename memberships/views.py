from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Membership , UserMembership , Subscription
from django.views.generic import ListView
# Create your views here.

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
                        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


class MemberSelectView(ListView):
     model = Membership

     def post(self,request,**kwargs):
         selected_membership_type = request.POST.get('membership_type')
         user_membership = get_user_membership(request)
         user_subscription = get_user_subscription(request)

         selected_membership_qs = Membership.objects.filter(membership_type=selected_membership_type)


         if selected_membership_qs.exists():
             selected_membership = selected_membership_qs.first()
         request.session['selected_membership_type'] = selected_membership.membership_type
         return HttpResponseRedirect(reverse('memberships:payment'))


     def get_context_data(self,*args,**kwargs):
         context = super().get_context_data(**kwargs)
         current_memberhip = get_user_membership(self.request)
         context['current_membership'] = str(current_memberhip.membership)
         return context
