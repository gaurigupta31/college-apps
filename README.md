# Web Scraping

1. We have used Beautiful Soup to parse the HTML response from the HTTP GET request made to the URL entered. We make use of `lxml` which is a parser used with `bs4`
2. For each category, we find all instances of the keyword with the `find_all` function.
3. Different functions have been created for fetching different details regarding a program - `get_toefl`, `get_deadline` etc.

---

<!--
this script has been unit tested for 
https://www.si.umich.edu/programs/master-science-information/how-do-i-apply and
https://mhcid.washington.edu/admissions/
it's possible that the information provided might not map correctly every time
wip
-->