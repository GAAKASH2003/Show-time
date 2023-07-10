from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
# Create your models here.
class movie(models.Model):
    movie_id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=50)
    release_date=models.DateField()
    desc=models.TextField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/',null=True,blank=True)
    youtube_url=models.TextField(max_length=200,default="https://www.youtube.com/embed/NgBoMJy386M")
    def __str__(self) -> str:
        return self.title
    def comments(self):
        return self.review_set.all()

class review(models.Model):
    rev_id=models.AutoField(primary_key=True)
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=100)    
    likes=models.IntegerField(default=0)
    
        
class like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.ForeignKey(review,on_delete=models.CASCADE)



stats=[
    ('1','Available'),
    ('2','Booked')
] 

class theatre(models.Model):
    theatre_id=models.AutoField(primary_key=True)
    theatre_name=models.CharField(max_length=12)
    theatre_address=models.CharField(max_length=15)
    rows=models.PositiveSmallIntegerField(MaxValueValidator(15))
    cols=models.PositiveSmallIntegerField(MaxValueValidator(15))
    
    def __str__(self) -> str:
        return self.theatre_name
    
# class screen(models.Model):
#     screen_id=models.AutoField(primary_key=True)
#     theatre=models.OneToOneField("theatre", on_delete=models.CASCADE)
    
class show(models.Model):
    show_id=models.AutoField(primary_key=True)
    date=models.DateTimeField()
    time=models.TimeField(default='10.30')
    price=models.IntegerField(default=250)
    theatre=models.ForeignKey(theatre,on_delete=models.CASCADE)
    location_url=models.CharField( max_length=100,default="https://maps.google.co.in/?q=17.437147,78.448591(AAA%20Cinemas:%20Ameerpet)")
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.theatre.theatre_name
    

class booking(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    num_ticket=models.PositiveSmallIntegerField(max_length=1,default=1)
    seat_number_choices = [(str(i), str(i)) for i in range(1, 101)] 
    seat_no=models.CharField(max_length=10,choices=seat_number_choices)
    show=models.ForeignKey(show,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qr_code=models.ImageField(upload_to='qr_codes/',blank=True)
    
    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.show.theatre.theatre_name+self.seat_no+self.show.movie.title)
        canvas=Image.new('RGB',(300,300),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{f"{self.show.theatre.theatre_name}|{self.seat_no}|{self.show.movie.title}|{self.show.time} "}'+'.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

 
    
    # row_no=models.PositiveSmallIntegerField(blank=False,null=False)
    # col_no=models.PositiveSmallIntegerField(blank=False,null=False)
class Rating(models.Model):
    Rating_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(movie,on_delete=models.CASCADE,blank=True,default='2')
    rate=models.IntegerField(default=0)
    
    
        


    
    
    
        
    
    
    
    
    
        
    
    