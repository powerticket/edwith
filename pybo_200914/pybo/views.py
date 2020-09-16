from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_at')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 20)
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj,
    }
    return render(request, 'pybo/question_list.html', context)


def detail(request, pk):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=pk)
    form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'pybo/question_detail.html', context)

@login_required
def answer_create(request, pk):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('pybo:detail', pk)
    else:
        form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    # question.answer_set.create(content=request.POST.get('content'))
    return render(request, 'pybo/question_detail.html', context)

@login_required
def question_create(request):
    """
    Pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('pybo:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'pybo/question_form.html', context)
