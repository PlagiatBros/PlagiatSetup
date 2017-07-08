[
    {
        "label": "PLAGIAT",
        "widgets": [
            {
                "type": "panel",
                "top": 0,
                "left": 0,
                "id": "panel_4",
                "label": false,
                "width": "100%",
                "height": "85%",
                "scroll": true,
                "color": "auto",
                "css": "",
                "widgets": [
                    {
                        "type": "fader",
                        "top": 0,
                        "left": 0,
                        "id": "pitch_samples",
                        "linkId": "",
                        "label": "Pitch",
                        "unit": "",
                        "width": "10%",
                        "height": "100%",
                        "alignRight": false,
                        "horizontal": false,
                        "noPip": false,
                        "compact": true,
                        "color": "lime",
                        "css": "--display-input:none;",
                        "snap": false,
                        "spring": true,
                        "range": {
                            "min": 0,
                            "max": 2
                        },
                        "origin": 1,
                        "value": "",
                        "logScale": false,
                        "precision": 2,
                        "meter": false,
                        "address": "/pitch",
                        "preArgs": [
                            "samples"
                        ],
                        "target": [
                            "non:pitch"
                        ]
                    },
                    {
                        "type": "panel",
                        "top": 0,
                        "left": "11%",
                        "id": "panel_2",
                        "label": false,
                        "width": "89%",
                        "scroll": true,
                        "color": "auto",
                        "widgets": [
                            {
                                "type": "panel",
                                "top": "80%",
                                "left": 0,
                                "id": "Vx",
                                "label": "auto",
                                "width": "100%",
                                "height": "20%",
                                "scroll": true,
                                "color": "auto",
                                "css": "",
                                "widgets": [
                                    {
                                        "type": "toggle",
                                        "top": 0,
                                        "left": 0,
                                        "id": "vx_orl_meuf",
                                        "linkId": "",
                                        "label": "MEUF",
                                        "width": "20%",
                                        "height": "100%",
                                        "color": "pink",
                                        "css": "",
                                        "on": 1,
                                        "off": 0,
                                        "precision": 2,
                                        "preArgs": [
                                            "meuf"
                                        ],
                                        "target": [
                                            "non:vx"
                                        ],
                                        "address": "/vxorl",
                                        "value": ""
                                    },
                                    {
                                        "type": "toggle",
                                        "top": 0,
                                        "left": "20%",
                                        "id": "vx_orl_gars",
                                        "linkId": "",
                                        "label": "GARS",
                                        "width": "20%",
                                        "height": "100%",
                                        "color": "auto",
                                        "css": "",
                                        "on": 1,
                                        "off": 0,
                                        "precision": 2,
                                        "preArgs": [
                                            "gars"
                                        ],
                                        "target": [
                                            "non:vx"
                                        ],
                                        "address": "/vxorl",
                                        "value": ""
                                    },
                                    {
                                        "type": "toggle",
                                        "top": 0,
                                        "left": "40%",
                                        "id": "vx_orl_disint",
                                        "linkId": "",
                                        "label": "DISINT",
                                        "width": "20%",
                                        "height": "100%",
                                        "color": "red",
                                        "css": "",
                                        "on": 1,
                                        "off": 0,
                                        "precision": 2,
                                        "preArgs": [
                                            "disint"
                                        ],
                                        "target": [
                                            "non:vx"
                                        ],
                                        "address": "/vxorl",
                                        "value": ""
                                    },
                                    {
                                        "type": "toggle",
                                        "top": 0,
                                        "left": "60%",
                                        "id": "vx_orl_delay",
                                        "linkId": "",
                                        "label": "DELAY",
                                        "width": "20%",
                                        "height": "100%",
                                        "color": "purple",
                                        "css": "",
                                        "on": 1,
                                        "off": 0,
                                        "precision": 2,
                                        "preArgs": [
                                            "delay"
                                        ],
                                        "target": [
                                            "non:vx"
                                        ],
                                        "address": "/vxorl",
                                        "value": ""
                                    },
                                    {
                                        "type": "toggle",
                                        "top": 0,
                                        "left": "80%",
                                        "id": "vx_orl_vocod",
                                        "linkId": "",
                                        "label": "VOCOD",
                                        "width": "20%",
                                        "height": "100%",
                                        "color": "green",
                                        "css": "",
                                        "on": 1,
                                        "off": 0,
                                        "precision": 2,
                                        "preArgs": [
                                            "vocod"
                                        ],
                                        "target": [
                                            "non:vx"
                                        ],
                                        "address": "/vxorl",
                                        "value": ""
                                    }
                                ],
                                "tabs": [],
                                "layout": "",
                                "spacing": 0
                            },
                            {
                                "type": "panel",
                                "top": 0,
                                "left": 0,
                                "id": "panel_3",
                                "label": "auto",
                                "width": "100%",
                                "height": "80%",
                                "scroll": true,
                                "color": "auto",
                                "css": "",
                                "layout": "",
                                "spacing": 0,
                                "widgets": [],
                                "tabs": [
                                    {
                                        "id": "",
                                        "label": "PRE",
                                        "widgets": [
                                            {
                                                "type": "strip",
                                                "id": "sooperlooper",
                                                "label": "Sooperlooper",
                                                "width": "100%",
                                                "height": "100%",
                                                "horizontal": false,
                                                "color": "pink",
                                                "widgets": [
                                                    {
                                                        "type": "panel",
                                                        "id": "panel_1",
                                                        "label": "Synth BASS",
                                                        "width": "100%",
                                                        "scroll": true,
                                                        "color": "auto",
                                                        "css": "",
                                                        "widgets": [
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": 0,
                                                                "id": "sl_record_0",
                                                                "linkId": "",
                                                                "label": "Record",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "red",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "record"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "address": "/sl/0/hit",
                                                                "css": ""
                                                            },
                                                            {
                                                                "type": "push",
                                                                "left": "20%",
                                                                "id": "sl_overdub_0",
                                                                "label": "Overdub",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "orange",
                                                                "css": "",
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "overdub"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "top": "auto",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "address": "/sl/0/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "40%",
                                                                "id": "sl_pause_0",
                                                                "label": "Pause",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "yellow",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "pause"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/0/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "60%",
                                                                "id": "sl_trigger_0",
                                                                "label": "Trigger",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "auto",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "trigger"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/0/hit"
                                                            },
                                                            {
                                                                "type": "knob",
                                                                "left": "80%",
                                                                "id": "sl_position_0",
                                                                "label": false,
                                                                "unit": "",
                                                                "width": "20%",
                                                                "height": "100%",
                                                                "color": "auto",
                                                                "css": "--display-input:none; canvas {pointer-events:none}",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "origin": "auto",
                                                                "value": "",
                                                                "preArgs": [],
                                                                "address": "/sl_position_0",
                                                                "compact": true,
                                                                "linkId": "",
                                                                "noPip": true,
                                                                "angle": 360,
                                                                "snap": false,
                                                                "spring": false,
                                                                "precision": 2,
                                                                "target": [],
                                                                "top": "auto"
                                                            },
                                                            {
                                                                "type": "meter",
                                                                "top": "90%",
                                                                "left": 0,
                                                                "id": "sl_wait_0",
                                                                "label": false,
                                                                "width": "80%",
                                                                "height": "10%",
                                                                "color": "red",
                                                                "css": "--display-input:none;--color-knob:transparent;",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "value": "",
                                                                "preArgs": [
                                                                    "wait"
                                                                ],
                                                                "unit": "",
                                                                "horizontal": true,
                                                                "origin": "auto",
                                                                "address": "/sl/0/hit",
                                                                "widgetId": "",
                                                                "compact": true
                                                            }
                                                        ],
                                                        "tabs": [],
                                                        "height": "auto",
                                                        "layout": "",
                                                        "spacing": 0
                                                    },
                                                    {
                                                        "type": "panel",
                                                        "id": "panel_1",
                                                        "label": "Synth AIGU",
                                                        "width": "100%",
                                                        "scroll": true,
                                                        "color": "auto",
                                                        "css": "",
                                                        "widgets": [
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": 0,
                                                                "id": "sl_record_1",
                                                                "linkId": "",
                                                                "label": "Record",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "red",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "record"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "address": "/sl/1/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "40%",
                                                                "id": "sl_pause_1",
                                                                "label": "Pause",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "yellow",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "pause"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/1/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "60%",
                                                                "id": "sl_trigger_1",
                                                                "label": "Trigger",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "auto",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "trigger"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/1/hit"
                                                            },
                                                            {
                                                                "type": "knob",
                                                                "left": "80%",
                                                                "id": "sl_position_1",
                                                                "label": false,
                                                                "unit": "",
                                                                "width": "20%",
                                                                "height": "100%",
                                                                "color": "auto",
                                                                "css": "--display-input:none; canvas {pointer-events:none}",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "origin": "auto",
                                                                "value": "",
                                                                "preArgs": [],
                                                                "address": "/sl_position_1",
                                                                "compact": true,
                                                                "linkId": "",
                                                                "noPip": true,
                                                                "angle": 360,
                                                                "snap": false,
                                                                "spring": false,
                                                                "precision": 2,
                                                                "target": [],
                                                                "top": "auto"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "left": "20%",
                                                                "id": "sl_overdub_1",
                                                                "label": "Overdub",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "orange",
                                                                "css": "",
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "overdub"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "top": 0,
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "address": "/sl/1/hit"
                                                            },
                                                            {
                                                                "type": "meter",
                                                                "top": "90%",
                                                                "left": 0,
                                                                "id": "sl_wait_1",
                                                                "label": false,
                                                                "width": "80%",
                                                                "height": "10%",
                                                                "color": "red",
                                                                "css": "--display-input:none;--color-knob:transparent;",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "value": "",
                                                                "preArgs": [
                                                                    "wait"
                                                                ],
                                                                "unit": "",
                                                                "horizontal": true,
                                                                "origin": "auto",
                                                                "address": "/sl/1/hit",
                                                                "widgetId": "",
                                                                "compact": true
                                                            }
                                                        ],
                                                        "tabs": [],
                                                        "height": "auto",
                                                        "layout": "",
                                                        "spacing": 0
                                                    },
                                                    {
                                                        "type": "panel",
                                                        "id": "panel_1",
                                                        "label": "RHODES",
                                                        "width": "100%",
                                                        "scroll": true,
                                                        "color": "auto",
                                                        "css": "",
                                                        "widgets": [
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": 0,
                                                                "id": "sl_record_2",
                                                                "linkId": "",
                                                                "label": "Record",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "red",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "record"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "address": "/sl/2/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "left": "20%",
                                                                "id": "sl_overdub_2",
                                                                "label": "Overdub",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "orange",
                                                                "css": "",
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "overdub"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "top": "auto",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "address": "/sl/2/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "40%",
                                                                "id": "sl_pause_2",
                                                                "label": "Pause",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "yellow",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "pause"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/2/hit"
                                                            },
                                                            {
                                                                "type": "push",
                                                                "top": 0,
                                                                "left": "60%",
                                                                "id": "sl_trigger_2",
                                                                "label": "Trigger",
                                                                "width": "20%",
                                                                "height": "90%",
                                                                "color": "auto",
                                                                "css": "",
                                                                "on": 1,
                                                                "off": 0,
                                                                "norelease": true,
                                                                "precision": 2,
                                                                "preArgs": [
                                                                    "trigger"
                                                                ],
                                                                "target": [
                                                                    "sl:port"
                                                                ],
                                                                "linkId": "",
                                                                "address": "/sl/2/hit"
                                                            },
                                                            {
                                                                "type": "knob",
                                                                "left": "80%",
                                                                "id": "sl_position_2",
                                                                "label": false,
                                                                "unit": "",
                                                                "width": "20%",
                                                                "height": "100%",
                                                                "color": "auto",
                                                                "css": "--display-input:none; canvas {pointer-events:none}",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "origin": "auto",
                                                                "value": "",
                                                                "preArgs": [],
                                                                "address": "/sl_position_2",
                                                                "compact": true,
                                                                "linkId": "",
                                                                "noPip": true,
                                                                "angle": 360,
                                                                "snap": false,
                                                                "spring": false,
                                                                "precision": 2,
                                                                "target": [],
                                                                "top": "auto"
                                                            },
                                                            {
                                                                "type": "meter",
                                                                "top": "90%",
                                                                "left": 0,
                                                                "id": "sl_wait_2",
                                                                "label": false,
                                                                "width": "80%",
                                                                "height": "10%",
                                                                "color": "red",
                                                                "css": "--display-input:none;--color-knob:transparent;",
                                                                "range": {
                                                                    "min": 0,
                                                                    "max": 1
                                                                },
                                                                "logScale": false,
                                                                "value": "",
                                                                "preArgs": [
                                                                    "wait"
                                                                ],
                                                                "unit": "",
                                                                "horizontal": true,
                                                                "origin": "auto",
                                                                "address": "/sl/2/hit",
                                                                "widgetId": "",
                                                                "compact": true
                                                            }
                                                        ],
                                                        "tabs": [],
                                                        "height": "auto",
                                                        "layout": "",
                                                        "spacing": 0
                                                    }
                                                ],
                                                "css": "",
                                                "left": "auto",
                                                "top": "auto"
                                            }
                                        ]
                                    },
                                    {
                                        "id": "",
                                        "label": "POST"
                                    }
                                ]
                            }
                        ],
                        "tabs": [],
                        "height": "100%",
                        "css": "",
                        "layout": "",
                        "spacing": 0
                    }
                ],
                "tabs": [],
                "layout": "",
                "spacing": 0
            },
            {
                "type": "panel",
                "top": "85%",
                "left": 0,
                "id": "mididings",
                "label": "Mididings",
                "width": "100%",
                "height": "15%",
                "scroll": true,
                "color": "auto",
                "css": "",
                "widgets": [
                    {
                        "type": "switch",
                        "top": 0,
                        "left": 0,
                        "id": "mididings_scenes",
                        "label": false,
                        "width": "100%",
                        "height": "30%",
                        "horizontal": true,
                        "color": "auto",
                        "css": "",
                        "linkId": "",
                        "values": {
                            "ConnassesSACEM": 1,
                            "Da Fist": 2,
                            "Climat": 3,
                            "Fifty": 4,
                            "Le5": 5,
                            "Trapone": 6,
                            "SW": 7,
                            "GetYourFreakOn": 8,
                            "Horrorcore": 9,
                            "Wholeworld": 10
                        },
                        "value": "",
                        "precision": 0,
                        "address": "/mididings/switch_scene",
                        "preArgs": [],
                        "target": [
                            "mididings:port"
                        ]
                    },
                    {
                        "type": "switch",
                        "top": "30%",
                        "left": 0,
                        "id": "mididings_subscenes",
                        "label": "Subscenes",
                        "width": "100%",
                        "height": "70%",
                        "horizontal": true,
                        "color": "auto",
                        "css": "",
                        "linkId": "",
                        "values": {
                            "Bass ORL": 1,
                            "Vx ORL": 2,
                            "Nope": 7,
                            "Pedal Select": 8,
                            "Tune Select": 9
                        },
                        "value": "",
                        "precision": 0,
                        "address": "/mididings/switch_subscene",
                        "preArgs": [],
                        "target": [
                            "mididings:port"
                        ]
                    }
                ],
                "tabs": [],
                "layout": "",
                "spacing": 0
            }
        ],
        "id": ""
    },
    {
        "label": "SACEM",
        "widgets": [
            {
                "type": "panel",
                "top": 0,
                "left": 0,
                "id": "sacem_samples",
                "label": "Samples ^heart",
                "width": "100%",
                "height": "100%",
                "scroll": true,
                "color": "auto",
                "css": "",
                "widgets": [
                    {
                        "type": "push",
                        "label": "Laughters",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            65
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_43",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "Reload",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            3,
                            65
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_44",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "Fire",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            3,
                            66
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_45",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "ArmeMitrailletteTony",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            120
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_46",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "Automatiseeslesarmesafeu",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            117
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_47",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroAdoreInternet",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            10
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_48",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroBonjour",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "0%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            0
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_49",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroChouetteJeuns",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            1
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_50",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroCondamne",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            1,
                            2
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_51",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroContreLaMusiqueGratuite",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            1,
                            11
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_52",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroFlippeSurInternet",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            3
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_53",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "ClogeroFlippeSurLesDroitsAuteur",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            4
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_54",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroLaAnarchie",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            5
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_55",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroLoiMalFaite",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "16.666666666666668%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            6
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_56",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroOse",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            7
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_57",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroPommeC",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            1,
                            8
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_58",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CalogeroVoleDesDisques",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            1,
                            9
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_59",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CesNousLesBagarreurs",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            111
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_60",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CommeTonyMontana2",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            121
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_61",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "CommeTonyMontana",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            122
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_62",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "EurosDansMonCompteCourant",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "33.333333333333336%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            115
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_63",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "FlorentPagnyPlagiat",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            17
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_64",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "JulRappeChambre",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            1,
                            112
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_65",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "LeCanonFrotteAMonPenis",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            1,
                            116
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_66",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "LunettesTonyMontana",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            119
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_67",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "MoiMoi",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            100
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_68",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PeignoirArmeAFeu",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            118
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_69",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PNApprendreCafe",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "50%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            15
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_70",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PNCreux",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            16
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_71",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PNStagiaire",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            1,
                            12
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_72",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PNPasStagiaireBenevole",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            1,
                            13
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_73",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "PNSousPaye",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            14
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_74",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TonyMontana1x2",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            123
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_75",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TonyMontana1x3",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            124
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_76",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TonyMontana1x",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "66.66666666666667%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            125
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_77",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TonyMontana2x",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "0%",
                        "preArgs": [
                            1,
                            126
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_78",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TonyMontana6x",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "14.285714285714286%",
                        "preArgs": [
                            1,
                            127
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_79",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "TrapDeFeignants",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "28.571428571428573%",
                        "preArgs": [
                            1,
                            114
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_80",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "UrolagneDescription",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "42.857142857142854%",
                        "preArgs": [
                            1,
                            102
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_81",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "Urolagne",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "57.142857142857146%",
                        "preArgs": [
                            1,
                            101
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_82",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "YADesEnfants",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "71.42857142857143%",
                        "preArgs": [
                            1,
                            103
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_83",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    },
                    {
                        "type": "push",
                        "label": "BlahBlahBlah",
                        "norelease": true,
                        "on": 127,
                        "precision": 0,
                        "width": "14.285714285714286%",
                        "height": "16.666666666666668%",
                        "top": "83.33333333333333%",
                        "left": "85.71428571428571%",
                        "preArgs": [
                            1,
                            104
                        ],
                        "address": "/midi/noteon",
                        "target": [
                            "127.0.0.1:11001"
                        ],
                        "id": "push_84",
                        "linkId": "",
                        "color": "auto",
                        "css": "",
                        "off": 0
                    }
                ],
                "tabs": [],
                "layout": "",
                "spacing": 0
            }
        ],
        "id": ""
    },
    {
        "id": "",
        "label": "Unnamed",
        "widgets": []
    }
]