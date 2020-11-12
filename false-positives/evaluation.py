from os import path
from itertools import product
from email.parser import BytesParser
from email.message import Message
import logging

def file_check(fname):
    if not path.exists(fname):
        logging.warning("Missing file: %s", fname)

def compare_payloads(pl1, pl2):
    if type(pl1) != type(pl2):
        return False
    elif isinstance(pl1, list):
        if len(pl1) != len(pl2):
            return False
        return [compare_payloads(p1, p2) for p1, p2 in zip(pl1, pl2)]
    elif isinstance(pl1, Message):
        # FIXME: Header
        return compare_payloads(pl1.as_string(), pl2.as_string())
    else:
        return pl1 == pl2

clients = ["gmail", "outlook", "yahoo", "gmx", "zoho", "icloud",
           "aol", "hushmail", "fastmail", "mailbox", "mailru", "runbox"]

groups = ["simple", "pgp-mime"]
directions = ["inbound", "outbound", "internal"]
emails = ["{0:02d}-{1}.eml".format(idx + 1, fname) for idx, fname in
           enumerate(clients)]

testcases = zip(product(groups, directions, ["send"], emails),
                product(groups, directions, ["recv"], emails))

for send, recv in testcases:
    group, direction, _, email = send
    ifn = path.join(*send)
    ofn = path.join(*recv)
    file_check(ifn)
    file_check(ofn)

    bp = BytesParser()
    
    with open(ifn, "rb") as ifh:
        im = bp.parse(ifh)
    with open(ofn, "rb") as ofh:
        om = bp.parse(ofh)

    print("-----------------------------------------------------")
    print("Testcase: {}, {}, {}".format(group, direction, email))

    imhk = set(im.keys())
    omhk = set(om.keys())
    print ("Add Header: ", repr(sorted(omhk.difference(imhk))))
    print ("Del Header: ", repr(sorted(imhk.difference(omhk))))
    mod_header = set()
    for k in imhk.intersection(omhk):
        if im[k] != om[k]:
            mod_header.add(k)
    print ("Mod Header: ", repr(sorted(mod_header)))
    for k in mod_header:
        print ("-%s: %r" % (k, im[k]))
        print ("+%s: %r" % (k, om[k]))
            
    body_eq = compare_payloads(im.get_payload(), om.get_payload())
    print("Body: ", body_eq)
    if not body_eq:
        print("Body Send: ",
              im.get_payload())
        print("Body Recv: ",
              om.get_payload())
