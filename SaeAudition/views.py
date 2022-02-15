from django_filters import filters
from rest_framework import status, mixins, viewsets
from rest_framework import generics, permissions
from flask import json
from rest_framework.response import Response
from .models import Question, Answer
from register.models import Profile
from .serializers import questionSerializer, answerSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = questionSerializer

    # parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [
    # permissions.IsAuthenticated,
    # ]
    def post(self, request, format=None):
        serializer = questionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = answerSerializer
    # parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [
    # permissions.IsAuthenticated,
    # ]

    filterset_fields = ['profile', 'question']

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        question = Question.objects.all()
        questionlist = []
        for i in question:
            questionlist.append({
                'round': i.ques_round,
                'type': i.question_type,
                'text': i.question_text,
                'image': i.image,
            })
    
        if request.method == 'POST':
            answer = request.POST
        
            for i in question:
                responses = Answer.objects.create(profile=profile, question=i)
                responses.response = answer[str(i.ques_round)]

        responses.id=user.id
        serializer = self.get_serializer(responses)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create funct 
        """
        # is_many = isinstance(request.data, list)
        # if not is_many:
        # return super(BookViewSet, self).create(request, *args, **kwargs)
        # else:
        # serializer = self.get_serializer(data=request.data, many=True)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)








