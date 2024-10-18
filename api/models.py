from django.db import models


class hservice(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=555)
    deatail = models.CharField(max_length=999)
    link = models.CharField(max_length=999)

    def __str__(self):
        return self.heading


class ourservice(models.Model):
    id = models.AutoField(primary_key=True)
    b = models.CharField(max_length=555)
    h4 = models.CharField(max_length=999)
    p = models.CharField(max_length=999)

    def __str__(self):
        return self.b


class review(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=999)
    h4 = models.CharField(max_length=355)
    h5 = models.CharField(null=True)
    p = models.CharField(max_length=777)
    h5b = models.CharField(max_length=255)

    def __str__(self):
        return self.h4


class vehicleAll(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.p


class vehicleFirst(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.p


class vehicleSecond(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.p


class vehicleThird(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.p


class vehicleFourth(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.p


class service(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    h5 = models.CharField(max_length=455)
    p = models.CharField(max_length=999)
    link = models.CharField(max_length=999)

    def __str__(self):
        return self.h5


class team(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=999)
    h2 = models.CharField(max_length=255)

    def __str__(self):
        return self.h2


class contact(models.Model):
    name = models.CharField(max_length=555)
    subject = models.CharField(max_length=999)
    email = models.EmailField()
    message = models.CharField(max_length=999)
