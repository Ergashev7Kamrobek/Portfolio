from django.shortcuts import render, redirect
from django.urls import reverse
from apps.models import (
    User,
    Skills,
    Service,
    Statistic,
    Portfolio,
    Blog,
    Prize,
    BlogSingles,
    Opinion,
    Comment,
)
# from httpx import post
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# HomePage View


# def homepagefunc(request):
#     return render(request, 'main.html')


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"{email} dan sizga quyidagi habar keldi:/n/n/n{message}"

        try:
            send_mail(
                f"{name} sizga habar yubordi",
                full_message,
                settings.EMAIL_HOST_USER,
                [
                    settings.EMAIL_HOST_USER,
                ],
                fail_silently=False,
            )
            return redirect("home")
        except Exception as e:
            print(f"Email yuborish xato:  {e}")
            return HttpResponse(f"Xato yuz berdi :  {e}")

    users = User.objects.first()
    skills = Skills.objects.all()
    services = Service.objects.all()
    statistic = Statistic.objects.all()
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    prize = Prize.objects.all()
    opinions = Opinion.objects.all()
    return render(
        request,
        "index.html",
        {
            "user": users,
            "skills": skills,
            "services": services,
            "statistic": statistic,
            "portfolios": portfolio,
            "blogs": blog,
            "Prizes": prize,
            "opinions": opinions,
        },
    )


def Portfolio_detailsView(request, id):
    portfolio = Portfolio.objects.filter(id=id).first()
    portfolios = Portfolio.objects.all()
    return render(
        request,
        "portfolio-details.html",
        {"portfolio": portfolio, "portfolios": portfolios, "Blog": Blog},
    )


def BlogSinglesView(request, id):
    blog_singles = BlogSingles.objects.all()
    blog_single = BlogSingles.objects.filter(id=id).first()
    blog = Blog.objects.first()
    users = User.objects.first()

    return render(
        request,
        "blog-single.html",
        {
            "blog_singles": blog_singles,
            "blog_single": blog_single,
            "blogs": blog,
            "user": users,
        },
    )


def commentfunc(request, pk):
    blog = Blog.objects.filter(id=pk).first()
    personal_info = User.objects.first()
    if not blog:
        return redirect("error_page")

    if request.POST:
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        post_id = pk
        text = request.POST.get("text")
        if fullname and post_id and text and email:
            Comment.objects.create(
                fullname=fullname, email=email, post_id_id=post_id, text=text
            )
            return redirect(reverse("post", args=(pk,)))

    searchs = ""
    if request.GET:
        key = request.GET.get("s")
        searchs = BlogSingles.objects.filter(title__contains=key)

    comments = Comment.objects.filter(post_id=pk).order_by("created_at")
    return render(
        request,
        "blog-single.html",
        {
            "comments": comments,
            "searchs": searchs,
            "blog": blog,
            "personal_info": personal_info,
        },
    )


# def signupfunc(request):
#     if request.POST:
#         data = SignUpForm(request.POST, files=request.FILES)
#         if data.is_valid():
#             data.save()
#             return redirect('login')
#     return render(request, 'signup.html')


# def loginfunc(request):
#     if request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('my-profile')
#     return render(request, 'login.html')


# def userfunc(request, username):
#     users = User.objects.filter(username=username).first()
#     if users:
#         # statis = Statistic.objects.filter(user_id_id=users.id).first()
#         # partners = PartnerComment.objects.filter(user_id_id=users.id)
#         # skills = Skill.objects.filter(user_id_id=users.id)
#         # services = Service.objects.filter(user_id_id=users.id)
#         # blogs = Blog.objects.filter(user_id_id=users.id).order_by('-created_at')
#         # portfolio = Portfolio.objects.filter(user_id_id=users.id).order_by('-create_at')
#         return render(request, 'index.html', {'users': users, 'username': username})
#                     #   {'users': users, 'statis': statis, "skills": skills, 'services': services, 'blogs': blogs,
#                     #    'portfolios': portfolio, 'username': username, 'partners': partners})
#     else:
#         return HttpResponse('<h1 style="text-align: center; margin-top: 200px;">404 - Page Not Found!</h1>')
