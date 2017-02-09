(function(){

    host = 'osc.udp://127.0.0.1:11000'

    sl_registered = false
    sl_host = '127.0.0.1'
    sl_port = 9951

    loop_time = {
        loop_pos:{},
        loop_len:{}
    }

    sl_states = {
        2:'record',
        5:'overdub',
        14:'pause',
        1:'wait',
        3:'wait'
    }

    sl_map = [6,7,8]
    sl_range = '[6-8]'

    non_host = '127.0.0.1'

    vx_ports = {
        pre:6666,
        post:6668
    }
    vx_addresses = {
        meuf: {
            on: [
                '/strip/VxORLMeuf/Gain/Mute',
                '/strip/VxORLMeufPost/Gain/Mute'
            ],
            off: [
                '/strip/VxORLMeufPost/Gain/Mute'
            ]
        },
        gars: {
            both: [
                '/strip/VxORLGars/Gain/Mute',
                '/strip/VxORLGarsPost/Gain/Mute'
            ]
        },
        disint: {
            both: [
                '/strip/VxORLDisint/Gain/Mute',
                '/strip/VxORLDisintPost/Gain/Mute'
            ],
        },
        delay: {
            both:[
                '/strip/VxORLDelayPre/Gain/Mute',
                '/strip/VxORLDelayPost/Gain/Mute'
            ]
        },
        vocod: {
            on: [
                '/strip/VxORLMeuf/Gain/Mute',
                '/strip/VxORLVocodePost/Gain/Mute'
            ],
            off: [
                '/strip/VxORLVocodePost/Gain/Mute'
            ]
        }
    }



    pitch_addresses = {
        samples:['/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled']
    }
    pitch_ports = {
        samples:7008
    }

    mididings_host = '127.0.0.1'
    mididings_port = 57422
    mididings_registered = false
    mididings_current_scenes = false
    mididings_current_subscenes = false
    mididings_scenes = {}


    return {
        init: function(){

            ping = ()=>{
                sendOsc({
                    address: '/ping',
                    args: [{type:'s', value:host},{type:'s',value:'/pong'}],
                    host: sl_host,
                    port: sl_port
                })
                if (!sl_registered) {
                    setTimeout(ping,1000)
                } else {
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'state'}, {type:'f',value:1}, {type:'s', value:host}, {type:'s', value:'/sl_state'}],
                        host: sl_host,
                        port: sl_port
                    })
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'loop_len'}, {type:'f',value:50}, {type:'s', value:host}, {type:'s', value:'/sl_time'}],
                        host: sl_host,
                        port: sl_port
                    })
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'loop_pos'}, {type:'f',value:50}, {type:'s', value:host}, {type:'s', value:'/sl_time'}],
                        host: sl_host,
                        port: sl_port
                    })
                }
            }

            mididings_query = ()=>{
                if (!mididings_registered) {
                    sendOsc({
                        address: '/mididings/query',
                        args: [],
                        host: mididings_host,
                        port: mididings_port
                    })
                    setTimeout(mididings_query, 1000)
                }

            }

            setTimeout(mididings_query, 1000)

            setTimeout(ping, 1000)
        },
        oscInFilter: function(data){
            // Filter incomming osc messages

            var {address, args, host, port} = data

            if (address == '/pong') {
                sl_registered = true
                return
            }

            else if (address == '/sl_time') {
                sl_registered = true

                var i    = args[0].value,
                    ctrl = args[1].value,
                    v    = args[2].value


                if (ctrl.indexOf('loop_') != -1) {
                    loop_time[ctrl][i] = v
                    address = '/sl_position_' + sl_map.indexOf(i)
                    args = [{type:'f', value:loop_time.loop_pos[i] / loop_time.loop_len[i]}]
                    if (isNaN(args[0].value)) return
                }

            }

            else if (address == '/sl_state') {

                var i    = args[0].value,
                    v    = args[2].value

                var state = {
                    record:0,
                    overdub:0,
                    pause:0,
                    wait:0
                }

                state[sl_states[v]] = 1

                for (k in state) {
                    receiveOsc({
                        address: '/sl/' + sl_map.indexOf(i) + '/hit',
                        args: [{type:'s', value:k}, {type:'s', value:state[k]}]
                    })
                }

                return

            }

            else if (address.indexOf('/mididings') != -1) {

                mididings_registered = true

                if (address == '/mididings/add_scene') {

                    mididings_scenes[args[0].value] = {
                        title: args[1].value,
                        subscenes: []
                    }
                    for (var i = 2; i < args.length; i++) {
                        mididings_scenes[args[0].value].subscenes.push(args[i].value)
                    }

                    return

                }

                else if (address == '/mididings/end_scenes') {

                    var scenes_buttons = {}
                    for (var i in mididings_scenes) {
                        scenes_buttons[mididings_scenes[i].title] = parseInt(i)
                    }
                    address = '/EXEC'
                    args = [
                        {type:'s', value: 'edit'},
                        {type:'s', value: 'mididings_scenes'},
                        {type:'s', value: JSON.stringify({values:scenes_buttons})}
                    ]

                    setTimeout(()=>{
                        receiveOsc({address, args, host, port})

                        receiveOsc({address:'/mididings/switch_scene', args:[{type:'s',value: mididings_current_scenes }]})
                        receiveOsc({address:'/mididings/switch_subscene', args:[{type:'s',value: mididings_current_subscenes }]})

                    },3000)

                    return
                }

                else if (address == '/mididings/current_scene') {

                    if (mididings_current_scenes != args[0].value) {

                        var subscenes_buttons = {}

                        for (var i in mididings_scenes[args[0].value].subscenes) {
                            subscenes_buttons[mididings_scenes[args[0].value].subscenes[i]] = parseInt(i) + 1
                        }
                        address = '/EXEC'
                        editargs = [
                            {type:'s', value: 'edit'},
                            {type:'s', value: 'mididings_subscenes'},
                            {type:'s', value: JSON.stringify({values:subscenes_buttons})}
                        ]

                        receiveOsc({address, args:editargs, host, port})

                    }

                    mididings_current_scenes = args[0].value
                    mididings_current_subscenes = args[1].value

                    receiveOsc({address:'/mididings/switch_scene', args:[{type:'s',value: args[0].value }]})
                    receiveOsc({address:'/mididings/switch_subscene', args:[{type:'s',value: args[1].value }]})

                    return

                }


            }

            return {address, args, host, port}

        },
        oscOutFilter: function(data){
            // Filter outgoing osc messages

            var {address, args, host, port} = data

            if (address.indexOf('/sl') != -1) {
                address = '/sl/' + sl_map[address.split('/')[2]] + '/hit'
                args.splice(1,1)
                host = sl_host
                port = sl_port

            }

            else if (address == '/vxorl') {

                var type = args[0].value,
                    v    = args[1].value


                if (!vx_addresses[type]) throw 'Unknown VX strip ' + type

                var addresses = vx_addresses[type].both || vx_addresses[type][['off','on'][v]]

                for (i in addresses) {
                    sendOsc({
                        address: addresses[i],
                        args: [{type:'f', value:[1,0][v]}],
                        host: non_host,
                        port: addresses[i].indexOf('Post') != -1 ? vx_ports.post : vx_ports.pre

                    })
                }

                return

            }

            else if (address == '/pitch') {

                var type = args[0].value,
                    v    = args[1].value


                if (!pitch_ports[type]) throw 'Unknown Pitch strip ' + type

                var addresses = pitch_addresses[type]

                for (i in addresses) {
                    sendOsc({
                        address: addresses[i],
                        args: [{type:'f', value:v}],
                        host: non_host,
                        port: pitch_ports[type]
                    })
                }

                return

            }

            else if (address.indexOf('/mididings') != -1) {
                host= mididings_host,
                port= mididings_port
            }

            return {address, args, host, port}
        }
    }

})()
