from models import *;
import re;

class Requirement:
    def __init__( self, request ):
        self.data = request.POST.get( field_name );
    def __call__( self ):
        return self.data;    

class QuestionRequirement( Requirement ):
    def __init__( self, request, field_name = "question" ):
        self.data = request.POST.get( field_name );
    
    # def collect_subjects( self ):
        # pattern = r"\[\w{3}\d{4}\]";
        # subjects = re.findall( pattern, self.data );
        # self.data = re.sub( pattern, "", self.data );
        # return subjects;
        
    def collect_tags( self ):
        pattern = r"#[A-Za-z0-9]+";
        tags = re.findall( pattern, self.data );
        self.data = re.sub( pattern, "", self.data );
        return subjects;
        
        
class AnswerRequirement( Requirement ):
    def __init__( self, request, field_name = "answer" ):
        self.data = request.POST.get( field_name );
        self.data = self.data if self.data != "" else "";

class Order:
    def __init__( self, question, answer ):
        self.question = question;
        self.answer = answer;
        
        if self.answer == "":
            raise Exception();
    
    def __call__( self ):
        result = None;
        if self.answer is None:
            result = Question( 
                question = self.question(), 
                answer = ""
            );
        else:
            candidates = Question.objects.filter( question = self.question );
            if len(candidates) > 0:
                candidates[0].answer = self.answer();   
                result = candidates[0];
            else:
                
                result = Question( 
                    question = self.question(), 
                    answer = self.answer()
                );
        return result;