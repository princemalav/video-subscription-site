from django.shortcuts import render
from .models import Membership , UserMembership
from django.views.generic import ListView
# Create your views here.

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

class MemberSelectView(ListView):
     model = Membership
     def get_context_data(self,*args,**kwargs):
         context = super().get_context_data(**kwargs)
         current_memberhip = get_user_membership(self.request)
         context['current_membership'] = str(current_memberhip.membership)
         return context
