osc_host = 'osc.udp://127.0.0.1:11000'

sl_registered = false
sl_host = '127.0.0.1'
sl_port = 9951
sl_states = {
    2:'record',
    5:'overdub',
    14:'pause',
    1:'wait',
    3:'wait'
}

sl_reverse = false

sl_map = [0,1,2,3,4,5,6,7,8]
sl_range = '[0-8]'
loop_time = {
    loop_pos:{},
    loop_len:{}
}


module.exports = {
    init: ()=>{

        ping = ()=>{
            sendOsc({
                address: '/ping',
                args: [{type:'s', value: osc_host},{type:'s',value:'/pong'}],
                host: sl_host,
                port: sl_port
            })
            if (!sl_registered) {
                setTimeout(ping,1000)
            } else {
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','state', osc_host, '/sl_state')
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','loop_len', osc_host, '/sl_time')
                send(sl_host, sl_port, '/sl/'+sl_range+'/unregister_auto_update','loop_pos', osc_host, '/sl_time')

                setTimeout(()=>{


                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','state',  osc_host, '/sl_state')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','loop_len', osc_host, '/sl_time')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/get','loop_pos', osc_host, '/sl_time')

                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','state', 1,  osc_host, '/sl_state')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','loop_len', 50, osc_host, '/sl_time')
                    send(sl_host, sl_port, '/sl/'+sl_range+'/register_auto_update','loop_pos', 50, osc_host, '/sl_time')

                }, 250)
            }
        }

        setTimeout(ping, 1000)

    },

    oscInFilter: (data)=>{

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
                var prevVal = loop_time.loop_pos[i] / loop_time.loop_len[i]
                loop_time[ctrl][i] = v
                address = '/sl_position_' + sl_map.indexOf(i)
                args = [{type:'f', value:loop_time.loop_pos[i] / loop_time.loop_len[i]}]

                if (isNaN(args[0].value)) return false

                var reverse = args.value != 0 && args.value < prevVal
                if (reverse != sl_reverse) {
                    sl_reverse = reverse
                    receive('/sl/-1/hit/feedback', 'reverse', sl_reverse ? 1 : 0)
                }
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


        }

        return {address, args, host, port}


    },

    oscOutFilter: (data)=>{

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

        else if (address == '/sl/-1/hit' && args[0].value == 'reverse') {
            // strip 2nd arg out as it only used for gui (fake) state
            args = [args[0]]
        }

        return {address, args, host, port}

    }

}
