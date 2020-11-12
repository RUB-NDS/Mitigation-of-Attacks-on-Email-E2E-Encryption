Header Tests
============

We extracted the header names from four public mailing list archives
(November 2017) and generated an email where every of the 8095 headers
occurs twice in the following way (using plus addressing to pool all
replies in a single email account):

KEY: test+KEY-1@gmail.com
KEY: test+KEY-2@gmail.com

We filtered out the following keys and replaced them with fixed values
to distinguish the test cases and render them correctly:

content-transfer-encoding: 8bit
content-type: text/plain; charset=utf-8
content-disposition: inline
subject: HDR-001 All Headers

We did not correct or provide meaningful values to any of the other
8091 keys.

We then generated test cases to reverse engineer (with best effort)
the reply-to-author, reply-to-all and (if available) reply-to-list
logic of the email client.


1) Thunderbird 68.4.2:

function reply-to-author(msg):
  /* "Reply"-Button" */
  if header.has("mail-reply-to") then
    compose(to=header.get_all("mail-reply-to"))
  else if header.has("reply-to") then
    compose(to=header.get_first("reply-to"))
  else if header.has("from") then
    compose(to=header.get_all("from"))
  else
    compose(to="")

function reply-to-list(msg):
  /* "Reply All"-Button */
  if header.has("mail-followup-to") then
    compose(to=header.get_al("mail-followup-to"))
  else if header.has("reply-to") then
    compose(to=header.get_first("reply-to") + header.get_all("to"),
            cc=header.get_all("cc"))
  else if header.has("from") then
    compose(to=header.get_all("from") + header.get_all("to"),
            cc=header.get_all("cc"))
  else
    compose(to="")
