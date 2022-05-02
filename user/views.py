from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms import formset_factory, inlineformset_factory
from user.forms import UserCreationForm, KidRegisterForm, UpdateUserForm, UpdateKidForm
from user.models import User, Kid
from django.views.decorators.csrf import csrf_exempt
from user.decorators import *


# 회원가입
@logout_message_required
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        id = request.POST.get('id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        name = request.POST.get('name')      
        # 사용자 아이디가 이미 존재하는 아이디인 경우
        try: 
            if User.objects.get(id=id):
                id_error_msg = '이미 존재하는 아이디입니다.'
            context={
                'form' : form,
                'id_error_msg' : id_error_msg,
            }
            return render(request, 'user/signup.html', context)        
        except:
            # 비밀번호와 비밀번호 확인이 일치하지 않는 경우
            if password1 != password2:
                password_error_msg = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
                return render(request, 'user/signup.html', {'form': form, 'password_error_msg': password_error_msg})
            else:
                if form.is_valid():
                    User.objects.create_user(id=id, username=id, password=password1, email=email, name=name)
                    # user = authenticate(username=id, password=password1)  # 사용자 인증
                    # auth_login(request, user)  # 로그인
                    return redirect('user:login')
                else:
                    email_error_msg = '이메일 양식이 맞지 않습니다.'
                    context = {
                        'form' : form,
                        'email_error_msg' : email_error_msg,
                    }
                    return render(request, 'user/signup.html', {'form': form, 'email_error_msg': email_error_msg})
    else:
        form = UserCreationForm()
    context={
        'form' : form,
    }
    return render(request, 'user/signup.html', context)


# 아이디 중복체크
def id_check(request):
    id = request.GET.get('user_id')
    result = 'fail'
    try:
        check_result =  User.objects.get(id=id)
    except:
        check_result = None
    if check_result is None:
        result = 'possible'
    return JsonResponse({ 'result': result })


# 로그인
@logout_message_required
def CustomLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        user_id = request.POST.get('username')
        try:
            User.objects.get(username=user_id)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('user:kid_select')
            else:
                password_error_msg = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
                context = {
                    'form' : form,
                    'password_error_msg' : password_error_msg,
                }
                return render(request, 'user/login.html', context)
        except:
            id_error_msg = '일치하는 아이디가 없습니다.'
            context = {
                    'form' : form,
                    'id_error_msg' : id_error_msg,
            }
            return render(request, 'user/login.html', context)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'user/login.html', context)


# 아이등록
@login_message_required
def kid_register(request):
    if request.method == "POST":
        form = KidRegisterForm(request.POST, request.FILES)
        print(request)
        if form.is_valid():
            kid_regit = form.save(commit=False)
            kid_regit.user = request.user
            kid_regit.save()
            return redirect('user:kid_select')
    else:
        form = KidRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


# 아이선택
@login_message_required
def kid_select(request):
    if request.user.is_authenticated:
        user_id = request.session['_auth_user_id']
        kid_set = Kid.objects.filter(user_id = user_id)
    context = {
        'kid_set' : kid_set,
    }
    print(kid_set)
    # return render(request, 'user/select.html', context)
    return render(request, 'user/test1.html', context)


# 회원 정보 수정
@login_message_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            password_error_msg = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
            context = {
                'form': form,
                'password_error_msg': password_error_msg,
            }
            return render(request, 'user/user_update.html', context)
        else:
            if form.is_valid():
                form.save()
                user = authenticate(username=id, password=password1)  # 사용자 인증
                auth_login(request, user)
                messages.success(request, '회원정보가 수정되었습니다.')
                return redirect('user:kid_select')
            else:
                email_error_msg = '이메일 양식이 맞지 않습니다.'
                context = {
                    'form' : form,
                    'email_error_msg' : email_error_msg,
                }
                return render(request, 'user/user_update.html', context)  
    else:
        form = UpdateUserForm()
    context = {
        'form' : form,
        'user' : user,
    }
    return render(request, 'user/user_update.html', context)


# 회원탈퇴
@login_message_required
def member_del(request):
    user_id = request.session['_auth_user_id']
    data = User.objects.get(pk=user_id)
    data.delete()
    logout(request)
    return redirect('/')


# 로그아웃
# @logout_message_required
def CustomLogout(request):
    logout(request)
    return redirect('/')


# 아이디 찾기 메일링 서비스
@logout_message_required
def ForgotIDView(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                template = render_to_string('user/find_username_email_template.html', 
                                            {'name': user.name, 'id':user.username})
                method_email = EmailMessage(
                    '[밀키드] 요청하신 ID입니다.',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'user/find_username_done.html', context)
        except:
            email_error_msg = '일치하는 이메일이 없습니다.'
            context = {
                'email_error_msg' : email_error_msg,
            }
            return render(request, 'user/find_username_form.html', context)
    context = {}
    return render(request, 'user/find_username_form.html', context)


# 아이 정보 삭제
@login_message_required
def kid_del(request):
    kid_id = request.session['kid_id'] # 아이 세션 정보를 받아와야 함
    data = Kid.objects.get(pk=kid_id)
    data.delete()
    return redirect('user:kid_select')


# 아이 정보 수정(각자) # meal view에 위치해야 할 듯
@login_message_required
def kid_update_each(request):
    kid_id = request.session['kid_id']
    kid = Kid.objects.get(pk=kid_id)
    if request.method == 'POST':
        form = UpdateKidForm(request.POST, request.FILES, instance=kid)
        if form.is_valid():
            form.save()
            messages.success(request, '아이 정보가 수정되었습니다.')
            return redirect('meal:meal')
    else:
        form = UpdateKidForm(instance=kid)
    context = {
        'form' : form,
        'kid' : kid,
    }
    return render(request, 'user/kid_update_each.html', context)

    
# 아이 선택 시 세션에 저장
@csrf_exempt
def kid_send(request):
    request.session['kid_id'] = 0
    if request.session['kid_id'] == 0:
        request.session['kid_id'] = request.POST.get('kid_id')
    return  render(request, 'user/user_update.html')