from django.test import TestCase
from django.test import TestCase
from django.urls import reverse


class InfoMarcaTestCase(TestCase):
    def test_info_marca_renderiza_template_correcto(self):
        
        url = reverse('info_marca')

       
        response = self.client.get(url)

        
        self.assertEqual(response.status_code, 200)

       
        self.assertTemplateUsed(response, 'Blog/infomarca.html')


