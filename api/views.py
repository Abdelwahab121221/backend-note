from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status
from .serializers import Noteserializer
from .models import Note
# Create your views here.
def Home(request):
    return render(request,'Home.html')
@api_view(["GET"])
def get_notes(request):
    return Response(Noteserializer(Note.objects.all(),many=True).data)
@api_view(['GET'])
def get_note_by_id(request,id):
    try:
        note = Note.objects.get(id = id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(Noteserializer(note).data)
{
    "name": "end react native course",
    "note": "end full react native course",
}
@api_view(['POST','GET'])
def post_note(request):
    if request.method == 'GET':
        return Response(Noteserializer(Note.objects.all(),many=True).data)
    else:
        new_note = Noteserializer(data=request.data)
        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
def update_note(request,id):
    try:
        note = Note.objects.get(id = id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Noteserializer(note).data)
    else:
        noteser = Noteserializer(note,data=request.data)
        if noteser.is_valid():
            noteser.save()
            return Response(noteser.data)
@api_view(["GET","DELETE"])
def delete_note(request,id):
    try:
        note = Note.objects.get(id = id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Noteserializer(note).data)
    else:
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)