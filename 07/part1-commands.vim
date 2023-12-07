" For NeoVim using Lua
" Could be transcribed in VimScript
" Substitutes characters for cards so they can be sorted with basic sort
:lua substitutions = {'T/B','J/C','Q/D','K/E','A/F'}
:lua for _, pattern in pairs(substitutions) do vim.api.nvim_exec("%s/" .. pattern .. "/g", true) end

" Sort all by char value in descending order
:sort

" Move lines matching $pattern to the end of file

" Set highest hand A
%s/^/A /g

" $pattern = pair = B
g/^.*\(.\).*\1.* /m$
:%s/^\zs[^ ]*\ze .*\(.\).*\1.* /B/

" $pattern = two pairs = C
g/^.*\(.\).*\(.\|\1\).*\(\1\|\2\).*\(\1\|\2\).* /m$
:%s/^\zs[^ ]*\ze .*\(.\).*\(.).*\(\1\|\2\).*\(\1\|\2\).* /C/
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\(.\).*\(\2\).* /C/

" $pattern = three of kind = D
g/^.*\(.\).*\1.*\1.* /m$
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\1.* /D/

" $pattern = full house = E
g/^.*\(.\).*\(.\).*\(\1\|\2\).*\(\1\|\2\).*\(\1\|\2\) /m$
:%s/^\zs[^ ]*\ze .*\(.\).*\(.\).*\(\1\|\2\).*\(\1\|\2\).*\(\1\|\2\) /E/

" $pattern = four of kind = F
g/^.*\(.\).*\1.*\1.*\1.* /m$
:%s/^\zs[^ ]*\ze..*\(.\).*\1.*\1.*\1.* /F/

" $pattern = five of kind = G
g/^.*\(.\).*\1.*\1.*\1.*\1.* /m$
:%s/^\zs[^ ]*\ze .*\(.\).*\1.*\1.*\1.*\1.* /G/

" Give rank to each hand
%s/^/\=line('.').' '/


%s/^/\=line('.').' '/
%s/\v\d+ \zs.+\ze /*/g
2,$s/^/+/g
%J0C=-

" Tada
