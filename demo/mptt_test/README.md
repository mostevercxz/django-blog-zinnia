== How to solve too much queries in managin some hierarchical data ? ==
Modified Preorder Tree Traversal,

Webpage : http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/

http://www.sitepoint.com/hierarchical-data-database/
== Mptt makes most tree operations much cheaper in terms of queries. ==
== Steps ==
- Add mptt to INSTALLED_APPS
- Define a model in models.py
- python manager.py syncdb
- python manager.py shell, create some data using Genre.objects.create(name='aaa', parent=bbb)
- Make a view function
- Add url in  urls.py
- Add a template

== Sqlite3 Commands Archive ==
- .tables, show tables
- .show, show environment variables
- .quit, quit the terminal
- .open localfile.sqllite3, open a local disk database
- .save local.sqlite3, save the database into a disk file
- create table table(one varchar(10), two smallint);
- insert into table values('hello', 10)
- select * from table
