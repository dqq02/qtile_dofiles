# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import socket
import subprocess
from libqtile.config import Click, Drag, Group,  Key, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
mod2 = "mod1"
myTerm = "alacritty"      # My terminal of choice
myBrowser = "google-chrome-stable"  # My browser of choice

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm+" -e zsh"),
        desc='Launches My Terminal'
        ),
    Key([mod], "d",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Run Launcher'
        ),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='Google Chrome'
        ),
    Key([mod, "shift"], "q",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        desc='Restart Qtile'
        ),
    Key([mod], "r",
        lazy.spawn(myTerm+" -e ranger"),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "Delete",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key([mod2], "Tab",
        lazy.layout.next(),
        desc='Toggle through layouts'
        ),

    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    Key([mod], 'space', lazy.widget['keyboardlayout'].next_keyboard(), 
        desc='Next keyboard layout.'
        ),
    # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
]

groups = [Group(" 1 ", layout='monadtall'),
          Group(" 2 ", layout='monadtall'),
          Group(" 3 ", layout='monadtall'),
          Group(" 4 ", layout='monadtall'),
          Group(" 5 ", layout='monadtall'),
          Group(" 6 ", layout='monadtall'),
          Group(" 7 ", layout='monadtall'),
          Group(" 8 ", layout='monadtall'),
          Group(" 9 ", layout='monadtall'),
          Group(" 0 ", layout='monadtall')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": '#13315c',
                "border_normal": "#1D2330"
                }
layouts = [
    layout.MonadTall(**layout_theme),
]

colors = [["#1B1D24", "#1B1D24"],  # panel background
          # background for current screen tab
          ["#434758", "#434758"],
          ["#ffffff", "#ffffff"],  # font color for group names
          # border line color for current tab
          ["#bc13fe", "#bc13fe"],  # Group down color
          # border line color for other tab and odd widgets
          ["#8d62a9", "#8d62a9"],
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#e1acff", "#e1acff"],  # window name
          ["#000000", "#000000"],
          ["#AD343E", "#AD343E"],
          ["#f76e5c", "#f76e5c"],
          ["#F39C12", "#F39C12"],
          ["#F7DC6F", "#F7DC6F"],
          ["#f1ffff", "#f1ffff"],
          ["#4c566a", "#4c566a"], ]


#BLU
blu = [
    ["#0b2545", "#0b2545"],  # 1
    ["#13315c", "#13315c"],  # 2
    ["#134074", "#134074"],  # 3
    ["#8da9c4", "#8da9c4"],  # 4
    ["#eef4ed", "#eef4ed"],  # 5
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Nerd Font",
    fontsize=14,
    # padding=0,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    '''
    Function that returns the desired widgets in form of list
    '''
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            background=colors[0],
            foreground=colors[12],
            padding=0,
            fontsize=20
        ),
        widget.Sep(
            linewidth=0,
            padding=5,
            foreground='#ffffff',
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Nerd Font",
            fontsize=12,
            margin_y=2,
            margin_x=4,
            padding_y=2,
            pading_x=3,
            borderwidth=3,
            active=colors[-2],
            inactive=colors[-1],
            center_aligned = True,
            # rounded=True,
            rounded=False,
            # highlight_color=colors[4],
            # highlight_method="line",
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[7],
            this_current_screen_border=colors[5],
            # this_screen_border=colors[4],
            # other_current_screen_border=colors[0],
            # other_s5reen_border=colors[0],
            foreground=colors[0],
            background=colors[0],
            disable_drag=True
        ),
        widget.Prompt(
            prompt=lazy.spawncmd(),
            font="Ubuntu Nerd Font",
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),
        widget.Sep(
            linewidth=0,
            padding=12,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            fontsize=14,
            foreground=colors[12],
            background=colors[0],
            padding=80
        ),
        widget.CPU(
            fontsize=14,
            format=' {load_percent}%',
            foreground=colors[2],
            background=colors[0],
            padding=0,
            update_interval = 1.0
        ),
        # 
        # widget.TextBox(
        #     text='',
        #     background=colors[0],
        #     foreground=blu[4],
        #     padding=-14,
        #     fontsize=40
        # ),
        widget.Memory(
            foreground=colors[2],
            background=colors[0],
            format='﬙ {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            padding=20
        ),
        # widget.TextBox(
        #     text='',
        #     background=colors[11],
        #     foreground=colors[10],
        #     padding=-7,
        #     fontsize=44
        # ),
        # widget.TextBox(
        #     text="  ",
        #     foreground=colors[0],
        #     background=colors[10],
        #     padding=0
        # ),
        # widget.Volume(
        #     foreground=colors[0],
        #     background=colors[10],
        #     padding=5
        # ),
        # widget.TextBox(
        #     text='',
        #     foreground=blu[3],
        #     background=blu[4],
        #     padding=-7,
        #     fontsize=54
        # ),
        # widget.TextBox(
        #     text='',
        #     background=blu[3],
        #     foreground=blu[2],
        #     padding=-7,
        #     fontsize=44
        # ),
        # widget.TextBox(
        #     text='',
        #     foreground=blu[1],
        #     background=blu[2],
        #     padding=-7,
        #     fontsize=44
        # ),
        widget.Clock(
            foreground=colors[2],
            background=colors[0],
            format=" %H:%M  ",
            padding=0
        ),
        widget.TextBox(
            text='',
            foreground=colors[2],
            background=colors[0],
            padding=3,
            fontsize=16
        ),
        widget.KeyboardLayout(
            configured_keyboards=['us','ru'],
            foreground=colors[2],
            background=colors[0],
            fmt='{}',
            padding=3
        ),
       # widget.Net(
       #     foreground=colors[2],
       #     background=colors[0],
       #     padding=10,
       #     prefix='M'
       # ),
        #  widget.TextBox(
        #     text="  ",
        #     foreground=colors[2],
        #     background=colors[0],
        #     padding=0
        # ),
        # widget.Volume(
        #     foreground=colors[2],
        #     background=colors[0],
        #     padding=5
        # ),
        widget.Systray(
            foreground=colors[2],
            background=colors[0],
            padding=10
        ),
        # widget.TextBox(
        #     text='',
        #     foreground=colors[0],
        #     background=colors[1],
        #     padding=-7,
        #     fontsize=44
        # ),
        # widget.Net(
        #     interface="",
        #     format='Net: {down} ↓↑ {up}',
        #     foreground=colors[1],
        #     background=colors[3],
        #     padding=5
        # ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=24)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=24)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=24))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
