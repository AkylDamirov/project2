from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect, get_object_or_404
from .models import JobsModel, Cart
from .forms  import NewUserFrom, AddVacancy
from django.contrib.auth import login, logout
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.

def index(request):
    jobs = JobsModel.objects.all()
    return render(request, 'job_app/index.html',{'jobs':jobs[::-1]})

def register(request):
    if request.method == 'POST':
        form = NewUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = NewUserFrom
    return render(request, 'registration/register.html', {'form':form})

class Vacancy(CreateView):
    model = JobsModel
    form_class = AddVacancy
    template_name = 'job_app/AddVacancy.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        # form.instance.creator = self.request.user
        form.instance.creator = self.request.user
        return super().form_valid(form)

class about(DetailView):
    model = JobsModel
    template_name = 'job_app/about.html'
    context_object_name = 'job'


def about2(request):
    return HttpResponse('This app was created by Akylbek')



def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            jobs = JobsModel.objects.filter(work_position__contains=query)
            return render(request, 'job_app/searchbar.html', {'jobs':jobs[::-1]})
        else:
            print('no info')
            return request(request, 'job_app/searchbar.html', {})

# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#
#     customer = request.user.customer
#     product = JobsModel.objects.get(id=productId)
#
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     #
#     orderItem = OrderItem.objects.get_or_create(order=order, product=product)
#     orderItem.save()
#
#     # if action == 'add':
#     #     orderItem.quantity +=1
#     # elif action=='remove':
#     #     orderItem.quantity -=1
#     # orderItem.save()
#     #
#     # if orderItem.quantity <= 0:
#     #     orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)
#
# # def update_saved_items(request):
# #     if request.method == 'POST':
# #         user = request.user
# #         job_id = request.POST.get('productId')
# #         action = request.POST.get('action')
# #
# #         if user.is_authenticated:
# #             job = get_object_or_404(JobsModel, id=job_id)
# #
# #             if action == 'add':
# #                 SavedItem.objects.get_or_create(user=user, job=job)
# #
# #             return JsonResponse({'message': 'Item added to saved items successfully.'})
# #
# #         else:
# #             return JsonResponse({'message': 'User is not authenticated.'}, status=403)

def cart(request):
    user = request.user
    if user.is_authenticated:
        jobs = Cart.objects.filter(user=user)
        context = {'jobs':jobs[::-1]}
        return render(request, 'job_app/saved.html', context)
    else:
        return redirect('login')

def cart_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = JobsModel.objects.get(id=product_id)
    baskets = Cart.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Cart.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(current_page)
    return HttpResponseRedirect(current_page)

def cart_delete(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def profile(request):
    user = request.user
    if user.is_authenticated:
        jobs = JobsModel.objects.filter(creator=user)
        context = {'jobs': jobs[::-1]}
        return render(request, 'job_app/profile.html', context)
    else:
        return redirect('login')

def profile_delete(request, id=None): #id=None

    cart = JobsModel.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UpdateVacancy(UpdateView):
    model = JobsModel
    form_class = AddVacancy
    template_name = 'job_app/change.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

def loguot_view(request):
    logout(request)
    return redirect('home')







