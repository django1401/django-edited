from ..models import Comment
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class DeleteCommentView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'course/comment_confirm_delete.html'
    success_url = '/courses/'