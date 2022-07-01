## Install even moar stuff
[Awesome Mac](https://wangchujiang.com/awesome-mac/) has a list of like every tool you care about for every category, and has a good system to determine which things are FOSS vs Free vs Paid.

## Emojis
Mac Emoji Keyboard Shortcut: control + cmd + space

## Finder
you can run
```
defaults write com.apple.finder QuitMenuItem -bool YES && killall
```

Finder command in the Terminal, after that you can exit Finder with ⌘Q just like any other app. It won't help to remove Finder from the Dock though.

To revert, run:
```
defaults write com.apple.finder QuitMenuItem -bool NO && killall Finder
```

This is such a pain, right? Why does mac want its dock to look so cluttered?

https://github.com/jesscxc/hide-finder-trash-dock-icons
