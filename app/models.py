from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class BlogPost(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = "blog_posts"

# Модуль для валидации и сериализации данных при чтение в бд      
BlogPost_Pydantic = pydantic_model_creator(BlogPost, name="BlogPost")

# Модуль для валидации входных данных при создаие или обновление(только для чтения!).
BlogPostIn_Pydantic = pydantic_model_creator(BlogPost, name="BlogPostIn", exclude_readonly=True)