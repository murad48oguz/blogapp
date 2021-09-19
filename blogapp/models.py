from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField




CATEGORY = (
    
    ('news', 'news'),
    ('world', 'world'),
    ('sport', 'sport'),
    ('music', 'music'),
    
)
    

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)  
   
    
    def __str__(self):
        return self.tag_name
        

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='title')
    slug = models.SlugField(max_length=100,editable = False)
    image = models.ImageField(null=True, blank = True, upload_to = 'post')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Post content')
    publish_date = models.DateField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY, max_length=50)
    tag = models.ManyToManyField(Tag)
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    

        
    def __str__(self):
        return self.title 
    
    
    class Meta:
        ordering = ( '-publish_date' , )
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s - %s" % (self.post.title, self.comment_author)
   
    
    class Meta:
        ordering = ['-comment_content']
        
        

    
   
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    


    



