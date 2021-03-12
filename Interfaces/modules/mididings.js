mididings_host = '127.0.0.1'
mididings_port = 57422
mididings_registered = false
mididings_current_scenes = false
mididings_current_subscenes = false
mididings_scenes = {}


module.exports = {

    init: ()=>{

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

    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        if (address.indexOf('/mididings') != -1) {

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

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data

        if (address.indexOf('/mididings') != -1) {
            host = mididings_host,
            port = mididings_port
        }


        return {address, args, host, port}

    }

}
