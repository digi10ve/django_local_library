# django_local_library
Local Library website written in Django
Website: https://digi10ve.pythonanywhere.com/

## Overview
This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

- There are models for books, book copies, genre, language and authors.
- Users can view list and detail information for books and authors.
- Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
- Librarians can renew reserved books.

![Local Library Model](https://raw.githubusercontent.com/digi10ve/django_local_library/master/catalog/static/images/local_library_model_uml.png)

Built according to the steps in this document:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
