# KDRAMA APPLICATION

## Updates

In our continuous effort to enhance the functionality and user experience of our website, we've made several significant updates. This document outlines the changes deployed, detailing added features, updates, and areas that still require attention.

Nicholas Williams - 4/3/24
Nicholas Williams - 4/11/24
Ryan Pivirotto -    4/12/24

### Added Features

- **HTML Pages for Navigation**: Added new `.html` pages to improve website navigation.

- **User Model**: A new User model has been added to our database schema. The User model includes essential attributes needed for user identification and interaction within our platform.

- **CRUD Operations for User**: Corresponding to the User model, started implemention of Create, Read, Update, and Delete (CRUD) operations.

- **CRUD Operations for Drama**: Corresponding to the Drama model, started implemention of Create, Read, Update, and Delete (CRUD) operations.

- **CRUD Operations for Actor**: Corresponding to the Actor model, started implemention of Create, Read, Update, and Delete (CRUD) operations.

- **CRUD Operations for Director**: Corresponding to the Director model, started implemention of Create, Read, Update, and Delete (CRUD) operations.

### Updates

- **Updated URLs and Settings.py**: To link up with the newly added `.html` pages, I've updated our `urls.py` and `settings.py` files. These updates ensure that our website's navigation is integrated smoothly with the backend, allowing for efficient page loading and interaction. This is still not working fully and will need to be debugged further to flesh out system.

### Ongoing and Future Work

- **Testing**: The new features and updates are still in the early stages of testing. We will need to add data to our DB to fully test features properly.

- **CRUD Operations Enhancement**: While the basic CRUD operations for the User, Director, Actor, and Drama model have been implemented, further work is necessary to ensure they work with no errors.

- **More Data**: While there is data in our application, there
still needs a lot more data to fully integrate all the models to thier full potential.

- **Links and Logins**: Added links in several tempaltes to route back to relevant pages AND back to the homepage.
e.g.(drama details link back to drama list, Add Actor back to actor list, and so forth)

- **Corrected links** Corrected the links for the actor_update.html, actor_delete.html, and actor_add.html

- **STYLIN** Added a uniformed styling to all pages that are accessible

- **Fixed character and Actor Error in drama_details.html** Instead of seeing character:none and actor:none, it now has a list of all actors associated with a drama

- **Final Fixes** Tried to get a purchase form to work but it failed but I did go through every use case and found the drama_delete to nto work so I fixed it.
Should be ready for submission