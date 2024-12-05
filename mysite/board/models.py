from django.db import models

class Board(models.Model):
    title = models.CharField(name="제목", verbose_name="제목", max_length=100)
    content = models.TextField(name="내용", verbose_name="내용")
    passwd = models.CharField(name="비밀번호", verbose_name="비밀번호", max_length=100)
    username = models.CharField(name="글쓴이", verbose_name="글쓴이", max_length=10)
    created_at = models.DateTimeField(name="작성일시", verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(name="수정일시", verbose_name="수정일시", auto_now=True)
    
    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
        ordering = ['-created_at']

    def __str__(self):
        return self.title