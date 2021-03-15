
module.exports = {

    init: ()=>{


    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        return {address, args, host, port}

    },

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data

        return {address, args, host, port}

    }

}
