from django.db import models



'''
each bed has it's own bed tag
'''
class bedTags(models.Model):
    name = models.CharField(max_length=200,null=False)


    def __str__(self):
        return self.name


'''
each bed has bed type
'''
class bedType(models.Model):
    name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name


'''
the a ward will have a bed layout
e.g
8 rows and each row will have 6 columns
that means 8 rows and each row will have 6 beds
'''
class BedLayout(models.Model):
    row = models.CharField(max_length=10,null=False)
    column = models.CharField(max_length=10,null=False)
    tags = models.ForeignKey(bedTags,on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)
    type = models.ForeignKey(bedType,on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)

    def __str__(self):
        return str(self.id)
