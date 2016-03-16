from django.http import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ReviewForm
from apps.reviews.models import Review
from apps.books.models import Book
import json
# Create your views here.


def create_review(request):
    if request.is_ajax():
        params = dict()
        if request.method == "GET":
            params['form'] = ReviewForm()
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                params['message'] = 'Your review has been saved'
                form.save()
            params['form'] = form

        return render(request, 'reviews/form.html', params)
    else:
        raise Http404


def edit_review(request, review_id):
    if request.is_ajax():
        params = dict()
        # review = Review.objects.get(pk=review_id, user=request.user)
        review = Review.objects.get(pk=review_id)
        if request.method == "GET":
            if review:
                params['form'] = ReviewForm(instance=review)
            else:
                params['message'] = 'This review not exist or not yours.'
        if request.method == "POST":
            if review:
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    params['message'] = 'Your review has been saved'
                    form.save()
                params['form'] = form
            else:
                params['message'] = 'This review not exist or not yours.'

        return render(request, 'reviews/form.html', params)
    else:
        raise Http404


def view_review(request, book_id):
    if request.is_ajax():
        params = dict()
        if request.method == "GET":
            params['form'] = ReviewForm()
            params['reviews'] = Book.objects.get(pk=book_id).review_set.all()
        return render(request, 'reviews/view.html', params)
    else:
        raise Http404


def delete_review(request):
    if request.is_ajax():
        if request.method == "POST":
            # review = Review.objects.get(pk=request.POST.get('id'), user=request.user)
            review = Review.objects.get(pk=request.POST.get('id'))
            if review:
                review.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'Review has been removed.'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'Can\' delete this review.'
                    }),
                    content_type="application/json"
                )
    else:
        raise Http404
