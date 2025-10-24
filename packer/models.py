from django.db import models
import json

# Create your models here.

class CargoItem(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    
    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}x{self.height}, {self.weight}kg)"

class CargoStorage(models.Model):
    STORAGE_CHOICES = [
        ('20ft', '20 ft Container'),
        ('40ft', '40 ft Container'),
        ('curtainsider', 'Curtainsider'),
        ('warehouse', 'Warehouse'),
    ]
    
    storage_type = models.CharField(max_length=20, choices=STORAGE_CHOICES)
    items_json = models.TextField(default='[]')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_items(self):
        return json.loads(self.items_json)
    
    def set_items(self, items):
        self.items_json = json.dumps(items)
    
    def __str__(self):
        return f"{self.storage_type} - {len(self.get_items())} items"
