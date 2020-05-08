from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# Create your views here.
def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html',{'reviews':reviews})

@login_required
def create_review(request):
    if request.method=="GET":
        create_form = ReviewForm()

        return render(request, 'reviews/create.template.html',{'form':create_form})

    if request.method=='POST':
        create_form = ReviewForm(request.POST)

        if create_form.is_valid():
            saved_form = create_form.save()
            messages.success(request, f"the review '{saved_form.title}' has been created!")
            return redirect(reverse(index))
        else:
            return render(request, 'reviews/create.template.html', {
                'form': create_form
            })

@login_required
def update_review(request, reviewid):
    update_form = get_object_or_404(Review, pk=reviewid)
    if request.method == 'GET':
        update_instance = ReviewForm(instance=update_form)
        return render(request, 'reviews/create.template.html',{'form': update_instance})

    elif request.method == 'POST':
        updated_instance = ReviewForm(request.POST, instance=update_form)
        if updated_instance.is_valid():
            saved_form = updated_instance.save()
            messages.success(request, f"the review '{saved_form.title}' has been updated")
            return redirect(reverse(index))
        else:
            return render(request, 'reviews/create.template.html',{'form': update_instance})
@login_required
def delete_review(request, reviewid):
    delete_form = get_object_or_404(Review, pk=reviewid)
    if request.method == 'GET':
        return render(request, 'reviews/delete.template.html',{'form': delete_form})

    elif request.method == 'POST':
        deleted_form = delete_form.delete()
        messages.success(request, f"the review '{delete_form.title}' has been deleted")
        return redirect(reverse(index))
    
