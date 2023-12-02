# CLI commands, not script!

for line in $(cat mapping.txt); do STRING+=" -e \"s/${line%%,*}/${line##*,}/g\""; done; echo $STRING
eval "sed -i \"\" $STRING part2-alternative-solution.txt"
