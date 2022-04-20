from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from user.forms import UserForm
from user.models import User

# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        id = request.POST.get('id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        name = request.POST.get('name')
        
        # 사용자 아이디가 이미 존재하는 아이디인 경우
        try: 
            if User.objects.get(id=id):
                id_error_msg = '이미 존재하는 아이디입니다.'
            return render(request, 'user/signup.html', {'form': form, 'id_error_msg': id_error_msg})
        
        # 사용자 아이디가 유일한 경우
        except:
            if password1 != password2:
                password_error_msg = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
                return render(request, 'user/signup.html', {'form': form, 'password_error_msg': password_error_msg})
            else:
                if form.is_valid():
                    User.objects.create_user(id=id, username=id, password=password1, email=email, name=name)
                    user = authenticate(username=id, password=password1)  # 사용자 인증
                    login(request, user)  # 로그인
                    return redirect('/')

                else:
                    email_error_msg = '이메일 양식이 맞지 않습니다.'
                    return render(request, 'user/signup.html', {'form': form, 'email_error_msg': email_error_msg})



    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})


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