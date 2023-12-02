for line in $(cat mapping.txt); do sed -i -e "s/${line%%,*}/${line##*,}/g" part2-solution.txt; done
