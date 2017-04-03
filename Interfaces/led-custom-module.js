(function(){




    return {
        init: function(){
        },
        oscInFilter: function(data){
            // Filter incomming osc messages

            var {address, args, host, port} = data


            if (address.indexOf('/Stop')!=-1) {
                var [_, bar, _, seg] = address.split('/')

                address = '/led'
                args = [
                    {
                        type:'f',
                        value: 0
                    }
                ]
            }

            if (address.indexOf('/Segment')!=-1 && args.length == 3) {

                var [_, bar, _, seg] = address.split('/')

                if (seg == 'All') {

                    for (var i = 1; i < 9; i++) {
                        receiveOsc({
                            address: '/EDIT_SOFT',
                            args: [
                                {
                                    type:'s',
                                    value: `${bar}_${i}`
                                },
                                {
                                    type:'s',
                                    value:JSON.stringify({
                                        color:`rgb(${args[0].value}, ${args[1].value}, ${args[2].value})`
                                    })
                                }
                            ]
                        })
                    }

                } else {

                    address = '/EDIT_SOFT'
                    args = [
                        {
                            type:'s',
                            value: `${bar}_${seg}`
                        },
                        {
                            type:'s',
                            value:JSON.stringify({
                                color:`rgb(${args[0].value}, ${args[1].value}, ${args[2].value})`
                            })
                        }
                    ]

                }
            }

            return {address, args, host, port}

        },
        oscOutFilter: function(data){
            // Filter outgoing osc messages

            var {address, args, host, port} = data

            return {address, args, host, port}
        }
    }

})()
