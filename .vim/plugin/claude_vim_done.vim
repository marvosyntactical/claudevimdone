if !has('python3')
    echo "Error: This plugin requires Vim compiled with +python3"
    finish
endif

python3 << EOF
import sys
import vim
sys.path.append(vim.eval('expand("<sfile>:p:h:h")') + '/python')
import claude_vim_done
EOF

function! ClaudeVimDone()
    python3 claude_vim_done.generate_completion()
endfunction

function! ClaudeVimUndone()
    python3 claude_vim_done.undo_completion()
endfunction

" Map Ctrl-L to generate completion in normal mode
nnoremap <C-L> :call ClaudeVimDone()<CR>

" Map Ctrl-I to undo completion in normal mode
nnoremap <C-I> :call ClaudeVimUndone()<CR>
