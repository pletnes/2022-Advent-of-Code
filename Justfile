lint:
    black *.py

today:
    #!/usr/bin/env zsh
    fname="dec$(date '+%d').py"
    file_contents="from helpers import p, pp, inp\nfor line in inp():\n    ..."
    [[ -f "$fname" ]] || echo "$file_contents" > "$fname"
