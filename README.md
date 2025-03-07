# Media Hotkeys Plugin

This plugin adds media hotkey support to your application, allowing you to control playback using keyboard shortcuts. Specifically, it maps the `F10` key to play the next song.

## Features

- **Next Track**: Press `F10` to skip to the next track in the playlist.

## Installation

1. Clone this repository or download the plugin files:
   ```bash
   git clone https://github.com/mervick/media-hotkeys.git
   ```

2. Copy the plugin to the appropriate directory for your application. For Rhythmbox, this would typically be:
   ```bash
   cp -r media-hotkeys ~/.local/share/rhythmbox/plugins/
   ```

3. Enable the plugin in your application:
   - Open Rhythmbox (or your application).
   - Go to `Preferences` > `Plugins`.
   - Find `Media Hotkeys` in the list and enable it.

## Configuration

Currently, the plugin is configured to use the `F10` key for the "next" action. You can modify the key bindings by editing the `do_activate` method in the `MediaHotkeysPlugin` class.

```python
app.set_accels_for_action("win.next", ["F10"])
```

Replace `"F10"` with your desired key combination.
