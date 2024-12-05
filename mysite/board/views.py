from django.shortcuts import redirect, render
from django.http import HttpResponse

# 게시글 등록
def board_create(request):
    return HttpResponse('게시글 등록')

# 게시글 목록
def board_list(request):
    return HttpResponse('게시글 목록')

# 게시글 보기
def board_read(request, board_id):
    return HttpResponse('게시글 보기')

# 게시글 수정
def board_update(request, board_id):
    return HttpResponse('게시글 수정')

# 게시글 삭제
def board_delete(request, board_id):
    return HttpResponse('게시글 삭제')
