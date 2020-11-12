# These are example pseudo-codes for the reply and reply-all behavior
# in three email clients. The full evaluation is in tabular form in
# results.md.

class Thunderbird:
  # Thunderbird 68.4.2
  def reply(msg):
    # "Reply"-Button
    if msg.has("mail-reply-to"):
      compose(to=msg.get_all("mail-reply-to"))
    else if msg.has("reply-to"):
      compose(to=msg.get_first("reply-to"))
    else if msg.has("from"):
      compose(to=msg.get_all("from"))
    else:
      compose(to="")

  def reply_all(msg):
    # "Reply All"-Button
    # Note: In the special case that "from" is identical to the
    # imap account holder, BCC headers are also copied into the
    # draft email.
    if msg.has("mail-followup-to"):
      compose(to=msg.get_all("mail-followup-to"))
    else if msg.has("reply-to"):
      compose(to=msg.get_first("reply-to") + msg.get_all("to"),
              cc=msg.get_all("cc"))
    else if msg.has("from"):
      compose(to=msg.get_all("from") + msg.get_all("to"),
              cc=msg.get_all("cc"))
    else:
      compose(to="")

class Gmail:
  # Gmail 2020-02-11
  def reply(msg):
    # "Reply"-Button
    if msg.has("mail-followup-to"):
      compose(to=msg.get_all("mail-followup-to", "reply-to")
#    else if msg.has("mail-reply-to") and msg.has("reply-to"):
#      compose(to=msg.get_all("reply-to"))
    else if msg.has("reply-to"):
      compose(to=msg.get_all("reply-to"))
    else if msg.has("from"):
      compose(to=msg.get_all("from"))
    else if msg.has("resent-from"):
      compose(to=msg.get_first("resent-from"))
    else:
      compose(to="(unknown sender)")

  def reply_to_all(msg):
    # "Reply All"-Button. Note: The button is only
    # available if more than one email address would be replied to.
    if msg.has("mail-followup-to"):
      # FIXME: We get some inconsistent results with the cc.
      # Sometimes it is empty, sometimes it is populated like below.
      compose(to=msg.get_all("mail-followup-to", "reply-to"))
    # 2020-02-11: else if msg.has("mail-reply-to") and msg.has("reply-to"):
    # Retested on 2020-05-02
    else if msg.has("reply-to"):
      compose(to=msg.get_all("reply-to"),
              cc=msg.get_all("to", "apparently-to", "cc"))
    else if msg.has("from"):
      compose(to=msg.get_all("from"),
              cc=msg.get_all("to", "apparently-to", "cc"))
    else:
      # No "Reply All"-Button displayed.
      pass

class Aol:
  # AOL 2020-03-31
  def reply(msg):
    # "Reply"-Button
    if msg.has("reply-to"):
      compose(to=msg.get_all("reply-to"))
    else if msg.has("from"):
      compose(to=msg.get_first("from"))
    else:
      compose(to="")

  def reply_to_all(msg):
    # "Reply All"-Button
    if msg.has("reply-to"):
      compose(to=msg.get_all("reply-to", "to"),
              cc=msg.get_all("cc"))
    else if msg.has("from"):
      compose(to=msg.get_first("from") + msg.get_all("to"),
              cc=msg.get_all("cc"))
    else:
      compose(to=msg.get_all("to"),
              cc=msg.get_all("cc"))
