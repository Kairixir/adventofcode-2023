" For NeoVim using Lua
" Could be transcribed in VimScript
" Substitutes characters for cards so they can be sorted with basic sort
" CHANGE from part1 -> changed substitution
:lua substitutions = {'T/B','J/1','Q/D','K/E','A/F'}
:lua for _, pattern in pairs(substitutions) do vim.api.nvim_exec("%s/" .. pattern .. "/g", true) end

" Rank each hand by its strongest comnination
" Implementation in separate script
:source part2-executable-highest-hand-ranking.vim

" Sort all by char value in descending order
:sort

" Give rank to each hand
%s/^/\=line('.').' '/


%s/^/\=line('.').' '/
%s/\v\d+ \zs.+\ze /*/g
2,$s/^/+/g
%J0C=-

" Tada
