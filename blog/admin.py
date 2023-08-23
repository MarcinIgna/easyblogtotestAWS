from django.contrib import admin
from .models.user_model import UserModel
from .models.post_model import PostModel
from .models.comment_model import CommentModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)