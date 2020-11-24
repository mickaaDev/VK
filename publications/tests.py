from django.test import TestCase, Client
from django.urls import reverse
from .models import Publication

class PublicationTestCase(TestCase):
    def setUp(self):
        publications_url = reverse("publications",  kwargs={"pk": self.id})
        print(reverse)
        c = Client()
        self.response = c.get(publications_url)
        self.publications = Publication.objects.all()

    # def test_publication_open_200_OK(self):
    #         self.assertEqual(self.response.status_code, 200)
            # self.assertContains(self.response.content, "My profile")
            





