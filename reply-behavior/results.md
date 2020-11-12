# Decryption Context Research Log

## Accounts

dcheadertest@gmail.com
dcheadertest2@aol.com
dcheadertest2@outlook.com
decryptioncontext@outlook.com
decryptioncontext@yahoo.com
decryptioncontext@gmx.de
decryptioncontext@zohomail.com
decryptioncontext@aol.com
decryptioncontext@mail.ru
decryptioncontext@fastmail.com
decryptioncontext@hushmail.com
decryptioncontext@runbox.com
decryptioncontext@icloud.com

## Reply-Behaviour

### Thunderbird

See pseudo-code.py

### Gmail

See pseudo-code.py

Notes:
* Redirecting the large email causes a MaxSizeError.

### AOL (2020-03-31)

(Also see pseudo-code.py)

#### REPLY

1. `HDR-002 All Headers No CL`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`                |

2. `HDR-030 RTA No CL-RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |

3. `HDR-031 RTA No CL-RT-FROM`

Empty.

#### REPLY-ALL

1. `HDR-002 All Headers No CL`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`, `to-1`, `to-2`|
|cc       |`cc-1`, `cc-2`                            |

2. `HDR-030 RTA No CL-RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`,`to-1`,`to-2`                    |
|`cc`     |`cc-1`, `cc-2`                            |

3. `HDR-130 RTL No-RT-TO`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |
|cc       |`cc-1`, `cc-2`                            |

4. `HDR-131 RTL No-RT-TO-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|cc       |`cc-1`, `cc-2`                            |

#### Notes

* Actually sending the emails triggers spam detection,
  and the account will be blocked.
* `HDR-001 All Headers`: APPEND error due to content-length header

### Outlook.com (office365.com, 2020-03-31)

#### REPLY

1. `HDR-003 All Headers No CTE` (split version)

fehlt: 3,9,14

In the split version, we first collect all relevant headers.

|Split    |Header                                    |
|---------|------------------------------------------|
|7        |`from-2`                                  |
|14[1]    |`reply-to-1`,`reply-to-2`                 |
|15       |`sender-2`                                |

[1] After removing `resent-from` headers.

2. `HDR-004 All Headers Outlook`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`reply-to-1`,`reply-to-2`                 |

3. `HDR-040 RTA Outlook No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from-2`                                  |

4. `HDR-041 RTA Outlook No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`sender-2`                                |

5. `HDR-042 RTA Outlook No RT-FROM-SENDER`

Empty.

#### REPLY-ALL

1. `HDR-003 All Headers No CTE` (split version)

|Split    |Header                                    |
|---------|------------------------------------------|
|2        |`bcc-1`,`bcc-2`                           |
|3[1]     |`cc-1`,`cc-2`                             |
|7        |`from-2`                                  |
|14[2]    |`reply-to-1`,`reply-to-2`                 |
|15       |`sender-2`                                |
|17       |`to-1`,`to-2`                             |

[1] After removing `bounces-to` headers.
[2] After removing `resent-from` headers.

2. `HDR-004 All Headers Outlook`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`to-1`,`to-2`,`reply-to-1`,`reply-to-2`   |
|cc       |`cc-1`,`cc-2`                             |
|bcc      |`bcc-1`,`bcc-2`                           |

3. `HDR-040 RTA Outlook No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from-2`,`to-1`,`to-2`                    |
|cc       |`cc-1`,`cc-2`                             |
|bcc      |`bcc-1`,`bcc-2`                           |

4. `HDR-041 RTA Outlook No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`sender-2`,`to-1`,`to-2`                  |
|cc       |`cc-1`,`cc-2`                             |
|bcc      |`bcc-1`,`bcc-2`                           |

5. `HDR-042 RTA Outlook No RT-FROM-SENDER`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`to-1`,`to-2`                  |
|cc       |`cc-1`,`cc-2`                             |
|bcc      |`bcc-1`,`bcc-2`                           |

#### Notes

* All headers in total must not exceed approximately 10kB.
* keywords, x-message-flag are interpreted
* If bounces-to is present, the email is not shown in list.
* If any header starting with "list" is present,
  the email is not shown in the list.

### GMX (2020-04-01)

#### REPLY

1. `HDR-003 All Headers No CTE` (split version)

In the split version, we first collect all relevant headers.

|Split    |Header                                    |
|---------|------------------------------------------|
|7        |`from-2`                                  |
|14       |`reply-to-1`,`reply-to-2`                 |

2. `HDR-004 All Headers Outlook`

Gmx headers are a subset of Outlook.

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`reply-to-1`,`reply-to-2`                  |

3. `HDR-040 RTA Outlook No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from-2`                                  |

4. `HDR-041 RTA Outlook No RT-FROM`

Empty.

#### REPLY-ALL

1. `HDR-003 All Headers No CTE` (split version)

In the split version, we first collect all relevant headers.

|Split    |Header                                    |
|---------|------------------------------------------|
|3        |`cc-1`,`cc-2`                             |
|7        |`from-2`                                  |
|14       |`reply-to-1`,`reply-to-2`                 |
|17       |`to-1`,`to-2`                             |

2. `HDR-004 All Headers Outlook`

Gmx headers are a subset of Outlook.

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`reply-to-1`,`reply-to-2`                 |
|cc       |`to-1`,`to-2`,`cc-1`,`cc-2`               |

3. `HDR-040 RTA Outlook No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from-2`                                  |
|cc       |`to-1`,`to-2`,`cc-1`,`cc-2`               |

4. `HDR-041 RTA Outlook No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |""                                        |
|cc       |`to-1`,`to-2`,`cc-1`,`cc-2`               |

5. `HDR-160 Short No RT-FROM-TO-CC`

Empty.

### Mail.ru (2020-04-01)

#### REPLY

1. `HDR-005 All Headers Single FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`reply-to-1`,`reply-to-2`                 |

2. `HDR-050 Single FROM No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from`                                    |

3. `HDR-051 No RT-FROM`

Empty.  Sender is shown as "<Не указано>" (Not specified).

#### REPLY-ALL

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`reply-to-1`,`reply-to-2`                 |
|cc       |`cc-1`,`cc-2`,`to-1`,`to-2`               |

2. `HDR-050 Single FROM No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |`from`                                    |
|cc       |`cc-1`,`cc-2`,`to-1`,`to-2`               |

3. `HDR-051 No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|to       |                                          |
|cc       |`cc-1`,`cc-2`,`to-1`,`to-2`               |

4. `HDR-051 No RT-FROM-CC-TO`

Reply-all button is not shown.

#### Notes

* If there is more than one "from" header, the email appears to be
from "Invalid Address" and that is also used instead of `from` above.

### iMail 11.5 (3445.9.1)

#### REPLY

1. `HDR-001 All Headers` (split version)

|Split    |Header                                    |
|---------|------------------------------------------|
|7        |`from-1`                                  |
|14       |`reply-to-1`,`reply-to-2`                 |

2. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`                |

3. `HDR-021 RTA No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |


#### REPLY-ALL

1. `HDR-001 All Headers` (split version)

|Split    |Header                                    |
|---------|------------------------------------------|
|2        |`bcc-1`, `bcc-2`                          |
|3        |`cc-1`, `cc-2`                            |
|14       |`reply-to-1`,`reply-to-2`                 |
|17       |`to-1`,`to-2`                             |

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`                |
|`cc`     |`to-1`, `to-2`, `cc-1`, `cc-2`            |
|`bcc`    |`bcc-1`, `bcc-2`                          |

2. `HDR-021 RTA No RT`

|Header   |Value                                     |
<|---------|------------------------------------------|
|`to`     |`from-1`                                  |
|`cc`     |`to-1`, `to-2`, `cc-1`, `cc-2`            |
|`bcc`    |`bcc-1`, `bcc-2`                          |

### Outlook Microsoft Office Professional Plus 2016

#### REPLY

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`                |

2. `HDR-021 RTA No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |

3. `HDR-051 RTA No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`sender-1`                                |

#### REPLY-ALL

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `reply-to-2`, `to-1`, `to-2`|
|`cc`     |`cc-1`, `cc-2`                            |

2. `HDR-021 RTA No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`, `to-1`, `to-2`                  |
|`cc`     |`cc-1`, `cc-2`                            |

3. `HDR-051 RTA No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`sender-1`, `to-1`, `to-2`                |
|`cc`     |`cc-1`, `cc-2`                            |


### K9 Android

#### REPLY

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`                              |

2. `HDR-021 RTA No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |

3. `HDR-051 RTA No RT-FROM`

Empty.

#### REPLY-ALL

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`, `from-1`, `to-1`            |
|`cc`     |`cc-1`                                    |

2. `HDR-021 RTA No RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`, `to-1`                          |
|`cc`     |`cc-1`                                    |

3. `HDR-051 RTA No RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`to-1`                                    |
|`cc`     |`cc-1`                                    |

4. `HDR-150 No RT-FROM-CC-TO.eml`

Empty.

### Kmail 5.11.3 (Kubuntu 19.09)

#### REPLY (defaults to mailing list, and fallbacks to author)

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`mail-followup-to-1`                      |

to author:

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-1`                                 |

2. `HDR-020 RTA No MFT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-1`                                 |

3. `HDR-060 RTA No MFT-R`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`                              |

4. `HDR-061 RTA No MFT-R-RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |

5. `HDR-063 RTA No MFT-R-RT-FROM`

Empty.

#### REPLY-ALL

1. `HDR-001 All Headers`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-1`                                 |
|`cc`     |`to-1`, `cc-1`                            |

2. `HDR-060 RTA No MFT-R`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`                              |
|`cc`     |`to-1`, `cc-1`                            |

3. `HDR-061 RTA No MFT-R-RT`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |
|`cc`     |`to-1`, `cc-1`                            |

4. `HDR-062 RTA No MFT-R-RT-FROM`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`to-1`                                    |
|`cc`     |`cc-1`                                    |

5. `HDR-063 RTA No MFT-R-RT-FROM-TO`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`cc-1`                                    |

6. `HDR-064 No MFT-R-RT-FROM-TO-CC`

Empty.

#### iPhone

##### REPLY

1. `HDR-090 iphone.eml`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`                              |

2. `HDR-091 iphone.eml`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |


3. `HDR-092 iphone.eml`

Empty.

##### REPLY ALL

1. `HDR-090 iphone.eml`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`reply-to-1`                              |
|`cc`     |`to-1`, `cc-1`                            |

2. `HDR-091 iphone.eml`

|Header   |Value                                     |
|---------|------------------------------------------|
|`to`     |`from-1`                                  |
|`cc`     |`to-1`, `cc-1`                            |

3. `HDR-092 iphone.eml`

|Header   |Value                                     |
|---------|------------------------------------------|
|`cc`     |`to-1`, `cc-1`                            |
