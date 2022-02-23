Tabs = '''
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu
#:import MDExpansionPanelLabel kivymd.uix.expansionpanel.MDExpansionPanelLabel 
#:import MDExpansionPanelThreeLine kivymd.uix.expansionpanel.MDExpansionPanelThreeLine


MDBoxLayout:
    orientation: "vertical"

    MDTabs:
        id: tabs
        tab_indicator_type: "round"
        tab_indicator_anim: True
        default_tab: 1
        tab_hint_x: True
        on_tab_switch:  app.on_tab_switch(*args)
        allow_strech:   True
        tab_indicator_height: "0dp"
        indicator_color: 0.9922, 1, 0.9608, 0.5




<Check@MDCheckbox>:
    group: 'group'
    size_hint:  None, None
    size: dp(48), dp(48)

<InfoTab>

    MDLabel:
        pos_hint:  {'center_x': .5, 'center_y': .7}
        text:   "developed by Tzvi Gershanik, Itay Levin & Sagi Chen."
        font_size:  12
        halign: "center"

    Image:
        source: "images/2BarG.png"
        pos_hint: {"center_x": 0.5, "center_y":0.8}

    MDCard:
        orientation: "vertical"
        padding: "15dp"
        focus_behavior: True
        size_hint: None, None
        size: "400", "380dp"
        pos_hint: {"center_x": .5, "center_y": .4}

        MDLabel:
            text: "About DFL"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "2dp"

        MDLabel:
            halign: "justify"
            text: app.about_dfl

<ParametersTab>

    MDCard:
        orientation: "vertical"
        padding: "15dp"
        focus_behavior: True
        size_hint: None, None
        size: "270", "400dp"
        pos_hint: {"center_x": .5, "center_y": .335}

        MDLabel:
            text: "Signal Processing & Analysis"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "2dp"

        MDLabel:
            halign: "justify"
            text: app.guide

    MDRoundFlatIconButton:
        icon: "folder-open"
        text: "Set Path Folder"
        pos_hint: {'center_x': 0.825, 'center_y': 0.38}
        size_hint: None, None
        size: 203, 30
        font_style: 'Button'
        font_size: 15
        on_release: app.open_channel_dialog() 

    MDRoundFlatIconButton:
        icon: "arch"
        text: "Set as Default"
        pos_hint: {'center_x': 0.825, 'center_y': 0.25}
        size_hint: None, None
        size: 203, 30
        font_style: 'Button'
        font_size: 15
        on_release: app.set_parameters_as_default("")

    MDRoundFlatIconButton:
        icon: "note-multiple"
        text: "Show Parameters"
        pos_hint: {'center_x': 0.825, 'center_y': 0.12}
        size_hint: None, None
        size: 203, 30
        font_style: 'Button'
        font_size: 15
        on_release: app.show_data("")

    MDTextField:
        id: spec_diam
        hint_text:  "Specimen Diameter [m]"
        multiline:  False
        on_text_validate:   app.update_parameters("specimen", 0, self)
        helper_text: "Default value: {} [m]".format(app.parameters[0][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "diameter"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.9}
        size_hint_x: None
        width: 240

    MDTextField:
        id: spec_length
        hint_text:  "Specimen Length [m]"
        multiline:  False
        on_text_validate:   app.update_parameters("specimen", 1, self)
        helper_text: "Default value: {} [m]".format(app.parameters[1][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "consolidate"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.8}
        size_hint_x: None
        width: 240

    MDTextField:
        id: bar_diameter 
        hint_text:  "Bar Diameter [m]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 2, self)
        helper_text: "Default value: {} [m]".format(app.parameters[2][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "diameter"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.7}
        size_hint_x: None
        width: 240

    MDTextField:
        id: young_modulus
        hint_text:  "Young's Modulus [Pa]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 3, self)
        helper_text: "Default value: {} [GPa]".format(app.parameters[3][1]/1e9)
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "alpha-e-circle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.6}
        size_hint_x: None
        width: 240

    MDTextField:
        id: first_gage
        hint_text:  "First Gauge [m]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 4, self)
        helper_text: "Default value: {} [m]".format(app.parameters[4][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "chevron-triple-right"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.5}
        size_hint_x: None
        width: 240

    MDTextField:
        id: second_gage
        hint_text:  "Second Gauge [m]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 5, self)
        helper_text: "Default value: {} [m]".format(app.parameters[5][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "transfer-right"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.4}
        size_hint_x: None
        width: 240

    MDTextField:
        id: sound_velocity
        hint_text:  "Sound Velocity [m/s]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 6, self)
        helper_text: "Default value: {} [m/s]".format(app.parameters[6][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "speedometer"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.3}
        size_hint_x: None
        width: 240

    MDTextField:
        id: gage_factor
        hint_text:  "Gauge Factor [-]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 7, self)
        helper_text: "Default value: {}".format(app.parameters[7][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "gauge"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.2}
        size_hint_x: None
        width: 240

    MDTextField:
        id: bridge_tension
        hint_text:  "Bridge Tension [V]"
        multiline:  False
        on_text_validate:   app.update_parameters("experiment", 8, self)
        helper_text: "Default value: {} [V]".format(app.parameters[8][1])
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "bridge"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.15, 'center_y': 0.1}
        size_hint_x: None
        width: 240

    MDRoundFlatButton:
        id: experiment_chooser
        text: "Choose Experiment"
        pos_hint: {"center_x": .5, "center_y": .75}
        font_style: 'Button'
        font_size: 15
        on_release: app.experiments_menu.open()

    MDRoundFlatButton:
        text: "Analyse All Experiments"
        pos_hint: {"center_x": .5, "center_y": .9}
        font_style: 'Button'
        font_size: 15
        on_release: app.analyse_all_experiments()

    MDSwitch:
        pos_hint:  {'center_x': .825, 'center_y': .85}
        on_active:  app.change_sp_mode()
        on_state:   app.change_sp_mode()

    MDLabel:
        pos_hint:  {'center_x': .76, 'center_y': .85}
        text:   "auto"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .89, 'center_y': .85}
        text:   "manual"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .825, 'center_y': .9}
        text:   "CROPPING"
        font_name: 'BAUHS93'
        font_size: 17
        halign: "center"

    MDSwitch:
        pos_hint:  {'center_x': .825, 'center_y': .7}
        on_active:  app.change_exp_mode()
        on_state:   app.change_exp_mode()

    MDLabel:
        pos_hint:  {'center_x': .76, 'center_y': .7}
        text:   "comp"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .89, 'center_y': .7}
        text:   "tens"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .825, 'center_y': .75}
        text:   "MODE"
        font_name: 'BAUHS93'
        font_size: 17
        halign: "center"

    MDSwitch:
        pos_hint:  {'center_x': .825, 'center_y': .55}
        on_active:  app.change_specimen_mode()
        on_state:   app.change_specimen_mode()

    MDLabel:
        pos_hint:  {'center_x': .76, 'center_y': .55}
        text:   "regular"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .89, 'center_y': .55}
        text:   "shear"
        halign: "center"
        font_name: 'ERASLGHT'

    MDLabel:
        pos_hint:  {'center_x': .825, 'center_y': .6}
        text:   "SPECIMEN"
        font_name: 'BAUHS93'
        font_size: 17
        halign: "center"


<SettingsTab>

    MDSwitch:
        pos_hint:  {'center_x': .585, 'center_y': .3}
        on_active:  app.change_bar_num()
        on_state:   app.change_bar_num()

    MDLabel:
        pos_hint:  {'center_x': .895, 'center_y': .3}
        text:   "One Bar Experiment"
        halign: "left"

    MDSwitch:
        pos_hint:  {'center_x': .585, 'center_y': .4}
        on_active:  app.change_auto_open_report()
        on_state:   app.change_auto_open_report()

    MDLabel:
        pos_hint:  {'center_x': .895, 'center_y': .4}
        text:   "Disable Report"
        halign: "left"

    MDSwitch:
        pos_hint:  {'center_x': .585, 'center_y': .5}
        on_active:  app.change_theme()
        on_state:   app.change_theme()

    MDLabel:
        pos_hint:  {'center_x': .895, 'center_y': .5}
        text:   "Dark Mode"
        halign: "left"

    Image:
        source: "images/logo-dfl.png"
        pos_hint: {"center_x": 0.49, "center_y":0.075}
        size_hint: .15, .15

    MDTextField:
        id: prominence_percent
        hint_text:  "Prominence [%]"
        multiline:  False
        on_text_validate:   app.update_parameters("spacing", 0, self)
        helper_text: "Default value: {}%".format(app.prominence_percent*100)
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': .5, 'center_y': .6}
        icon_right: "chart-areaspline"
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: 0.21
        width: 300

    MDTextField:
        id: spacing
        hint_text:  "Spacing"
        multiline:  False
        on_text_validate:   app.update_parameters("spacing", 0, self)
        helper_text: "Default value: {} points".format(app.spacing)
        helper_text_mode: "on_focus"
        helper_text_color: app.theme_cls.primary_color
        icon_right: "arrow-expand-horizontal"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': .5, 'center_y': .7}
        size_hint_x: 0.21
        width: 300

    MDRoundFlatButton:
        id: change_channels
        text: "Channel Configuration"
        pos_hint: {"center_x": .5, "center_y": .8}
        font_name: 'LUCON'
        font_size: 17
        on_release: app.open_channel_dialog("change")

'''
type: 'bottom'
