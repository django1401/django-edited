from django.test import TestCase
from django.urls import reverse, resolve
from .views import *



class TestUrlCourse(TestCase):
     
    def test_view_courselist(self):
        url = reverse('courses:courses')
        self.assertEquals(resolve(url).func.view_class, CourseListView)

    def test_view_course_detail(self):
        url = reverse('courses:course_detail', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, CourseDetailView)

    def test_view_course_cat(self):
        url = reverse('courses:course_cat', kwargs={'cat': 'test'})
        self.assertEquals(resolve(url).func.view_class, CourseListView)

    def test_view_course_delete(self):
        url = reverse('courses:delete', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, DeleteCommentView)