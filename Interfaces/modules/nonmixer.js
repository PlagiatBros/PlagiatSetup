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


app.on('sessionOpened', (data, client)=>{
    var monitors = loadJSON('../monitors.json')
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

        receive('/' + m, monitors[m], {clientId: client.id})
    }
})

module.exports = {

    init: ()=>{


    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        return {address, args, host, port}

    },

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data

        if (address == '/vxorl') {

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

        return {address, args, host, port}

    }

}
