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

This diagram shows the entity relationship between the each model in the database model structure of the application:

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
