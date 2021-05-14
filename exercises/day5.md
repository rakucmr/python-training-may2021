### Django exercises
1. [optional] Run the interactive Django shell (`python manage.py shell`) and play around with the ORM (create objects, query db).
```python
>>> from university.models import * 
>>> from datetime import date
>>> ase = University.objects.create(name='ASE', city='buc')  # object creation; returns University object
>>> Student.objects.all()  # select * from students
>>> Student.objects.create(first_name='John', last_name='Doe', date_enrolled=date(2019, 10, 1), university=ase)
>>> john = Student.objects.filter(university=ase).first()  # select * from students where condition
>>> john.last_name = 'Popescu'
>>> john.save()  # object update
```
1. Create a view for student details (similar to university details).
1. Create a template for the student details view. Display all student object fields.
1. Create a url to point to the new view.
1. Link the student details page to the university details page (for each student displayed under current university, transform its name into a link to the details page).
