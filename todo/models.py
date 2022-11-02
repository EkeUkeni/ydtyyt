from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-created']

    @property
    def preview(self):
        return self.description[:50]

