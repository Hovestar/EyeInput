#!/usr/bin/python2
import smtplib
import getpass

class Email(smtplib.SMTP):
	def __init__(self, username,password):
		smtplib.SMTP.__init__(self,"smtp.gmail.com:587")
		self.username = username
		self.password = getpass.getpass("What is your password? ")
		self.ehlo()
		self.starttls()
		self.login(self.username,self.password)
	def SendEmail(self,to,subject,body):
		msg = "\r\n".join([
			"From: "+self.username,
			"To: "+to,
			"Subject: "+subject,
			"",
			body
		])
		self.sendmail(self.username,to,msg)
	def __del__(self):
		self.quit()


# Note: This function definition needs to be placed
#       before the previous block of code that calls it.
def process_mailbox(M):
  rv, data = M.search(None, "ALL")
  if rv != 'OK':
	  print "No messages found!"
	  return

  for num in data[0].split():
	  rv, data = M.fetch(num, '(RFC822)')
	  if rv != 'OK':
		  print "ERROR getting message", num
		  return

	  msg = email.message_from_string(data[0][1])
	  print 'Message %s: %s' % (num, msg['Subject'])
	  print 'Raw Date:', msg['Date']
	  date_tuple = email.utils.parsedate_tz(msg['Date'])
	  if date_tuple:
		  local_date = datetime.datetime.fromtimestamp(
			  email.utils.mktime_tz(date_tuple))
		  print "Local Date:", \
			  local_date.strftime("%a, %d %b %Y %H:%M:%S")
if __name__=="__main__":
	username = "mercurymadman@gmail.com"
	password = getpass.getpass()
	"""
	em = Email(username)
	to = "sethhovestol@gmail.com"
	em.SendEmail(to,"This is a test","Did it work?")
	"""

	import sys
	import imaplib
	import getpass
	import email
	import datetime

	M = imaplib.IMAP4_SSL('imap.gmail.com')
	try:
		M.login(username, password)
	except imaplib.IMAP4.error:
		print "LOGIN FAILED!!! "
		exit(0)
	rv, mailboxes = M.list()
	if rv == 'OK':
		print "Mailboxes:"
		print mailboxes
	rv, data = M.select("Top Secret/PRISM Documents")
	if rv == 'OK':
		print "Processing mailbox...\n"
		process_mailbox(M) # ... do something with emails, see below ...
		M.close()
	M.logout()
