class Book(object):
	author = ""
	title = ""
		
	def __init__(self,author,title):
		self.author = author
		self.title = title
		
	def display(self):
		y = "%s written by %s" % (self.title,self.author)
		print y
		
book1 = Book("Harper Lee", "To Kill a Mockingbird")

book2 = Book("John Steinbeck", "Of Mice and Men")

book1.display()
book2.display()
