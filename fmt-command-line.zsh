# Autoformats long command lines in zsh. Splits lines at a certain length and
# appends the necessary endline '\' to keep it valid. Great for debugging long
# build commands.
#
# By default bound to <leader>f.
#
# autoload fmt-command-line
# zle -N fmt-command-line
# bindkey -M vicmd f fmt-command-line

export __PRETTY_CMD_DIR=${0:A:h}

function fmt-command-line() {
  local tmpfile=${TMPPREFIX:-/tmp/zsh}ecl$$
  print -R - "$PREBUFFER$BUFFER" | $__PRETTY_CMD_DIR/pretty_cmd.py > $tmpfile
  print -z - "$(<$tmpfile)" 
  command rm -f $tmpfile
  zle send-break
}

autoload fmt-command-line
zle -N fmt-command-line
bindkey -M vicmd f fmt-command-line
