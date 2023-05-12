from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.core.paginator import Paginator

from .models import User, NewTweet, Profile


def index(request):
    all_post = NewTweet.objects.all()
    # creating pagination
    pagination = Paginator(NewTweet.objects.all(), 10)
    page = request.GET.get('page')
    paginated_posts = pagination.get_page(page)
    num_page = "a" * paginated_posts.paginator.num_pages

    context = {
        "all_post": all_post,
        "paginated_posts": paginated_posts,
        "num_page": num_page,
    }
    return render(request, "network/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):
    if request.method == "POST":
        # author = request.user.username
        author = request.user
        caption = request.POST["caption"]
        new_post = NewTweet.objects.create(user=author, caption=caption)
        new_post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))
        # return render(request, "network/layout.html", context)

def profile(request, user_id):
    profile = User.objects.get(pk=user_id)
    post_count = NewTweet.objects.filter(user = user_id).count()
    profile_post = NewTweet.objects.filter(user = user_id)
    # to create pagination
    pagination = Paginator(NewTweet.objects.filter(user=user_id), 10)
    page = request.GET.get('page')
    paginated_posts = pagination.get_page(page)
    num_page = "a" * paginated_posts.paginator.num_pages

    if request.method == "POST":
        current_user_profile = request.user
        if user_id != request.user.id:
            if request.user.follows.filter(pk=user_id).exists():
                current_user_profile.follows.remove(profile)
                is_following = False
            else:
                current_user_profile.follows.add(profile)
                is_following = True
            context = {
                "profile": profile,
                "post_count": post_count,
                "is_following": is_following,
                "profile_post": profile_post,
                "paginated_posts": paginated_posts,
                "num_page": num_page,
            }
            current_user_profile.save()
            return render(request, "network/profile.html", context)
    context = {
        "profile": profile,
        "post_count": post_count,
        "profile_post": profile_post,
        "paginated_posts": paginated_posts,
        "num_page": num_page,
    }
    return render(request, "network/profile.html", context)



def likes_post(request, post_id):
        if request.user.is_authenticated:
            user = request.user
            post = NewTweet.objects.get(pk = post_id)
            # check if the post has likes from the current user
            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)
                likes_post = False
            else:
                post.likes.add(user)
                likes_post = True
            return HttpResponseRedirect(reverse("index"))
        context = {
            "post": post, 
            "likes_post": likes_post
        }

        return render(request, "network/index.html", context)

def following_feed(request):
    user_following_list = []
    user_following_feed = []

    user_following = User.objects.filter(follows=request.user)

    # to create pagination
    pagination = Paginator(NewTweet.objects.filter(user=request.user), 10)
    page = request.GET.get('page')
    paginated_posts = pagination.get_page(page)
    num_page = "a" * paginated_posts.paginator.num_pages

    for users in user_following:
        user_following_list.append(users)

    for users in user_following_list:
        feed_lists = NewTweet.objects.filter(user=users)
        user_following_feed.append(feed_lists)

    feed_list = list(chain(*user_following_feed))
    
    context = {
        "following_post": feed_list,
        "paginated_posts": paginated_posts,
        "num_page": num_page,
    }
    return render(request, "network/following.html", context)

def edit_post(request, post_id):
    post = NewTweet.objects.get(pk=post_id)
    if request.method == "POST":
        caption = request.POST["caption"]
        post.caption = caption
        post.save()
        # return render(request, "network/edit_post.html")
        # return redirect("network/index")
        return HttpResponseRedirect(reverse("index"))

    context = {
        "post": post,
    }
    return render(request, "network/edit_post.html", context)

