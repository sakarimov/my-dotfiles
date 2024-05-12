from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

mod = "mod4"
terminal = "konsole"

keys = [
    # Switch between windows
    Key([mod, "mod1"], "Tab", lazy.widget["keyboardlayout"].next_keyboard()),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.reset()),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod],
        "Tab",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "a", lazy.spawn(
        'rofi -show combi -combi-modi "window,drun,ssh" -modi combi'), desc="spawn rofi"),

    Key([mod, "shift", "control"], "l", lazy.to_screen(0),
        desc="Move focus to left screen"),
    Key([mod, "shift", "control"], "h", lazy.to_screen(1),
        desc="Move focus to right screen"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"],
        "l",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),

    # My Own Keys
    Key([mod, "shift"], "Return", lazy.spawn(
        'qutebrowser'), desc="Launch web browser"),
    Key([mod, "shift", "control"], "Return", lazy.spawn(
        'qbpm choose'), desc="Launch web browser"),
    Key([mod, "shift"], "p", lazy.spawn("rofi-pass"), desc="Launch passmenu"),
    Key([mod, "shift"], "v", lazy.spawn(
        "rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"), desc="launch rofi-greenclip"),
    Key([mod, "shift"], "c", lazy.spawn(
        "rofi -show calc -modi calc -no-show-match -no-sort"), desc="launch rofi-calc"),
    Key([mod, "shift"], "s", lazy.spawn('flameshot gui'),
        desc="Launch screenshot software"),
    Key([mod, "control"], "x", lazy.spawn("xtrlock"),
        desc="lock the keyboard and mouse not the screen"),

    KeyChord(
        [mod], "w",
        [
            Key([], "b", lazy.spawn("firefox https://web.whatsapp.com/ https://teach.brightchamps.com/home https://www.academia.brightchamps.com/curriculum-v4 https://app.slack.com/client/T0447SESBT4/C04DWDWD95Z https://discord.com/channels/@me/1013010337991249953")),
            Key([], "z", lazy.spawn("bash /home/mxsulthan/xcompmgr.sh")),
            Key([], "a", lazy.spawn(
                "bash /home/mxsulthan/Downloads/teka/tekapoint.sh")),
            Key([], "n", lazy.spawn("vboxmanage startvm 'win10'")),
            #            Key([], "z", lazy.spawn("setxkbmap -layout ara")),
            #            Key([], "1", lazy.to_screen(0)),
            #            Key([], "2", lazy.to_screen(1)),
        ]
    )

]
