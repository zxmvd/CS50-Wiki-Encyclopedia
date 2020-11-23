# An Wikipedia-like online encyclopedia

<a href="https://wiki-like.herokuapp.com/" target="_blank">Live Demo</a>
## Intro
This is a project from CS50's Web Programming with Python and JavaScript course.

In the distribution code is a Django project called wiki that contains a single app called encyclopedia.


You'll see the sidebar containing:
- Search: 
  - Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
  - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
  - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.

- Create
  - You can add new page.

- Random page 
  - Will simply return a random page from all pages. 
  
In the main area you'll see the title of all pages. You can click on any of these pages and it will direct you to the page displaying the content of the title.

Entries are stored using Markdown (a markup language), which makes entries more human-friendly to write and edit. It is converted into HTML before displaying it to the user.

 - In <a href="encyclopedia/urls.py">encyclopedia/urls.py</a> the URL configuration for this app is defined.
 - In <a href="encyclopedia/views.py">encyclopedia/views.py</a> functions will return results to the web browser.
 - In <a href="encyclopedia/templates/encyclopedia">encyclopedia/templates/encyclopedia/</a> are templates inheriting from a base layout.html file.
 - CSS is in <a href="encyclopedia/static/encyclopedia/styles.css">encyclopedia/static/encyclopedia/</a>.
