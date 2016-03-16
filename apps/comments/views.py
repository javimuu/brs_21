from django.http import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse
from apps.comments.forms import CommentForm
from apps.reviews.models import Review
from apps.comments.models import Comment
from .icons import ICONS
import json
# Create your views here.


def create_comment(request):
    if request.is_ajax():
        params = dict()
        if request.method == "GET":
            params['form'] = CommentForm()
            return render(request, 'comments/form.html', params)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                params['message'] = 'Your comment has been saved.'
                params['form'] = CommentForm()
                form.save()
            else:
                params['form'] = form
            params['comments'] = Review.objects.get(pk=request.POST.get('review')).comment_set.all()
            return render(request, 'comments/new.html', params)
    else:
        raise Http404


def edit_comment(request, comment_id):
    if request.is_ajax():
        params = dict()
        # comment = Review.objects.get(pk=comment_id, user=request.user)
        comment = Comment.objects.get(pk=comment_id)
        if request.method == "GET":
            if comment:
                params['message'] = 'Editing comment: "' + comment.comment + '"'
                params['form'] = CommentForm(instance=comment)
            else:
                params['message'] = 'This comment not exist or not yours.'
            return render(request, 'comments/form.html', params)
        if request.method == "POST":
            if comment:
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                    params['message'] = 'Your comment has been saved.'
                    form.save()
                params['form'] = form
            else:
                params['message'] = 'This comment not exist or not yours.'
            params['comments'] = Review.objects.get(pk=request.POST.get('review')).comment_set.all()
            return render(request, 'comments/view.html', params)
    else:
        raise Http404


def emoticons(request):
    if request.is_ajax():
        params = dict()
        if request.method == "GET":
            params['icons'] = ICONS
            return render(request, 'comments/icon.html', params)
    else:
        raise Http404


def delete_comment(request):
    if request.is_ajax():
        if request.method == "POST":
            # comment = Comment.objects.get(pk=request.POST.get('id'), user=request.user)
            comment = Comment.objects.get(pk=request.POST.get('id'))
            if comment:
                comment.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'Comment has been removed.'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'Can\' delete this comment.'
                    }),
                    content_type="application/json"
                )
    else:
        raise Http404
