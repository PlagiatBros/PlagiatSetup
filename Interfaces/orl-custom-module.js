host = 'osc.udp://127.0.0.1:11000'

sl_registered = false
sl_host = '127.0.0.1'
sl_port = 9951

lightseq = 8003

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

sl_map = [0,1,2,3,4,5,6,7,8]
sl_range = '[0-8]'

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
            '/strip/VxORLDelayPost/Gain/Mute',
        ]
    },
delaypre: {
        both:[
            '/strip/VxORLDelayPre/Gain/Mute'
        ]
},
    vocode: {
        on: [
            '/strip/VxORLMeuf/Gain/Mute',
            '/strip/VxORLVocodePost/Gain/Mute'
        ],
        off: [
            '/strip/VxORLVocodePost/Gain/Mute'
        ]
    }
}



pitch_addresses = [
    ['samples', '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'],
    ['samples', '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'],
    ['basssynth','/strip/BassSynth/AM%20pitchshifter/Pitch%20shift/unscaled'],
    ['vx','/x42/pitch'],
]
pitch_ports = {
    'samples':7008,
    'basssynth':7020,
    'vx':7040,

}


mididings_host = '127.0.0.1'
mididings_port = 57422
mididings_registered = false
mididings_current_scenes = false
mididings_current_subscenes = false
mididings_scenes = {}


time_zero = Date.now();

setInterval(()=>{

    setTimer((Date.now() - time_zero )/ 1000)

}, 1000)

function setTimer(time){

    var h = Math.floor(time / 3600),
        m = Math.floor((time - h * 3600) / 60),
        s = Math.round((time - h * 3600 - m * 60))

    receiveOsc({
        address: '/timer',
        args: [
            {
                type: 's',
                value: `${h<10?'0':''}${h}:${m<10?'0':''}${m}:${s<10?'0':''}${s}`
            }
        ]
    })
}

app.on('sessionOpened', ()=>{
    var monitors = loadJSON('./monitors.json')
    for (var m in monitors) {
        var last
        for (var i in monitors[m]) {
            if (monitors[m][i].id.includes('Monitors')) {
                last = monitors[m][i]
                monitors[m].splice(i, 1)
                break
            }
        }
        if (last) monitors[m].push(last)

        receive('/' + m, monitors[m])
    }
    receive('/timer_reset', 1)
})



module.exports = {
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
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','state', host, '/sl_state')
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','loop_len', host, '/sl_time')
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','loop_pos', host, '/sl_time')

                setTimeout(()=>{


                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','state',  host, '/sl_state')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','loop_len', host, '/sl_time')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','loop_pos', host, '/sl_time')

                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','state', 1,  host, '/sl_state')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','loop_len', 50, host, '/sl_time')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','loop_pos', 50, host, '/sl_time')

                }, 250)
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

        // setTimeout(()=>{
        //     var address = '/EXEC',
        //         args = [
        //             {type:'s', value: 'edit'},
        //             {type:'s', value: 'sacem_samples'},
        //             {type:'s', value: JSON.stringify({widgets:sacem_buttons})}
        //         ]
        //
        //     receiveOsc({address, args})
        //
        // },5000)
    },
    oscInFilter: function(data){
        // Filter incomming osc messages

        var {address, args, host, port} = data

        if (address == '/pong') {
            sl_registered = true
            return
        }

        else if (address == '/sl_time') {

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
                v    = args[2].value,
                loop_n  = sl_map.indexOf(i)

            var state = {
                record:0,
                overdub:0,
                pause:0,
                wait:0
            }

            state[sl_states[v]] = 1

            for (k in state) {
                receiveOsc({
                    address: '/sl/' + loop_n + '/hit/feedback',
                    args: [{type:'s', value:k}, {type:'s', value:state[k]}]
                })
            }

            return


        } else if (address.indexOf('/mididings') != -1) {

            mididings_registered = true

            if (address == '/mididings/add_scene') {

                mididings_scenes[args[0].value] = {
                    title: args[1].value,
                    subscenes: []
                }
                // for (var i = 2; i < args.length; i++) {
                //     mididings_scenes[args[0].value].subscenes.push(args[i].value)
                // }

                return

            }

            else if (address == '/mididings/end_scenes') {

                var scenes_buttons = {}
                for (var i in mididings_scenes) {
                    scenes_buttons[mididings_scenes[i].title] = parseInt(i)
                }
                address = '/EDIT'
                args = [
                    {type:'s', value: 'mididings_scenes'},
                    {type:'s', value: JSON.stringify({values:scenes_buttons})}
                ]

                setTimeout(()=>{
                    receiveOsc({address, args, host, port})

                    receiveOsc({address:'/mididings/switch_scene', args:[{type:'s',value: mididings_current_scenes }]})
                    // receiveOsc({address:'/mididings/switch_subscene', args:[{type:'s',value: mididings_current_subscenes }]})

                },3000)

                return
            }

            else if (address == '/mididings/current_scene') {

                // if (mididings_current_scenes != args[0].value) {
                //
                //     var subscenes_buttons = {}
                //
                //     for (var i in mididings_scenes[args[0].value].subscenes) {
                //         subscenes_buttons[mididings_scenes[args[0].value].subscenes[i]] = parseInt(i) + 1
                //     }
                //     address = '/EDIT'
                //     editargs = [
                //         {type:'s', value: 'mididings_subscenes'},
                //         {type:'s', value: JSON.stringify({values:subscenes_buttons})}
                //     ]
                //
                //     receiveOsc({address, args:editargs, host, port})
                //
                // }

                mididings_current_scenes = args[0].value
                // mididings_current_subscenes = args[1].value

                receiveOsc({address:'/mididings/switch_scene', args:[{type:'s',value: args[0].value }]})
                // receiveOsc({address:'/mididings/switch_subscene', args:[{type:'s',value: args[1].value }]})

                return

            }


        }


        return {address, args, host, port}

    },
    oscOutFilter: function(data){
        // Filter outgoing osc messages

        var {address, args, host, port} = data

        if (address.indexOf('/sl') != -1) {
            let i = address.split('/')[2]
            if (i!=-1) address = '/sl/' + sl_map[i] + '/hit'

            // if (args[0].value === 'reverse' && !args[1].value) {
            //     address = '/sl/-1/up'
            // }
            // if (args[0].value === 'reverse' && args[1].value) {
            //     address = '/sl/-1/down'
            // }

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

            var v = args[0].value


            for (i in pitch_addresses) {
                var [portname, address] = pitch_addresses[i]
                sendOsc({
                    address: address,
                    args: [{type:'f', value:v}],
                    host: non_host,
                    port: pitch_ports[portname]
                })
            }

            return

        }

        else if (address.indexOf('/mididings') != -1) {
            host= mididings_host,
            port= mididings_port
        }

        else if (address == '/sl/-1/hit' && args[0].value == 'reverse') {
            // strip 2nd arg out as it only used for gui (fake) state
            args = [args[0]]
        }

        else if (address == '/timer_reset') {
            time_zero = Date.now()
            setTimer(0)
            return
        }

        else if (address == '/bigup') {
            for (rpi of [
              "127.0.0.1:5555",
              "127.0.0.1:5556",
          ]) {
	 var [host, port] = rpi.split(':')
		 port = parseInt(port)
              sendOsc({
                  host,
                  port,
                  address: '/pyta/text/*/reset',
                  args: []
              })
              let n = Math.round(Math.random()*3)
              sendOsc({
                  host,
                  port,
                  address: '/pyta/text/'+n+'/set',
                  args: [{type:'s', value: 'visible'}, {type:'i', value: 1}]
              })
              sendOsc({
                  host,
                  port,
                  address: '/pyta/text/'+n+'/set',
                  args: [{type:'s', value: 'text'}, {type:'s', value: args[0].value}]
              })

          }
            return
        }

        else if (address == '/mandela') {

            address = '/Lightseq/Scene/Play'
            host = '127.0.0.1'
            port = lightseq
            args = [
                {type: 's', value: 'climat_mandela_subs'},
                {type: 'i', value: args[0].value},
            ]

        }


        else if (address === '/cmescene') {
            address = '/mididings/switch_scene'
        }

        return {address, args, host, port}
    }
}
