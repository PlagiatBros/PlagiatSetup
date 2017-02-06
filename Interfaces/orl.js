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
                "height": "70%",
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
                        "color": "auto",
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
                        "label": "Ctrlz",
                        "width": "68%",
                        "scroll": true,
                        "color": "auto",
                        "widgets": [
                            {
                                "type": "strip",
                                "top": 0,
                                "left": 0,
                                "id": "sooperlooper",
                                "label": "Sooperlooper",
                                "width": "100%",
                                "height": "80%",
                                "horizontal": false,
                                "color": "auto",
                                "widgets": [
                                    {
                                        "type": "panel",
                                        "id": "panel_1",
                                        "label": 1,
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
                                                "css": "--display-input:none;",
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
                                                "compact": true
                                            }
                                        ],
                                        "tabs": [],
                                        "height": "auto"
                                    },
                                    {
                                        "type": "panel",
                                        "id": "panel_1",
                                        "label": 2,
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
                                                "css": "--display-input:none;",
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
                                                "compact": true
                                            }
                                        ],
                                        "tabs": [],
                                        "height": "auto"
                                    },
                                    {
                                        "type": "panel",
                                        "id": "panel_1",
                                        "label": 3,
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
                                                "css": "--display-input:none;",
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
                                                "compact": true
                                            }
                                        ],
                                        "tabs": [],
                                        "height": "auto"
                                    }
                                ],
                                "css": ""
                            },
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
                                "tabs": []
                            }
                        ],
                        "tabs": [],
                        "height": "100%",
                        "css": ""
                    },
                    {
                        "type": "panel",
                        "left": "80%",
                        "id": "samples",
                        "label": "Samples",
                        "width": "20%",
                        "height": "100%",
                        "scroll": true,
                        "color": "auto",
                        "widgets": [],
                        "tabs": [],
                        "top": "auto",
                        "css": ""
                    }
                ],
                "tabs": []
            },
            {
                "type": "panel",
                "top": "70%",
                "left": 0,
                "id": "mididings",
                "label": "Mididings",
                "width": "100%",
                "height": "30%",
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
                        "height": "50%",
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
                        "top": "50%",
                        "left": 0,
                        "id": "mididings_subscenes",
                        "label": "Subscenes",
                        "width": "100%",
                        "height": "50%",
                        "horizontal": true,
                        "color": "auto",
                        "css": "",
                        "linkId": "",
                        "values": {
                            "Bass ORL": 1,
                            "Nope": 8,
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
                "tabs": []
            }
        ]
    }
]