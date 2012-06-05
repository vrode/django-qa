# Create your views here.

from django.shortcuts import render_to_response, redirect;
from django.template import RequestContext;
from django.core.context_processors import csrf;
from django.views.decorators.csrf import csrf_protect;
from django.contrib.auth.models import User;

from random import choice;

from models import *;
from controls import *;


@csrf_protect
def index( request ):
    return redirect( "add/" );


@csrf_protect
def list( request ):
    return render_to_response( "listing.html", {
            'questions': Question.objects.all()
        },
        context_instance = RequestContext( request )
    );

@csrf_protect
def home( request, question = "", answer = "" ):
    return render_to_response( "main.html", {
            'title': 'Questions and Answers',
            'question': question,
            'answer': answer,
        },
        context_instance = RequestContext( request )
    );

@csrf_protect    
def save( request ):
    question = QuestionRequirement( request );
    answer = AnswerRequirement( request );
    
    try:
        order = Order( question, answer );
        order().save();
    except Exception:
        pass;
    
    return redirect( "/" + __name__.replace(".views","") + "/add/" );
    

@csrf_protect
def random( request ):
    unanswered = Question.objects.filter( answer = "" );
    if len( unanswered ) > 0:
        candidate = choice( unanswered );
    else:
        return redirect( "/" );
    return home( request, candidate.question, candidate.answer );
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    