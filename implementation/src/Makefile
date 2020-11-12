BASE = ${CURDIR}/..
INSTALL_DIR = ${BASE}/install
LIBDIR = ${INSTALL_DIR}/lib
BINDIR = ${INSTALL_DIR}/bin

ENV = LD_LIBRARY_PATH=${LIBDIR} PATH=${BINDIR}:$$PATH

CONFIG_OPTS = --enable-maintainer-mode --prefix=${BASE}/install

CLEAN = git reset --hard; git clean -x -f -d

.PHONY: libgpg-error npth libgcrypt libksba libassuan gnupg enigmail
all: libgpg-error npth libgcrypt libksba libassuan gnupg enigmail

.PHONY: clean
clean:
	(cd libgpg-error; $(CLEAN))
	(cd npth; $(CLEAN))
	(cd libgcrypt; $(CLEAN))
	(cd libksba; $(CLEAN))
	(cd libassuan; $(CLEAN))
	(cd gnupg; $(CLEAN))

libgpg-error/configure:
	(cd libgpg-error; ${ENV} autoreconf)

libgpg-error/Makefile: libgpg-error/configure
	(cd libgpg-error; ${ENV} ./configure $(CONFIG_OPTS))

libgpg-error/src/.libs/libgpg-error.la: libgpg-error/Makefile
	${ENV} make -C libgpg-error -j8

${LIBDIR}/libgpg-error.la: libgpg-error/src/.libs/libgpg-error.la
	${ENV} make -C libgpg-error install

libgpg-error: ${LIBDIR}/libgpg-error.la


npth/configure:
	(cd npth; ${ENV} autoreconf)

npth/Makefile: npth/configure
	(cd npth; ${ENV} ./configure $(CONFIG_OPTS))

npth/src/.libs/libnpth.la: npth/Makefile
	${ENV} make -C npth -j8

${LIBDIR}/libnpth.la: npth/src/.libs/libnpth.la
	${ENV} make -C npth install

npth: ${LIBDIR}/libnpth.la


libgcrypt/configure:
	(cd libgcrypt; ${ENV} autoreconf)

libgcrypt/Makefile: libgcrypt/configure
	(cd libgcrypt; ${ENV} ./configure $(CONFIG_OPTS))

libgcrypt/src/.libs/libgcrypt.la: libgcrypt/Makefile
	${ENV} make -C libgcrypt -j8

${LIBDIR}/libgcrypt.la: libgcrypt/src/.libs/libgcrypt.la
	${ENV} make -C libgcrypt install

libgcrypt: ${LIBDIR}/libgcrypt.la


libksba/configure:
	(cd libksba; ${ENV} autoreconf)

libksba/Makefile: libksba/configure
	(cd libksba; ${ENV} ./configure $(CONFIG_OPTS))

libksba/src/.libs/libksba.la: libksba/Makefile
	${ENV} make -C libksba -j8

${LIBDIR}/libksba.la: libksba/src/.libs/libksba.la
	${ENV} make -C libksba install

libksba: ${LIBDIR}/libksba.la


libassuan/configure:
	(cd libassuan; ${ENV} autoreconf)

libassuan/Makefile: libassuan/configure
	(cd libassuan; ${ENV} ./configure $(CONFIG_OPTS))

libassuan/src/.libs/libassuan.la: libassuan/Makefile
	${ENV} make -C libassuan -j8

${LIBDIR}/libassuan.la: libassuan/src/.libs/libassuan.la
	${ENV} make -C libassuan install

libassuan: ${LIBDIR}/libassuan.la


gnupg/configure:
	(cd gnupg; ${ENV} autoreconf)

gnupg/Makefile: gnupg/configure
	(cd gnupg; ${ENV} ./configure $(CONFIG_OPTS))

gnupg/g10/gpg: gnupg/Makefile
	(cd gnupg; git am -3 ../../patches/gnupg/0001-Implement-decryption-context.patch)
	(cd gnupg; git am -3 ../../patches/gnupg/0002-Correctly-output-AEAD-decryption-error-on-the-status.patch)
	${ENV} make -C gnupg -j8

${BINDIR}/gpg: gnupg/g10/gpg
	${ENV} make -C gnupg install

gnupg: ${BINDIR}/gpg


enigmail/config.status:
	(cd enigmail; ./configure)

enigmail: enigmail/config.status
	(cd enigmail; git am -3 ../../patches/enigmail-2.0.8/0001-Support-decryption-context-in-account-settings.patch)
	(cd enigmail; git am -3 ../../patches/enigmail-2.0.8/0002-Support-decryption-context-in-PGP-MIME-encryption-an.patch)
	make -C enigmail -j8
	mkdir -p home/thunderbird/extensions
	echo "${BASE}/src/enigmail/build/dist" > home/thunderbird/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
