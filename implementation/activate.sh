# Use this with "bash --rcfile activate.sh"
source ~/.bashrc

export LD_LIBRARY_PATH=`pwd`/install/lib
export PATH=`pwd`/install/bin:$PATH
export PS1="\033[01;33m[DC-Demo]\033[00m $PS1"
export GNUPGHOME=`pwd`/home/gnupg

alias gpg="gpg --no-permission-warning"
echo "Using: `gpg --version | head -n 1` (`which gpg`)"
gpg --import dc-demo.keys

TB_PROFILE=`pwd`/home/thunderbird
alias thunderbird="thunderbird --profile ${TB_PROFILE} -purgecaches"

