from ..models import Comment
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentEditView(LoginRequiredMixin,UpdateView):
    template_name = 'course/edit.html'
    model = Comment
    fields = ['which_course', 'name', 'email', 'subject', 'message']
    success_url = '/courses/'
    context_object_name = 'comment'