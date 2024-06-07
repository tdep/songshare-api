# songshare-api
The SongShare-API serves as a service layer for social media applications based around music.

### To run locally:
1. Fork the repo 
2. Make sure you have `python 3.x.x` installed on your system 
3. In the directory run: `python3 -m venv env` 
4. Then run: `source env/bin/activate` 
5. Install the packages: `pip install requirements.txt` 
6. Run the migrations: `python manage.py migrate` 
7. Run the seeder for dummy data: `python manage.py setup_test_data` 
   1. This creates a group of `'subscriber'` users and article instances.
   2. To create `'admin'` users, see the next step.
8. Create a user: `python manage.py create_admin_user` 
9. Run the server: `python manage.py runserver` 
10. Open the API in the browser, sign in, and poke around using the endpoints below.

---

### To use the API endpoints
Right now, everything that isn't viewing requires a user login and the passing of JWT Tokens.

As long as the user is signed in, pass the access token with your requests. 

The token needs to be refreshed every `5 minutes`.

---

### Work left to do:
- Clean-up user permissions / groups
- Properly enforce RBAC through dedicated roles (right now there are loosely defined `'subscriber'` and `'admin'` users).
- Write testing suite
- Create more thorough validations
- Favorite functionality (for articles)
- Sharing functionality
- Write logout functionality (once you sign in, you can never leave!)
- Fix the browsable API
- Add `Events`, `Songs`, `Messages` apps
---

## Models
### SongShareUser
| field          | datatype   | constraints                                                                          |
|----------------|------------|--------------------------------------------------------------------------------------|
| `id`           | `int`      | auto-populated, incremental                                                          |
| `username`     | `str`      | required, <150 chars, unique, a-z \| 0-9                                             |
| `password`     | `str`      | required                                                                             |
| `first_name`   | `str`      | required for admin, <20 chars                                                        |
| `last_name`    | `str`      | < 20 chars                                                                           |
| `email`        | `str`      | required, <256 chars, unique, valid ("@")                                            |
| `phone_number` | `str`      | required, unique, format=`+12121235551234`                                           |
| `user_type`    | `str`      | set automatically for `'subscriber'` and `'admin'` currently                         |
| `is_active`    | `bool`     | set automatically                                                                    |
| `is_staff`     | `bool`     | set automatically                                                                    |
| `is_superuser` | `bool`     | set automatically                                                                    |
| `groups`       | `list`     | set automatically                                                                    |
| `permissions`  | `list`     | set automatically                                                                    |
| `created_at`   | `datetime` | set automatically                                                                    |
| `bio`          | `text`     | <2000 chars                                                                          |
| `avatar`       | `__file__` | automatically resized to 640x640/cropped from center -> out/formatted into a `'PNG'` |

### SongShareUserGroup
These are created programmatically

| field         | datatype | constraints |
|---------------|----------|-------------|
| `name`        | `str`    | *none*      |
| `description` | `str`    | *none*      |
| `permissions` | `list`   | *none*      |

### Article
| field           | datatype   | constraints                                                                            |
|-----------------|------------|----------------------------------------------------------------------------------------|
| `id`            | `int`      | auto-populated, incremental                                                            |
| `title`         | `str`      | <100 chars                                                                             |
| `author`        | `str`      | set automatically by logged in admin                                                   |
| `description`   | `text`     | < 1000 chars                                                                           |
| `article_image` | `__file__` | automatically resized to 1280x1280/cropped from center -> out/formatted into a `'PNG'` |
| `content`       | `text`     | *none*                                                                                 |
| `shares`        | `int`      | default=0, doesn't do anything yet                                                     |

---

## Endpoints
### Authorization
| name            | method | url                                        | function                                            |
|-----------------|--------|--------------------------------------------|-----------------------------------------------------|
| login           | `POST` | `/authorization/login/`                    | Get access & refresh tokens using user credentials. |
| refresh         | `POST` | `/authorization/login/refresh`             | Refresh session token (required every 5 minutes.    |
| register        | `POST` | `/authorization/register`                  | Register a new user (subscriber/artist only).       |
| change_password | `PUT`  | `/authorization/change_password/<int:pk>/` | Change password for user account.                   |
| update_profile  | `PUT`  | `/authorization/update_profile/<int:pk>/`  | Update profile details.                             |

### Users
| name   | method   | url                | function                         |
|--------|----------|--------------------|----------------------------------|
| list   | `GET`    | `/users/`          | Get a list of all users.         |
| list   | `POST`   | `/users/`          | Create a new user account.       |
|        |          |                    |                                  |
| detail | `GET`    | `/users/<int:pk>/` | Get a specific user account.     |
| detail | `PUT`    | `/users/<int:pk>/` | While logged in, update account. |
| detail | `DELETE` | `/users/<int:pk>/` | While logged in, delete account. |

### Articles
| name   | method   | url                   | function                                       |
|--------|----------|-----------------------|------------------------------------------------|
| list   | `GET`    | `/articles/`          | Get a list of all articles.                    |
| list   | `POST`   | `/articces/`          | While logged in as Admin, create a new artice. |
|        |          |                       |                                                |
| detail | `GET`    | `/artices<int:pk>/`   | Get a specific article.                        |
| detail | `PUT`    | `/artiles/<int:pk>/`  | While logged in as Admin, update article.      |
| detail | `DELETE` | `/articles/<int:pk>/` | While logged as Admin, delete article.         |

### Admin
| name       | method  | url                   | function      |
|------------|:-------:|-----------------------|---------------|
| admin site |    -    | `/songshareapiadmin/` | Admin portal. |
