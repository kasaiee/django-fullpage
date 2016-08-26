django-fullpage
===================


django-fullpage is a django project that uses [fullpage.js](http://alvarotrigo.com/fullPage/) to create simple page website.

----------


installation
--------------------
- requirements: install following packages via **pip** or **easy_install**
 - python 2.7
 - django 1.10
 - [django-colorfield 0.1.10](https://github.com/jaredly/django-colorfield)
 - [django-ckeditor 5.0.3](https://github.com/django-ckeditor/django-ckeditor)
- Download Django-fullpage
- Add it to your project directory
- Add these to your **INSTALLED_APPS**
```
 INSTALLED_APPS = [
...
    'ckeditor',
    'ckeditor_uploader',
    'colorfield',
    'fullpage.apps.FullpageConfig',
...
]

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Advance',
    },
}
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + 'ck_uploads/'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True
```
- <i class="icon-file"></i> Add following line to your **urlpatterns** in project's **urls.py** 
```
urlpatterns += [
    url(r'^', include('fullpage.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
```
- Create models via typing following commands in terminal or cmd
```
$ python manage.py makemigrations fullpage
$ python manage.py migrate fullpage
```
- <i class="icon-refresh"></i> Run django server to see the result
```
$ python manage.py runserver
```

> **Note:**

> - Some settings are depends on your project. If you have any problem with installation of django-fullpage see wour wiki or ask us.

#### How me maked django-fullpage?
I maked it to show my students How can i make a site via django in a short time? If you want to know how it maked you can see the learning movie at [aparat](http://www.aparat.com/v/WP0lU).


#### Follow me
- [Github](https://github.com/kasaiee)
- [Telegran](https://telegram.me/pydeveloper2)
- [Aparat](http://www.aparat.com/kasaie)
- [Linkedin](https://www.linkedin.com/in/kasaiee)
