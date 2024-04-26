# ~/.bashrc

# common aliases
alias ls='eza'
alias ll='eza -lah' # show long listing of all except ".."
alias la='eza -A'
alias ~="cd ~/"
alias bashrc='nvim ~/.bashrc'
alias bashsrc='source ~/.bashrc'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

################################################################################

# common environment variables set
## add time info in history file
export HISTTIMEFORMAT="%d/%m/%y %T "
## make history file unlimitted
export HISTSIZE=-1
export HISTFILESIZE=-1
## avoid duplicates..
export HISTCONTROL=ignoredups:erasedups
## append history entries..
shopt -s histappend
## After each command, save and reload history
export PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"

## paths to export
export PATH=$HOME/.local/bin:/opt/cuda/bin:/bin/appimages${PATH:+:${PATH}}

## some additional softwares
export BROWSER='qutebrowser'
export EDITOR='nvim'
export VISUAL='nvim'

## hooks for direnv
eval "$(direnv hook bash)"
## replace cd with zoxide
eval "$(zoxide init --cmd cd bash)"

function pac-log {
	# Usage: pac-log [n=20]
	# show persisting installs/removes in last n lines of pacman.log (install X...remove X pairs and the converse are filtered out)
	{
		if [[ -e /var/log/pacman.log.1 ]]; then
			cat /var/log/pacman.log.1
		elif [[ -e /var/log/pacman.log.1.gz ]]; then
			zcat /var/log/pacman.log.1.gz
		fi
		cat /var/log/pacman.log
	} |
		rg '] installed|] removed' | tail -n "${1-20}" |
		python <(
			cat <<EOF

import sys, re
pkgre=re.compile(r'\[[^]]*\] (installed|removed) ([^ ]*) .*')
lines = []
hist = {
    'installed': {},
    'removed': {},
}
otheract = {
    'installed':'removed',
    'removed':'installed',
}
li=0
for l in sys.stdin:
    m = pkgre.match(l)
    if m:
        act,pkg = m.groups()
        hist[act].setdefault(pkg,[]).append(li)
        lines.append((li,act,pkg,l[:-1]))
        li+=1
for li,act,pkg,line in lines:
    if li==hist[act][pkg][-1] and li>hist[otheract[act]].get(pkg,-1):
      print ("%s" % (line,))
EOF
		)

}

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# NNN CONFIGS
## cd on quit
n() {
	[ "${NNNLVL:-0}" -eq 0 ] || {
		echo "nnn is already running"
		return
	}

	# The behaviour is set to cd on quit (nnn checks if NNN_TMPFILE is set)
	# If NNN_TMPFILE is set to a custom path, it must be exported for nnn to
	# see. To cd on quit only on ^G, remove the "export" and make sure not to
	# use a custom path, i.e. set NNN_TMPFILE *exactly* as follows:
	#      NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"
	export NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"

	# Unmask ^Q (, ^V etc.) (if required, see `stty -a`) to Quit nnn
	# stty start undef
	# stty stop undef
	# stty lwrap undef
	# stty lnext undef

	# The command builtin allows one to alias nnn to n, if desired, without
	# making an infinitely recursive alias
	command nnn -Gd "$@"

	[ ! -f "$NNN_TMPFILE" ] || {
		. "$NNN_TMPFILE"
		rm -f "$NNN_TMPFILE" >/dev/null
	}
}

[[ -r "/usr/share/z/z.sh" ]] && source /usr/share/z/z.sh

export NNN_FIFO=/tmp/nnn.fifo
export NNN_PLUG='c:fzcd;s:rsynccp;r:renamer;m:nmount;p:preview-tui;t:preview-tabbed'
export NNN_COLORS="#b1b1b1b1;5555"
export NNN_TERMINAL='konsole'

[[ -f $HOME/.aliases ]] && source $HOME/.aliases

# pnpm
export PNPM_HOME="/home/sulthan/.local/share/pnpm"
case ":$PATH:" in
*":$PNPM_HOME:"*) ;;
*) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# Set up Node Version Manager
source /usr/share/nvm/init-nvm.sh
