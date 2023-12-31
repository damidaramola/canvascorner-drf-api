# CanvasCorner using the Django Rest Framework

**Developer: Dami Daramola**

[view: web link](https://canvascorner-drf-api-8c6faae9ad24.herokuapp.com/)

## Table of Contents

- User stories
- Database 
- Validation 
- Testing 
- Technologies used 
- credits

## User Stories 

This is the backend section of the CanvasCorner project where the http requests will be made to the Django Rest Framework API

- As an admin, I want to be able to create, edit, update and delete the users bookmarks, likes, comments and posts, in order to
  monitor inappropriate user content

## Database 

This is entity relationship between the each model in the database model structure of the application:

### User Model
- The user model is part of the Django Allauth library
- The user model has a one-to-one relationship with the Profile 'owner' field
- A ForeignKey relationship with the Follower model 'owner' and 'followed' fields 
- ForeignKey relationship with the Post model 'owner' field
- ForeignKey relationship with the Comment model 'owner' field
- ForeignKey relationship with the Like model 'owner' field
- ForeignKey relationship with the Bookmark model 'owner' field

#### Profile Model

- The fields contained in the profile model are: owner, name, description, created_on, updated_on and image
- There is a One-to-one relationship between the owner field and the User model id field

#### Post Model

- The fields contained in the post model are : owner, created_on, updated_on, title, description, category and image
- ForeignKey relationship with the Comment model post field
- ForeignKey relationship with the Like model post field
- ForeignKey relationship with the Bookmark model post field

#### Follower Model

- The Follower model contains the following fields: owner, followed and created_on
- ForeignKey relationship between the owner field and the User model id field
- ForeignKey relationship between the followed field and the User model post field

#### Comment Model

- The Comment model contains the following fields: owner, post, created_on, updated_on and content
- ForeignKey relationship between the owner field and the User model id field
- ForeignKey relationship between the post field and the User model post field

#### Like Model

- The Like model contains the following fields: owner, post and created_on
- ForeignKey relationship between to the User model id field
- ForeignKey relationship between the owner field and the User model id field
- ForeignKey relationship between the post field and the Post model post field

### Bookmark model

- the Bookmark model contains the following fields: owner, post and bookmarked_at

## Technologies used 

### Languages and Frameworks

- Django 
- Python 


## Testing 

Manual Testing was conducted on this application in alignment with the user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Bookmark | Create & delete | A bookmark can be created or deleted (bookmark /un-bookmark post) | Works as expected

## Validation

### PEP8 Validation
[This PEP8](https://pep8ci.herokuapp.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors.



## Tools and Libraries 

- [Django REST Framework](https://www.django-rest-framework.org/) This was used to build the API  in the back-end
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for the authentication of users
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python programming language 
- [PostgreSQL](https://www.postgresql.org/) I used the PostgreSQL database
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub
- [GitHub](https://github.com/) was utilized as a remote repository to store my project code
- [Gitpod)](https://gitpod.io/workspaces) the virtual IDE workspace used to build this site
- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing
- [Cloudinary](https://cloudinary.com/) to store static files and images 


## Credits

### Code

This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api) 