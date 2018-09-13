mysite/  
  manage.py: used to create applications, work with the databases and start the development server.  
  mysite/  
      __init__.py: an empty file that instructs Python to treat this directory as a Python package
      settings.py: contains all website settings. This is where we register any applications we create, the location of our static files, db configuration details, etc.
      urls.py: site url-view mappings. Could contain all url mapping code, _it is more common to delegate some of the mapping to particular applications._
      wsgi.py: used to help the Django application communicate with the web server. _can be treated as the boilerplate._
  myapp/
    migrations/: stores the 'migrations'-files that allow the user to automatically update your databases as modes are modified.
    __init__.py: an empty file created so Django/Python will recognize the folder as a Python Package and allow you to use its objects within other parts of the project.
    views.py: views are stored here
    models.py: models stored here
    tests.py: tests are stored here
    admin.py: administration site configuration
    apps.py: application registration


## Registering the catalog application

When the application is created it has to be registered with the project so it will be included when any tools are run(i.e. models added to db). **To register** an application add it the the ``INSTALLED_APPS`` list in the project settings.
