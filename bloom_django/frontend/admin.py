from django.contrib import admin
from frontend.models import Player, PlantType, UserPlant, PlantImageZipFile, Timeline, Background, Pot

class UserPlantInline(admin.TabularInline):
    model = UserPlant

class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        UserPlantInline,
    ]


# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(UserPlant)
admin.site.register(PlantType)
admin.site.register(PlantImageZipFile)
admin.site.register(Timeline)
admin.site.register(Background)
admin.site.register(Pot)