(function(){




    return {
        init: function(){
        },
        oscInFilter: function(data){
            // Filter incomming osc messages

            var {address, args, host, port} = data


            if (address.indexOf('/Stop')!=-1) {

                for (var bar of ['CC','CJ','BJ','BC']) {
                    for (var i of [1,2,3,4,5,6,7,8]) {
                        receiveOsc({
                            address: `/${bar}_${i}`,
                            args: [
                                {
                                    type:'f',
                                    value: 0
                                },
                                {
                                    type:'f',
                                    value: 0
                                },
                                {
                                    type:'f',
                                    value: 0
                                }
                            ]
                        })
                    }
                }

                return
            }

            if (address.indexOf('/Segment')!=-1 && args.length == 3) {

                var [_, bar, _, i] = address.split('/')

                if (i == 'All') {

                    for (var i = 1; i < 9; i++) {
                        receiveOsc({
                            address: `/${bar}_${i}`,
                            args: args
                        })
                    }

                    return

                } else {

                    address = `/${bar}_${i}`

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
