from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from grafico.forms import QuestionForm
from grafico.models import Question, Answer


class Home(TemplateView):
    template_name = 'home.html'


class DiagramaView(TemplateView):
    template_name = 'diagrama.html'

    def get_context_data(self, **kwargs):
        result_yes = Answer.objects.filter(text='yes').count()
        result_no = Answer.objects.filter(text='no').count()
        context = super(DiagramaView, self).get_context_data()
        context['count_yes'] = result_yes
        context['count_no'] = result_no
        return context


class ListQuestionsView(ListView):
    model = Question
    template_name = 'list_questions.html'


class UpdateQuestionsView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'update_questions.html'
    success_url = reverse_lazy('list_questions')


class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'delete_question.html'
    success_url = reverse_lazy('list_questions')


class CreateQuestionView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions.html'
    success_url = reverse_lazy('home')


def questionnaire(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        for question in questions:
            answer_text = request.POST.get(f'question_{question.id}')
            answer = Answer(question=question, text=answer_text)
            answer.save()
        return redirect('results')
    context = {'questions': questions}
    return render(request, 'questionnaire.html', context)


def results(request):
    answers = Answer.objects.all()
    yes_count = answers.filter(text='yes').count()
    no_count = answers.filter(text='no').count()
    context = {'yes_count': yes_count, 'no_count': no_count}
    return render(request, 'results.html', context)
