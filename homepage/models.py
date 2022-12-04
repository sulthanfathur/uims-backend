from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class NewsPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='UIMS', blank=True, null=True)
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = NewsPost.objects.all().filter(slug__iexact=original_slug).count()

        # Ensure url slugs with the same title are unique
        if queryset == 0:
            self.slug = original_slug
        else:
            self.slug = original_slug + '-' + str(queryset - 1)

        if self.featured:
            try:
                temp = NewsPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except NewsPost.DoesNotExist:
                pass

        super(NewsPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title