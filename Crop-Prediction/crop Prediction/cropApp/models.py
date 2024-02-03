# from django.db import models
# from joblib import load

# loaded_model = load('ML_model/random_forest_model.joblib')

# loaded_le = load('ML_model/label_encoder.joblib')

# class Data(models.Model):
#     seed_varieties = models.CharField(max_length=100, blank=True)
#     seed_conditions = models.CharField(max_length=100, blank=True)
#     N = models.PositiveIntegerField(null=True)
#     P = models.PositiveIntegerField(null=True)
#     K = models.PositiveIntegerField(null=True)
#     temp = models.PositiveIntegerField(null=True)
#     humid = models.PositiveIntegerField(null=True)
#     ph = models.PositiveIntegerField(null=True)
#     rain = models.PositiveIntegerField(null=True)
#     predictions = models.CharField(max_length=100, blank=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         try:
#             input_data = [[self.N, self.P, self.K, self.temp, self.humid, self.ph, self.rain]]

#             prediction_encoded = loaded_model.predict(input_data)
#             prediction_original = loaded_le.inverse_transform(prediction_encoded)
#             self.predictions = prediction_original[0]
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             self.predictions = "Error"
            
#         return super().save(*args, **kwargs)

#     class Meta:
#         ordering = ['-date']

#     def __str__(self):
#         return f"{self.seed_conditions} {self.seed_varieties} {self.N} {self.P} {self.K} {self.temp} {self.humid} {self.ph} {self.rain} {self.predictions} {self.date}"
