
- WSL-Terminal: https://github.com/goreliu/wsl-terminal
- FiraCode: https://github.com/tonsky/FiraCode
- Use FiraCode in PyCharm and enable ligatures
- oh-my-git: ```git clone https://github.com/arialdomartini/oh-my-git.git ~/.oh-my-git && echo source ~/.oh-my-git/prompt.sh >> ~/.bashrc```
- Edit oh-my-git config to use glyphs form FiraCode: 
    ```: ${omg_is_a_git_repo_symbol:='◉'}
    : ${omg_has_untracked_files_symbol:='☹'}
    : ${omg_has_adds_symbol:='+'}
    : ${omg_has_deletions_symbol:='-'}
    : ${omg_has_cached_deletions_symbol:='-'}
    : ${omg_has_modifications_symbol:='⌨'}
    : ${omg_has_cached_modifications_symbol:='⌨'}
    : ${omg_ready_to_commit_symbol:='⇪'}            #   →
    : ${omg_is_on_a_tag_symbol:='⌧'}                #   
    : ${omg_needs_to_merge_symbol:='┪'}
    : ${omg_detached_symbol:='╍'}
    : ${omg_can_fast_forward_symbol:='►'}
    : ${omg_has_diverged_symbol:=''}               #   
    : ${omg_not_tracked_branch_symbol:=''}
    : ${omg_rebase_tracking_branch_symbol:='♪'}     #   
    : ${omg_merge_tracking_branch_symbol:='♫'}      #  
    : ${omg_should_push_symbol:='⬆'}                #    
    : ${omg_has_stashes_symbol:='⇪'}```