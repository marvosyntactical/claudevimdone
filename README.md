# ClaudeVimDone()

A tiny plugin for Vim that does code completion on Keybind. 
Currently powered by Claude Sonnet.

The entire file that is in the current buffer is used as context, as well as its filename.
In a very small file, a ~20 line completion takes about 5 seconds for me.

# Setup

1. Copy ```.vim/plugin/claude\_vim\_done.vim``` to ```.vim/plugin/claude\_vim\_done.vim```.
2. Copy ```.vim/python/claude\_vim\_done.py``` to ```.vim/python/claude\_vim\_done.py```.
3. Put your Anthropic API key into a single line file at ```.vim/python/.anthropic_api_key```.
4. Run ```pip install anthropic```.
5. Restart Vim.

# Usage

1. Move the cursor to where you want the completion to begin. The following characters in the file will simply be replaced by the LLM's output. So you might want to make some space below where you want it to generate a big function.
2. Enter Normal Mode.
3. Press Ctrl L.
4. Wait a few seconds.
5. After the completion is done, carry on editing as normal.
6. If you want to undo the last completion, press Ctrl I.

# TODOs

* Async/Streaming Output directly, token by token.
* More interactivity?
* Get this on vundle
* Please open an issue for feature requests

