from .course_detail import CourseDetailView
from ..models import Course
from django.views.generic import ListView

class CourseListView(ListView):
    
    template_name = 'course/courses.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Course.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Course.objects.filter(teacher__info__email = self.kwargs.get('teacher'))
        elif self.request.GET.get('search'):
            return Course.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Course.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = CourseDetailView()
        return post_detail.post(request,*args,**kwargs)