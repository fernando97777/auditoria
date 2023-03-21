
from django.contrib import admin
from django.urls import path

from grafico.views import questionnaire, results, Home, CreateQuestionView, ListQuestionsView, UpdateQuestionsView, \
    DeleteQuestionView, DiagramaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('listado-preguntas/', ListQuestionsView.as_view(), name='list_questions'),
    path('diagram/', DiagramaView.as_view(), name='diagrama'),
    path('actualizar-preguntas/<pk>', UpdateQuestionsView.as_view(), name='update_questions'),
    path('generar-preguntas', CreateQuestionView.as_view(), name='questions'),
    path('eliminar-pregunta/<pk>', DeleteQuestionView.as_view(), name='delete_questions'),
    path('preguntas/', questionnaire, name='questionnaire'),
    path('resultados/', results, name='results'),
]
