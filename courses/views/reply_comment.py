from ..models import Comment
from ..forms import ReplyForm
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ReplyView(LoginRequiredMixin,DetailView):
    template_name = 'course/reply.html'
    model = Comment
    context_object_name = 'comment'

    def post(self, request, *args, **kwargs):
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)