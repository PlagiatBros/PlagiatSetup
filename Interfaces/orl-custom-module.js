(function(){

    registered = false
    slhost = '127.0.0.1'
    slport = 9952
    host = 'osc.udp://127.0.0.1:8080'

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

    sl_map = [0,1,2]
    sl_range = '[0-2]'

    nonhost = '127.0.0.1'

    vxports = {
        pre:6666,
        post:6668
    }
    vxaddresses = {
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


    pitchaddresses = {
        samples:['/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled']
    }
    pitchports = {
        samples:7008
    }

    return {
        init: function(){

            ping = ()=>{
                sendOsc({
                    address: '/ping',
                    args: [{type:'s', value:host},{type:'s',value:'/pong'}],
                    host: slhost,
                    port: slport
                })
                if (!registered) {
                    setTimeout(ping,1000)
                } else {
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'state'}, {type:'f',value:1}, {type:'s', value:host}, {type:'s', value:'/sl_state'}],
                        host: slhost,
                        port: slport
                    })
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'loop_len'}, {type:'f',value:50}, {type:'s', value:host}, {type:'s', value:'/sl_time'}],
                        host: slhost,
                        port: slport
                    })
                    sendOsc({
                        address: '/sl/'+sl_range+'/register_auto_update',
                        args: [{type:'s',value:'loop_pos'}, {type:'f',value:50}, {type:'s', value:host}, {type:'s', value:'/sl_time'}],
                        host: slhost,
                        port: slport
                    })
                }
            }

            setTimeout(ping,1000)
        },
        oscInFilter: function(data){
            // Filter incomming osc messages

            var {address, args, host, port} = data

            if (address == '/pong') {
                registered = true
                return
            }

            else if (address == '/sl_time') {
                registered = true

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


            return {address, args, host, port}

        },
        oscOutFilter: function(data){
            // Filter outgoing osc messages

            var {address, args, host, port} = data

            if (address.indexOf('/sl') != -1) {
                address = '/sl/' + sl_map[address.split('/')[2]] + '/hit'
                args.splice(1,1)
                host = slhost
                port = slport

            }

            else if (address == '/vxorl') {

                var type = args[0].value,
                    v    = args[1].value


                if (!vxaddresses[type]) throw 'Unknown VX strip ' + type

                var addresses = vxaddresses[type].both || vxaddresses[type][['off','on'][v]]

                for (i in addresses) {
                    sendOsc({
                        address: addresses[i],
                        args: [{type:'f', value:[1,0][v]}],
                        host: nonhost,
                        port: addresses[i].indexOf('Post') != -1 ? vxports.post : vxports.pre

                    })
                }

                return

            }

            else if (address == '/pitch') {

                var type = args[0].value,
                    v    = args[1].value


                if (!pitchports[type]) throw 'Unknown Pitch strip ' + type

                var addresses = pitchaddresses[type]

                for (i in addresses) {
                    sendOsc({
                        address: addresses[i],
                        args: [{type:'f', value:v}],
                        host: nonhost,
                        port: pitchports[type]
                    })
                }

                return

            }

            return {address, args, host, port}
        }
    }

})()
