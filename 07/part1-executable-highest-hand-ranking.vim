" Set highest hand A
%s/^/A /g

" $pattern = pair = B
:%s/^\zs[^ ]*\ze .*\(.\).*\1.* /B/

" $pattern = two pairs = C
:%s/^\zs[^ ]*\ze .*\(.\).*\(.\).*\(\1\|\2\).*\(\1\|\2\).* /C/
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\(.\).*\(\2\).* /C/

" $pattern = three of kind = D
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\1.* /D/

" $pattern = full house = E
:%s/\v^\zs[^ ]*\ze (.)(.)(\1|\2)(\1|\2)(\1|\2) /E/
:%s/\v^\zs[^ ]*\ze (.)\1(.)(\1|\2)(\1|\2) /E/
:%s/\v^\zs[^ ]*\ze (.)\1\1(.)\2 /E/

" $pattern = four of kind = F
:%s/^\zs[^ ]*\ze..*\(.\).*\1.*\1.*\1.* /F/

" $pattern = five of kind = G
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\1.*\1.*\1.* /G/
