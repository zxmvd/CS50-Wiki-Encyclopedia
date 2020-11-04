# An Wikipedia-like online encyclopedia

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

<a href="https://wiki-like.herokuapp.com/">Live Demo</a>