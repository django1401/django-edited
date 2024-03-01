from django.test import TestCase
from django.urls import reverse, resolve
from .views import *
from .forms import *

# Create your tests here.


class TestUrlRoot(TestCase):
     
    def test_view_home(self):
        url = reverse('root:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_view_contact(self):
        url = reverse('root:contact')
        self.assertEquals(resolve(url).func, contact)


    def test_view_about(self):
        url = reverse('root:about')
        self.assertEquals(resolve(url).func, about)

    
    def test_view_trainer(self):
        url = reverse('root:trainer')
        self.assertEquals(resolve(url).func, trainer)

    def test_form_newsletter(self):
        form = NewsLetterForm(data={
            'email': 'testcom',
        })
        self.assertFalse(form.is_valid())


    # def test_view_root(self):
    #     url1 = reverse('root:home')
    #     url2 = reverse('root:contact')
    #     url3 = reverse('root:about')
    #     url4 = reverse('root:trainer')
    #     self.assertEqual(resolve(url1).func.view_class, HomeView)
    #     self.assertEqual(resolve(url2).func, contact)
    #     self.assertEqual(resolve(url3).func, about)
    #     self.assertEqual(resolve(url4).func, trainer)

    


