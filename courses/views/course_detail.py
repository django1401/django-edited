from django.shortcuts import get_object_or_404, redirect
from ..models import Course
from django.views.generic import DetailView
from ..cart import Cart
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course-details.html'
    context_object_name = 'course'

    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if 'id' in request.POST :
            product = get_object_or_404(Course, id=int(request.POST['id']))    
            cart.delete_from_cart(product)
            
        else:
            product = get_object_or_404(Course, id=int(request.POST['pk']))
            quantity = int(request.POST['quantity'])
            cart.add_to_cart_some_quantity(product, quantity)
            
        return redirect(request.path_info)