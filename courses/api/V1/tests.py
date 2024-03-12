import pytest
from rest_framework.test import APIClient




@pytest.mark.django_db
class TestCourses:

    def test_view_api_course_list_view(self):
        url = "http://127.0.0.1:8000/courses/api/V1/courses/"
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200

    def test_view_api_view_category(self):
        url = "http://127.0.0.1:8000/courses/api/V1/category/"
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
        
    def test_view_api_create_category(self):
        url = "http://127.0.0.1:8000/courses/api/V1/category/"
        client = APIClient()
        data = {
            'name': 'test',
        }
        response = client.post(url, data=data)
        assert response.status_code == 401

    def test_view_api_create_category_with_normal_user(self):
        pass

    def test_view_api_create_category_with_superuser(self):
        pass


