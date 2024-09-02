# ClaudeVimDone()

A tiny plugin for Vim that does code completion on Keybind. 
Currently powered by Claude Sonnet.

The entire file that is in the current buffer is used as context, as well as its filename.
In a very small file, a ~20 line completion takes about 5 seconds for me.

# Setup

Copy ```.vim/plugin/claude\_vim\_done.vim``` to ```.vim/plugin/claude\_vim\_done.vim```.
Copy ```.vim/python/claude\_vim\_done.py``` to ```.vim/python/claude\_vim\_done.py```.

Put your Anthropic API key into a single line file at ```.vim/python/.anthropic_api_key```.

Run ```pip install anthropic```.

Start vim.

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

