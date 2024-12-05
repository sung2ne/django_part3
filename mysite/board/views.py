from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .models import Board
from .forms import BoardForm

# 게시글 등록
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            messages.success(request, '게시글이 등록되었습니다.')
            return redirect("board:read", board_id=board.id)
        else:
            for field_name, error_messages in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_messages[0]}")
    else:
        form = BoardForm()
        
    return render(request, 'board/board_create.html', {'form': form})

# 게시글 보기
def board_read(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/board_read.html', {'board': board})

# 게시글 수정
def board_update(request, board_id):
    board = Board.objects.get(id=board_id)
    
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        
        if form.is_valid():
            if form.cleaned_data['passwd'] == board.passwd:
                board = form.save(commit=False)
                board.save()
                messages.success(request, '게시글이 수정되었습니다.')
                return redirect('board:read', board_id=board.id)
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')
        else:
            for field_name, error_messages in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_messages[0]}")
    else:
        form = BoardForm(instance=board)
        
    return render(request, 'board/board_update.html', {'form': form})

# 게시글 삭제
def board_delete(request, board_id):
    board = Board.objects.get(id=board_id)
    
    if request.method == 'POST':
        if request.POST['passwd'] == board.passwd:
            board.delete()
            messages.success(request, '게시글이 삭제되었습니다.')
            return redirect('board:list')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('board:read', board_id=board.id)

# 게시글 목록
def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})