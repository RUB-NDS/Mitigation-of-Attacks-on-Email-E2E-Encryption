# NOTE

We can not distribute the account credentials for the test accounts
used with the various email providers.  For that reason, we do not
distribute the thunderbird configuration files.

To make the repository self-contained and keep it small, we also
removed the submodules for the upstream source code (git-modules.txt).

# Demonstrator for Decryption Contexts

This project includes patches for Thunderbird/Enigmail and GnuPG, demonstrating how to use the decryption context countermeasure against EFAIL [1] and Reply-To direct exfiltration attacks, as described in our paper [2].

[1] https://www.efail.de/
[2] https://dl.acm.org/doi/10.1145/3372297.3417878

Note: Emails generated with this software are **not** readable by other OpenPGP implementations that do not support the decryption context mechanism.

## Building

```
$ make shell
$ thunderbird
```

## Associated Data for OpenPGP

This version of GnuPG implements the draft standard "Associated Data for OpenPGP" in the following way:

```
$ gpg --force-aead --encrypt --associated-data <DATA> -r RECIPIENT
```

This command uses the provided associated data during encryption.  All the usual encryption flags are supported.

```
$ gpg --force-aead --decrypt --associated-data <DATA>
```

This command uses the provided associated data during decryption.  Decryption will fail if the data is missing or does not match the data used at encryption time.

Currently, only AEAD mode is supported.  For RFC4880 (legacy), we plan to use HMAC as a KDF.  For symmetric encryption, you can simply include the
associated data in the passphrase, separated with a static delimiter, so no special support is necessary.

If your data is binary, use any type of ASCII encoding before invoking GnuPG (Base-64, z32, hexadecimal, etc.).

## Limitations

Due to limitations in the Thunderbird extension API, we currently do not support characters outside of 7bit ASCII.  The reason is that the internal decoding does not produce the correct UTF-8 output.

## Notes

- Thundebird/Gmail needs "general.useragent.compatMode.firefox" set to true in the config editor (due to OAuth).
