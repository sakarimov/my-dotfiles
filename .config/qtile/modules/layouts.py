from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.MonadTall(
        margin=4,
        border_focus='#5294e2',
        border_normal='#2c5380'),
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
    # layout.Matrix(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
    # layout.MonadTall(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
    # layout.MonadWide(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
    # layout.RatioTile(
    #    margin=[4,0,4,4],
    #    border_focus='#5294e2',
    #    border_normal='#2c5380'),
    # layout.Tile(
    #    margin=[4,0,4,4],
    #    border_focus='#5294e2',
    #    border_normal='#2c5380'),
    # layout.TreeTab(
    #    margin=4,
    #    active_bg='#5294e2',
    #    inactive_bg='#2c5380',
    #    panel_width=50,
    #    previous_on_rm=True,
    #    font='mono'),
    # layout.VerticalTile(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
    # layout.Zoomy(margin=8, border_focus='#5294e2', border_normal='#2c5380'),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='blueman-manager'),  # ssh-askpass
    Match(wm_class='pavucontrol'),  # ssh-askpass
    # Match(wm_class='zoom'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='Welcome v24.5-1'),  # gitk
    Match(title='Blender Launcher'),  # gitk
    Match(title='Settings'),  # gitk
    Match(wm_class='Blender_Launcher'),  # GPG key password entry
    Match(wm_class='Pinentry-gtk-2'),  # GPG key password entry
    Match(wm_class='zenity'),  # GPG key password entry
    Match(wm_class='obs'),  # GPG key password entry
    Match(wm_class='ferdium'),  # GPG key password entry
])
