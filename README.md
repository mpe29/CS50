# CS50w-edX: Web Programming
Online course through edX and Harvard with focus on web programming.
Brian Yu: brian@cs50.harvard.edu

Introduced to loads of different aspects to web development such as:
-- SQL, Django, Servers, Git, CSS, HTML, JavaScript, security etc --

# Lecture 0: Git - Version Control [26 March 2019]
https://cs50.harvard.edu/web/2019/spring/notes/0/
Sycronizez working together process over the internet 
Good for testing changes and experiment
Maintains version control 
DOM = Document Object Model 
	this is the structure of the HTML or JSON etc
CSS = Cascading style sheet
	good for adding a bit of style
	# in CSS refers to ID
		must be UNIQUE otherwise it just like class reference .
	. in CSS refers to class
		may not be UNIQUE
	you can include both an ID and a CLASS to some tag
GitHub Pages can enable you deploy to the internet!

# Lecture 1: HTTP and CSS - Web Dev [27 March 2019]
https://cs50.harvard.edu/web/2019/spring/notes/1/
Git features to know include:
	push, pull, checkout, commit -m, commit -am, branch, branch []
	Branching:
		New branches are entire new clones of the repository not just a single file. 
		However GIT does this in a unique way by not copying everything but rather 
		logs changes and wokrs backwards to generate old versions.
		Also when the term ORIGIN comes up it generally refers to the master repository
	Remote: 
		git fetch is used to get an updated version of the master/origin repo on GitHUB
		thus Origin and Origin/Master are not the same thing. One may be further in from
		of others.
	Fork: 
		This is a non invasive branching for generally open source 
	Pull requests:
		Ask someone to pull thier stuff into the master 
Linking HTML:
	href[]
With CSS:
	ol li
		this reference without the , operator creates a focus on descendents rather than 
		selecting both ol and li. ol = ordered list and li = list item.
	ol > li selects only immediate childred!
Pseudo classes ":"" 
	activated with HOVERING for example
Pseudo elements "::"
	SELECTION for example can change colours when selected or hilighted
	also one can use BEFORE and AFTER	
Responsive Design: Making sure it looks good accross platfroms, screens etc.
	Media Query - lets you specifc min and max extents of the page 
Bootstrap: Style without to teadiousness yaay
https://getbootstrap.com/
Variables in CSS: SASS
	Browsers cannot reas SASS directly and so SCSS files need to be designed and then 
	compiled by SASS in terminal into a CSS file that the final HTML file can read
	and so eaxch time the SASS file is changes you need to compile it to see results
	Sass cna also watch the file so you dont need to recompile each time
	
# Lecture 2: FLask [27 March 2019]
https://cs50.harvard.edu/web/2019/spring/notes/2/
Discussing python and server communications with HTTP communications 
Specifically using FLASK as a microframework
http://flask.pocoo.org/docs/1.0/quickstart/
http://flask.pocoo.org/docs/dev/cli/
	When running a flask server, it is essential to use the EXPORT command to ensure that the specific file is being targeted. Then one can use the FLASK RUN command.
	Also DEBUGGER mode is good for constant update to the resver. 

# Lecture 3: SQL [5 April 2019]
SQL:
	race conditions and SQL injection can be a way to take a advantage of you DB
	use transactions
	SQLAlchemy: Connects SQL and python


