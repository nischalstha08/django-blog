from django.db import migrations

def update_default_image(apps, schema_editor):
    Profile = apps.get_model('users', 'Profile')
    for profile in Profile.objects.all():
        # Check if the old default is used. Adjust the string if needed.
        if profile.image.name in ['default.jpg', 'profile_pics/default.jpg']:
            profile.image = 'default.jpeg'
            profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.RunPython(update_default_image),
    ]
