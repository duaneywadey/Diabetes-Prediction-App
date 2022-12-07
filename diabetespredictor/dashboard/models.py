from django.db import models
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create your models here.

class Data(models.Model):
	bmi = models.FloatField(null=True)
	dpf = models.FloatField(null=True)
	age = models.PositiveIntegerField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	predictions = models.PositiveIntegerField(blank=True)

	def save(self, *args, **kwargs):
		model = joblib.load('mlmodel/updated_ml_model_diabetes')
		self.predictions = model.predict_proba([[self.bmi, self.dpf, self.age]])[:, 1]	
		self.predictions = self.predictions*100
		return super().save(*args, *kwargs)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return str(self.bp)



