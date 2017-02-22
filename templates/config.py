"""
Define substitutions dict here with all defined variables for the templates.
Notes:
    • The value after  # was the standard value.
    • Pixel sizes are related to input resolution.
    • Currently, most <textwidth>-Tags will not be scaled. The factor
      GlobalFontScaling would be a good basis if you want change that.
"""
substitutions = {
    # "W": 1920,
    # "H": 1080,

    # Font scaling is uncoupled from resolution scaling.
    # "GlobalFontScaling": 0.75, # Normal sized font at 720x480
    "GlobalFontScaling": 1.0,  # Big font at 720x480
    # "GlobalFontScaling": 1.1, # Font fits still in most labels.

    # Factor for VT323 font type.
    "VT323FontScaling": 1.2,

    # Constants from Includes.xml
    "DepthDialog": 0.50,
    "DepthDialog+": 0.52,
    "DepthDialog-": 0.48,
    "DepthMax": 0.54,
    "DepthOSD": 0.40,
    "DepthOSD+": 0.44,
    "DepthContentPopout": 0.10,
    "DepthContentPanel": 0.05,
    "DepthBars": 0.12,
    "DepthBackground": -0.80,
    "DepthSideBlade": 0.10,
    "bg_alpha": 79,
    "dialogbuttons_itemgap": -20,
    "list_y_offset": 0,
    "list_item_height": 80,

    # Constants from Constants_1920.xml
    "widelist_width": 1325,
    "list_width": 730,
    "width_center": 960,
    "tvchannelslist_width": 1002,
    "tvrecordings_width": 1060,
    "eventloglist_width": 1430,
    "playlisteditorlist_width": 770,
    "playlistlist_width": 896,

    "HomeLeftPanelExtraWidth": 200,
    "InfoBarExtraHeight": 30,

    "MediaMenuBladeExtraWidth": 400,
    "MediaMenuBladeExtraWidth2": 400,  # Affects background image
    "MediaMenuItemExtraHeight": 20,

    "SettingsItemExtraWidth": 200,
    "SettingsItemExtraHeight": 20,  # For bigger font sizes

    "DialogExtraWidth": 200,

    "ImageWidgetButtonExtraHeight": 60,
}

# Finally, extend by other dicts here
map(lambda x: substitutions.update(x), [])
