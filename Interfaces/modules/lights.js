lightseq = 8003

module.exports = {

    init: ()=>{


    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        return {address, args, host, port}

    },

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data



        if (address == '/bigup') {

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


        return {address, args, host, port}

    }

}
